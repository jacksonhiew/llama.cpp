# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/mnt/models/AI/LLM/Qwen3.8-27B-Q8_0.gguf`
- NGL: `999`
- CTX_SIZE: `260000`
- N_GEN: `128`
- BATCH: `4097`
- UBATCH: `32`
- CTK: `f16`
- CTV: `f16`
- SPEC_TYPE: `draft-mtp`
- SPEC_DRAFT_N_MAX: `3`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `11/11/11/11/11/9`
- PARALLEL: `1`
- TEMPERATURE: `0.15`
- CACHE_PROMPT: `0`
- FLASH_ATTN: `auto`
- THREADS: `auto`
- THREADS_BATCH: `auto`
- REPEATS: `1`
- CUDA_VISIBLE_DEVICES: `0,1,2,3,4,5`
- TURBOPREFILL: `0`
- TurboPrefill status: `TurboPrefill implementation detected; inactive (TURBOPREFILL=0)`
- TurboPrefill version: `TurboPrefill`
- llama.cpp git describe: `b10451-dirty`
- llama.cpp git commit: `10bf611e533d81f739128304991c5e133c6aebd8`
- Server PID: `86706`
- KEEP_SERVER_RUNNING: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/versions/TurboPrefill_b10451/bench_reports_Qwen3.8-27B-Q8_0/20260816_123012/llama_server.log`

## Environment

### TURBOPREFILL

```text
0
```

### RUN_DIR

```text
/home/serg/workspace/versions/TurboPrefill_b10451
```

### CONFIG_PATH

```text
/home/serg/workspace/versions/TurboPrefill_b10451/config_Qwen_3.8.sh
```

### LLAMA_SERVER_BIN

```text
/home/serg/workspace/versions/TurboPrefill_b10451/build/bin/llama-server
```

### LOCAL_LD_LIBRARY_PATH

```text
/home/serg/workspace/versions/TurboPrefill_b10451/build/bin
```

### CUDA_VISIBLE_DEVICES_effective

```text
0,1,2,3,4,5
```

### selected_gpu_count

```text
6
```

### selected_gpu_models

```text
NVIDIA P104-100 x6
```

### llama_server_version

```text
version: 0.1.0-dev (build 1, commit 10bf611)
built with GNU 13.3.0 for Linux x86_64
```

### uname

```text
Linux turboprefill 6.17.0-29-generic #29~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon May 11 10:30:58 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
```

### lscpu

```text
Архитектура:                             x86_64
CPU op-mode(s):                          32-bit, 64-bit
Address sizes:                           39 bits physical, 48 bits virtual
Порядок байт:                            Little Endian
CPU(s):                                  4
On-line CPU(s) list:                     0-3
ID прроизводителя:                       GenuineIntel
Имя модели:                              Intel(R) Core(TM) i5-7500 CPU @ 3.40GHz
Семейство ЦПУ:                           6
Модель:                                  158
Потоков на ядро:                         1
Ядер на сокет:                           4
Сокетов:                                 1
Степпинг:                                9
CPU(s) scaling MHz:                      50%
CPU max MHz:                             3800.0000
CPU min MHz:                             800.0000
BogoMIPS:                                6799.81
Флаги:                                   fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault pti ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp md_clear flush_l1d arch_capabilities
L1d cache:                               128 KiB (4 instances)
L1i cache:                               128 KiB (4 instances)
L2 cache:                                1 MiB (4 instances)
L3 cache:                                6 MiB (1 instance)
NUMA node(s):                            1
NUMA node0 CPU(s):                       0-3
Vulnerability Gather data sampling:      Vulnerable
Vulnerability Ghostwrite:                Not affected
Vulnerability Indirect target selection: Not affected
Vulnerability Itlb multihit:             KVM: Mitigation: VMX unsupported
Vulnerability L1tf:                      Mitigation; PTE Inversion
Vulnerability Mds:                       Mitigation; Clear CPU buffers; SMT disabled
Vulnerability Meltdown:                  Mitigation; PTI
Vulnerability Mmio stale data:           Mitigation; Clear CPU buffers; SMT disabled
Vulnerability Old microcode:             Not affected
Vulnerability Reg file data sampling:    Not affected
Vulnerability Retbleed:                  Mitigation; IBRS
Vulnerability Spec rstack overflow:      Not affected
Vulnerability Spec store bypass:         Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:                Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:                Mitigation; IBRS; IBPB conditional; STIBP disabled; RSB filling; PBRSB-eIBRS Not affected; BHI Not affected
Vulnerability Srbds:                     Mitigation; Microcode
Vulnerability Tsa:                       Not affected
Vulnerability Tsx async abort:           Mitigation; TSX disabled
Vulnerability Vmscape:                   Mitigation; IBPB before exit to userspace
```

### motherboard_vendor

```text
ASUSTeK COMPUTER INC.
```

### motherboard_name

```text
B250 MINING EXPERT
```

### motherboard_version

```text
Rev X.0x
```

### memory_summary

```text
всего        занят        своб      общая  буф/врем.   доступно
Память:         15Gi       8.1Gi       287Mi       1.3Gi       8.6Gi       7.4Gi
Подкачка:       23Gi       284Mi        23Gi
```

### memory_modules

```text
unavailable: Command '['dmidecode', '--type', '17']' returned non-zero exit status 1.
```

### nvidia_smi

```text
0, NVIDIA P104-100, 00000000:01:00.0, 535.309.01, 8192 MiB, 1, 1
1, NVIDIA P104-100, 00000000:02:00.0, 535.309.01, 8192 MiB, 1, 1
2, NVIDIA P104-100, 00000000:0A:00.0, 535.309.01, 8192 MiB, 1, 1
3, NVIDIA P104-100, 00000000:0C:00.0, 535.309.01, 8192 MiB, 1, 1
4, NVIDIA P104-100, 00000000:0D:00.0, 535.309.01, 8192 MiB, 1, 1
5, NVIDIA P104-100, 00000000:0E:00.0, 535.309.01, 8192 MiB, 1, 1
6, NVIDIA P104-100, 00000000:0F:00.0, 535.309.01, 8192 MiB, 1, 1
7, NVIDIA P104-100, 00000000:10:00.0, 535.309.01, 8192 MiB, 1, 1
8, NVIDIA P104-100, 00000000:11:00.0, 535.309.01, 8192 MiB, 1, 1
9, NVIDIA P104-100, 00000000:12:00.0, 535.309.01, 8192 MiB, 1, 1
10, NVIDIA P104-100, 00000000:13:00.0, 535.309.01, 8192 MiB, 1, 1
11, NVIDIA P104-100, 00000000:14:00.0, 535.309.01, 8192 MiB, 1, 1
```

### nvcc

```text
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Fri_Jan__6_16:45:21_PST_2023
Cuda compilation tools, release 12.0, V12.0.140
Build cuda_12.0.r12.0/compiler.32267302_0
```

### cmake

```text
cmake version 3.28.3

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

