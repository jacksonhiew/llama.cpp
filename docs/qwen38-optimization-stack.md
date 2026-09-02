# Qwen3.8 Flash Next optimization stack

Official baseline: `b96806d96061049a5b574269b049bf6241d63d46` (`upstream/master`, 2026-09-02).

| Change | Source | Integration status | Runtime behavior |
| --- | --- | --- | --- |
| Response API compatibility | local `fix/response-api-compatibility`, source commit `404d2a0fd` | Cherry-picked as `18dee5611` | Preserves current master APIs while accepting the downstream response inputs. |
| KV / previous-token lookup | PR #28128, `8d9c71931`; superseded by PR #28040, `b356fa262` | Already upstream; PR #28128 skipped | Current master uses the sequence-position index. No downstream toggle. |
| CUDA batched TOP_K | PR #28129, `95d9bdcc2` | Cherry-picked as `bdcab0c25` | Large CUB batches use the existing row-parallel argsort path; small batches keep `DeviceTopK`. |
| Sparse QSA gather | PR #28130, `e74cec36e` and `3bda5d023`; maintained equivalents `541f63a63` and `e89368c24` in Unsloth PR #165 | Forward-ported as `96776099d` and `242af8151` | Enabled for eligible decode batches. Set `QWEN4EXP_QSA_GATHER=0` to use the masked path. |
| PLE lazy direct read | PR #28136, `905557969` | Cherry-picked as `fedd388a7` | Opt in with `--lazy-mode on-direct`; unsupported or unavailable direct reads fall back to lazy mmap reads. |
| NextN / MTP | PR #27836, `d303eec92`, `d72620018`, and `1d8de7c1b` | Cherry-picked as `678eb3aac`, `5df5d5c54`, and `518a80178` | Compiled in but opt-in through `--spec-type draft-mtp`; converter export uses `--mtp`. |

The QSA conflict resolution retains current master's block grouping, sequence handling, M-RoPE ordering, and indexer-head fixes. MTP remains optional and normal inference defaults are unchanged.

## Supplemental fixes

| Change | Source | Status and local commit | Scope |
| --- | --- | --- | --- |
| Unsloth MTP sidecar compatibility | PR #28097, `3fb9b98` | Forward-ported as `3252597b9` | Supports draft-head-only loading and the correct draft path; trunk, PLE, and HC tensors remain optional. |
| Separate KV detection for `draft-mtp` | PR #27781, `4e627fe` | Cherry-picked as `fb9555812` | Detects shared KV from memory cells. |
| Multi-ubatch MTP serialization | PR #26827, `2295535` | Forward-ported as `8b6a01d25` | Synchronizes only MTP multi-ubatch decode; source test-fixture changes were omitted. |
| Complete `h_nextn` output ordering | PR #28104, `77476ce` | Already present; skipped | The existing #27836 path gathers output rows after exporting the complete `h_nextn`. |
| On-device speculative checkpoints | PR #28104, `175b66c` | Cherry-picked as `457b94fca` | Uses `LLAMA_STATE_SEQ_FLAGS_ON_DEVICE` only for live speculative rollback state. |
| Replay after rollback | PR #28061, `611953af` | Cherry-picked as `6e893f5ca` | Prevents replayed accepted tokens from being verified again. |
| MTP converter HC mixer export | rmonsurate PR #1, `57bb668` | Cherry-picked as `97596b13e` | Keeps the model-level HyperConnection head mixer in detached `--mtp` exports. |
| Gated DeltaNet normalization | PR #28068, `c03dc68` | Cherry-picked as `a563179df` | Uses the shared `rsqrt(sum(x^2) + eps)`-equivalent normalization helper. |
| Ngram cache request reset | PR #27866, `459ed0a` | Forward-ported as `7327a23da` | Resets speculative ngram state at request start; source test-file additions were omitted. |
| CUDA MoE MMQ tail padding | issue #27792 | Forward-ported as `5792d17c5` | Uses the padded get-rows extent when selecting `J_max`; no other MMQ behavior changed. |
| PLE direct-read weight lifetime | PR #28136, `905557969` | Forward-ported as `a4475d7ed` | Keeps tensor file metadata available for direct reads while preserving metadata-only model loading. |
| PLE offsets and graph reuse | PR #28136 and follow-up `d807f04` | Already present; skipped | Offsets are applied once; direct mode checks staged data and mmap mode checks row indexes. |
| Qwen4Exp tensor split enablement | Existing tensor metadata implementation | Enabled as `e7ab10349` | Removes the architecture gate so the existing experimental tensor-parallel path can be selected. |
| Lazy-read CLI compatibility | Former `--tensor-read-lazy` interface | Forward-ported as `aed8fca5f` | Accepts the old spelling as an alias for `--lazy-mode`; mode values keep their existing meaning. |
| Qwen4Exp routed-MoE MMQ scheduling | Local Nsight profile, SM75 | Experimental working-tree change | `--qwen4exp-exp-moe-mmq on` selects direct tiled MMQ only for Qwen4Exp 512-expert/top-10 prefill on SM75; default `off` keeps stream-K. |

MTP remains explicitly opt-in through `--spec-type draft-mtp`. These supplemental fixes do not change normal prompt-cache storage or default inference behavior.

Set `QWEN4EXP_PERF_TRACE=1` to log per-ubatch PLE host timings and QSA input dimensions. The trace is disabled by default and does not change graph computation.
