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