### git_describe

```text
b10451-dirty
```

### git_commit

```text
10bf611e533d81f739128304991c5e133c6aebd8
```

### git_last_commit

```text
2026-08-16 09:38:01 +0300
llama : check LoRA tensor data is within file bounds (#27056)
```

### git_turboprefill_hint

```text
none
```

### model_path

```text
/mnt/models/AI/LLM/Qwen3.8-27B-Q8_0.gguf
```

### model_filename

```text
Qwen3.8-27B-Q8_0.gguf
```

### model_size_bytes

```text
29047084352
```

### model_size_gib

```text
27.052
```

### gguf_architecture

```text
qwen35
```

### gguf_tensor_count

```text
866
```

### gguf_tensor_types

```text
F32:360, Q8_0:506
```

### model_sha256

```text
disabled (MODEL_HASH=0)
```

### TurboPrefill runtime markers

```text
12.35.248.153 I decode: TurboPrefill requested=0 active=0 n_tokens=4097 n_ubatch=32 n_rs_seq=3 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
13.14.694.660 I decode: TurboPrefill requested=0 active=0 n_tokens=4097 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
13.16.317.750 I decode: TurboPrefill requested=0 active=0 n_tokens=4097 n_ubatch=32 n_rs_seq=3 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
13.53.711.277 I decode: TurboPrefill requested=0 active=0 n_tokens=4097 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
13.55.562.412 I decode: TurboPrefill requested=0 active=0 n_tokens=623 n_ubatch=32 n_rs_seq=3 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
14.01.651.678 I decode: TurboPrefill requested=0 active=0 n_tokens=623 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
14.18.081.028 I decode: TurboPrefill requested=0 active=0 n_tokens=232 n_ubatch=32 n_rs_seq=3 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
14.21.701.319 I decode: TurboPrefill requested=0 active=0 n_tokens=232 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
14.33.611.578 I decode: TurboPrefill requested=0 active=0 n_tokens=505 n_ubatch=32 n_rs_seq=3 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
14.37.795.680 I decode: TurboPrefill requested=0 active=0 n_tokens=505 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
14.49.916.500 I decode: TurboPrefill requested=0 active=0 n_tokens=1046 n_ubatch=32 n_rs_seq=3 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
14.58.923.474 I decode: TurboPrefill requested=0 active=0 n_tokens=1046 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
15.13.979.427 I decode: TurboPrefill requested=0 active=0 n_tokens=2294 n_ubatch=32 n_rs_seq=3 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
15.34.574.282 I decode: TurboPrefill requested=0 active=0 n_tokens=2294 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
15.47.487.211 I decode: TurboPrefill requested=0 active=0 n_tokens=4097 n_ubatch=32 n_rs_seq=3 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
16.22.163.717 I decode: TurboPrefill requested=0 active=0 n_tokens=4097 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
16.23.737.987 I decode: TurboPrefill requested=0 active=0 n_tokens=155 n_ubatch=32 n_rs_seq=3 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
16.25.042.314 I decode: TurboPrefill requested=0 active=0 n_tokens=155 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
16.44.281.558 I decode: TurboPrefill requested=0 active=0 n_tokens=4097 n_ubatch=32 n_rs_seq=3 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
17.18.956.151 I decode: TurboPrefill requested=0 active=0 n_tokens=4097 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
```

## Server command

```bash
/home/serg/workspace/versions/TurboPrefill_b10451/build/bin/llama-server -m /mnt/models/AI/LLM/Qwen3.8-27B-Q8_0.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 999 -c 260000 --override-kv llama.context_length=int:260000 -b 4097 -ub 32 -np 1 -ctk f16 -ctv f16 -sm layer -ts 11/11/11/11/11/9 --flash-attn auto --no-warmup --no-mmproj --spec-type draft-mtp --spec-draft-n-max 3
```

Server PID: `86706`  
Stop command: `kill -INT 86706`

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 268 | 128 | 45.72 | 5.86 | 14.94 | 8.50 | 18.69 |
| ctx_000512.txt | 1 | 1 | 541 | 128 | 82.98 | 6.52 | 14.91 | 8.52 | 16.18 |
| ctx_001024.txt | 1 | 1 | 1082 | 128 | 93.55 | 11.57 | 11.52 | 11.02 | 23.85 |
| ctx_002048.txt | 1 | 1 | 2330 | 128 | 98.41 | 23.68 | 16.20 | 7.84 | 32.99 |
| ctx_004096.txt | 1 | 1 | 4288 | 128 | 107.30 | 39.96 | 12.54 | 10.12 | 52.06 |
| ctx_008192.txt | 1 | 1 | 8853 | 128 | 105.25 | 84.11 | 14.68 | 8.65 | 99.45 |
| ctx_016384.txt | 1 | 1 | 17670 | 128 | 98.88 | 178.71 | 13.45 | 9.45 | 192.55 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 27.0 | 54.0 | 115.2 | 179.2 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.7 | 58.3 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 113.3 | 176.0 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.6 | 53.7 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.3 | 52.3 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 33.5 | 67.0 | 50.0 | 50.1 | 7794 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 14.5 | 32.0 | 56.1 | 78.9 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 10.8 | 30.0 | 72.4 | 167.7 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 13.0 | 17.0 | 53.4 | 63.9 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 20.7 | 64.0 | 76.3 | 127.4 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 11.8 | 26.0 | 73.5 | 124.5 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 21.3 | 42.0 | 71.6 | 124.1 | 7794 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 10.7 | 32.0 | 93.0 | 176.8 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 7.7 | 23.0 | 53.2 | 54.4 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 4.3 | 13.0 | 67.3 | 100.9 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 18.3 | 30.0 | 77.4 | 127.6 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 20.3 | 30.0 | 51.9 | 53.3 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 23.7 | 51.0 | 50.3 | 50.8 | 7794 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 12.8 | 16.0 | 62.7 | 92.4 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 11.2 | 15.0 | 59.2 | 77.4 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 14.8 | 17.0 | 80.8 | 167.9 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 11.5 | 15.0 | 55.4 | 59.7 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 15.8 | 16.0 | 54.5 | 89.6 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 31.2 | 42.0 | 101.4 | 151.1 | 7794 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 6.8 | 32.0 | 58.1 | 97.9 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 12.0 | 30.0 | 62.9 | 104.5 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 15.4 | 32.0 | 64.2 | 121.0 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 13.0 | 31.0 | 51.3 | 54.4 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 12.0 | 30.0 | 54.7 | 59.7 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 28.0 | 98.0 | 72.8 | 108.9 | 7794 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 14.2 | 17.0 | 77.4 | 110.9 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 13.5 | 16.0 | 66.0 | 143.9 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 8.7 | 17.0 | 100.2 | 168.5 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 11.3 | 15.0 | 54.3 | 55.6 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 14.5 | 15.0 | 55.0 | 62.4 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 34.3 | 42.0 | 64.8 | 91.9 | 7794 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 15.4 | 33.0 | 64.5 | 172.6 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 9.1 | 31.0 | 89.8 | 185.2 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 16.5 | 33.0 | 89.2 | 180.2 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 19.4 | 31.0 | 58.0 | 102.3 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 17.8 | 31.0 | 59.4 | 122.6 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 14.7 | 23.0 | 52.4 | 84.1 | 7794 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 12.6 | 27.0 | 46.3 | 52.6 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 14.0 | 28.0 | 54.1 | 58.6 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 5.8 | 17.0 | 61.1 | 90.3 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 5.4 | 15.0 | 96.2 | 159.8 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 12.8 | 16.0 | 63.3 | 91.6 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 32.0 | 42.0 | 99.9 | 148.2 | 7794 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 31.6 | 66.0 | 72.8 | 171.8 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 24.7 | 62.0 | 73.1 | 174.6 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 26.4 | 67.0 | 88.9 | 185.0 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 22.8 | 62.0 | 86.3 | 184.6 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 21.2 | 60.0 | 87.4 | 189.7 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 20.9 | 41.0 | 59.8 | 136.9 | 7794 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 20.7 | 35.0 | 68.8 | 129.8 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 10.7 | 16.0 | 56.1 | 70.0 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 10.7 | 18.0 | 75.4 | 159.0 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 13.2 | 16.0 | 48.7 | 54.5 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 14.0 | 17.0 | 49.3 | 57.6 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 40.7 | 43.0 | 88.9 | 170.3 | 7794 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 18.7 | 100.0 | 76.5 | 183.7 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 14.0 | 66.0 | 93.6 | 191.5 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 16.3 | 74.0 | 88.4 | 173.2 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 16.6 | 43.0 | 62.0 | 156.2 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 20.6 | 70.0 | 69.3 | 176.9 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 21.3 | 98.0 | 59.0 | 159.8 | 7794 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 13.0 | 38.0 | 70.1 | 129.0 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 15.9 | 66.0 | 58.2 | 116.8 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 21.0 | 53.0 | 56.8 | 70.6 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 25.1 | 72.0 | 78.8 | 162.2 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 16.9 | 47.0 | 69.0 | 182.3 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 20.4 | 44.0 | 61.1 | 94.7 | 7794 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 21.4 | 84.0 | 68.6 | 176.4 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 20.2 | 69.0 | 68.0 | 183.1 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 23.8 | 77.0 | 72.6 | 184.5 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 20.8 | 74.0 | 73.4 | 191.1 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 18.0 | 67.0 | 77.1 | 186.8 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 16.4 | 98.0 | 71.7 | 162.8 | 7794 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 12.6 | 44.0 | 54.4 | 66.9 | 7974 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 12.1 | 39.0 | 62.9 | 153.7 | 6580 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 10.4 | 19.0 | 65.3 | 87.0 | 7974 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 12.4 | 26.0 | 100.0 | 192.0 | 7570 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 19.3 | 73.0 | 88.6 | 164.3 | 7570 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 37.0 | 47.0 | 55.6 | 81.9 | 7794 |


## CPU / RAM / swap load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 43.6 %, max 50.0 %

RAM used: avg 3664 MiB, max 3782 MiB, avg 23.1 %, max 23.8 %

Swap used: avg 382 MiB, max 382 MiB, avg 1.6 %, max 1.6 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 17.7 | 23.4 |
| 1 | 85.1 | 98.7 |
| 2 | 16.3 | 25.4 |
| 3 | 55.2 | 98.1 |

Decode stage:

CPU total: avg 33.7 %, max 37.1 %

RAM used: avg 3742 MiB, max 3832 MiB, avg 23.6 %, max 24.1 %

Swap used: avg 382 MiB, max 382 MiB, avg 1.6 %, max 1.6 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 13.1 | 15.0 |
| 1 | 15.3 | 24.3 |
| 2 | 19.1 | 24.2 |
| 3 | 87.2 | 100.0 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 39.0 %, max 43.7 %

RAM used: avg 4238 MiB, max 4262 MiB, avg 26.7 %, max 26.8 %

Swap used: avg 381 MiB, max 381 MiB, avg 1.6 %, max 1.6 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 25.3 | 46.7 |
| 1 | 94.8 | 100.0 |
| 2 | 23.2 | 25.7 |
| 3 | 12.1 | 15.3 |

Decode stage:

CPU total: avg 38.1 %, max 43.6 %

RAM used: avg 4309 MiB, max 4318 MiB, avg 27.1 %, max 27.2 %

Swap used: avg 381 MiB, max 381 MiB, avg 1.6 %, max 1.6 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 99.2 | 100.0 |
| 1 | 17.7 | 39.5 |
| 2 | 17.7 | 19.4 |
| 3 | 17.9 | 18.8 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 36.8 %, max 38.0 %

RAM used: avg 4753 MiB, max 4785 MiB, avg 29.9 %, max 30.1 %

Swap used: avg 381 MiB, max 381 MiB, avg 1.6 %, max 1.6 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 96.6 | 100.0 |
| 1 | 15.5 | 21.1 |
| 2 | 17.2 | 20.5 |
| 3 | 17.7 | 24.5 |

Decode stage:

CPU total: avg 38.8 %, max 49.9 %

RAM used: avg 4796 MiB, max 4821 MiB, avg 30.2 %, max 30.4 %

Swap used: avg 381 MiB, max 381 MiB, avg 1.6 %, max 1.6 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 57.3 | 99.5 |
| 1 | 19.1 | 24.4 |
| 2 | 11.9 | 19.7 |
| 3 | 66.7 | 100.0 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 37.0 %, max 41.6 %

RAM used: avg 5122 MiB, max 5243 MiB, avg 32.3 %, max 33.0 %

Swap used: avg 381 MiB, max 381 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 63.6 | 100.0 |
| 1 | 17.2 | 23.6 |
| 2 | 15.6 | 19.2 |
| 3 | 51.6 | 96.7 |

Decode stage:

CPU total: avg 37.5 %, max 39.7 %

RAM used: avg 5183 MiB, max 5260 MiB, avg 32.6 %, max 33.1 %

Swap used: avg 381 MiB, max 381 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 100.0 | 100.0 |
| 1 | 12.7 | 16.2 |
| 2 | 18.4 | 23.7 |
| 3 | 18.6 | 24.7 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 38.9 %, max 50.2 %

RAM used: avg 5689 MiB, max 5801 MiB, avg 35.8 %, max 36.5 %

Swap used: avg 381 MiB, max 381 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 51.2 | 100.0 |
| 1 | 15.2 | 21.8 |
| 2 | 70.1 | 100.0 |
| 3 | 18.8 | 25.8 |

Decode stage:

CPU total: avg 40.4 %, max 53.4 %

RAM used: avg 5869 MiB, max 5917 MiB, avg 37.0 %, max 37.3 %

Swap used: avg 381 MiB, max 381 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 71.8 | 100.0 |
| 1 | 16.1 | 26.4 |
| 2 | 25.6 | 65.6 |
| 3 | 47.8 | 100.0 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 38.5 %, max 50.8 %

RAM used: avg 5449 MiB, max 6746 MiB, avg 34.3 %, max 42.5 %

Swap used: avg 380 MiB, max 381 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 64.7 | 100.0 |
| 1 | 16.2 | 28.5 |
| 2 | 55.4 | 100.0 |
| 3 | 17.4 | 25.5 |

Decode stage:

CPU total: avg 39.9 %, max 50.9 %

RAM used: avg 5537 MiB, max 5756 MiB, avg 34.9 %, max 36.3 %

Swap used: avg 380 MiB, max 380 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 28.8 | 66.7 |
| 1 | 13.2 | 15.6 |
| 2 | 77.0 | 100.0 |
| 3 | 40.4 | 100.0 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 38.6 %, max 52.6 %

RAM used: avg 6460 MiB, max 6738 MiB, avg 40.7 %, max 42.4 %

Swap used: avg 380 MiB, max 380 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 16.9 | 28.2 |
| 1 | 38.5 | 100.0 |
| 2 | 37.7 | 100.0 |
| 3 | 60.9 | 100.0 |

Decode stage:

CPU total: avg 39.1 %, max 46.5 %

RAM used: avg 6795 MiB, max 6897 MiB, avg 42.8 %, max 43.4 %

Swap used: avg 380 MiB, max 380 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 13.8 | 17.8 |
| 1 | 87.4 | 100.0 |
| 2 | 37.3 | 100.0 |
| 3 | 17.6 | 21.6 |

