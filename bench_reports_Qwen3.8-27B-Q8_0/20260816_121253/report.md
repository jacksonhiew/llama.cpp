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
- TURBOPREFILL: `1`
- TurboPrefill status: `active (TURBOPREFILL=1)`
- TurboPrefill version: `TurboPrefill:`
- llama.cpp git describe: `b10451-dirty`
- llama.cpp git commit: `10bf611e533d81f739128304991c5e133c6aebd8`
- Server PID: `76256`
- KEEP_SERVER_RUNNING: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/versions/TurboPrefill_b10451/bench_reports_Qwen3.8-27B-Q8_0/20260816_121253/llama_server.log`

## Environment

### TURBOPREFILL

```text
1
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
CPU(s) scaling MHz:                      97%
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
Память:         15Gi        10Gi       2.2Gi       1.3Gi       4.8Gi       5.4Gi
Подкачка:       23Gi       261Mi        23Gi
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
0.00.927.268 I srv    load_model: TurboPrefill: CUDA Graphs disabled for target and draft contexts
12.30.480.820 I decode: TurboPrefill requested=1 active=1 n_tokens=4097 n_ubatch=32 n_rs_seq=3 turbo_ubatches=127 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
12.30.553.678 I process_ubatch: TurboPrefill recurrent rs_z=0 first_ubatch=standard turbo_ubatches=126
12.42.655.340 I turboprefill: version=TurboPrefill_b10451_v2.1.3 accumulation_us=3969578 compute_us=7791189 total_us=11760767
12.43.790.614 I decode: TurboPrefill requested=1 active=0 n_tokens=4097 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
12.45.379.005 I decode: TurboPrefill requested=1 active=1 n_tokens=4097 n_ubatch=32 n_rs_seq=3 turbo_ubatches=127 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
12.45.388.222 I process_ubatch: TurboPrefill recurrent rs_z=-1 first_ubatch=turbo turbo_ubatches=127
12.54.722.999 I turboprefill: version=TurboPrefill_b10451_v2.1.3 accumulation_us=1131887 compute_us=8200067 total_us=9331954
12.55.764.182 I decode: TurboPrefill requested=1 active=0 n_tokens=4097 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
12.57.632.926 I decode: TurboPrefill requested=1 active=1 n_tokens=623 n_ubatch=32 n_rs_seq=3 turbo_ubatches=19 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
12.57.633.610 I process_ubatch: TurboPrefill recurrent rs_z=-1 first_ubatch=turbo turbo_ubatches=19
12.59.464.720 I turboprefill: version=TurboPrefill_b10451_v2.1.3 accumulation_us=291421 compute_us=1536896 total_us=1828317
12.59.706.477 I decode: TurboPrefill requested=1 active=0 n_tokens=623 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
13.15.608.579 I decode: TurboPrefill requested=1 active=1 n_tokens=232 n_ubatch=32 n_rs_seq=3 turbo_ubatches=7 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
13.15.609.550 I process_ubatch: TurboPrefill recurrent rs_z=0 first_ubatch=standard turbo_ubatches=6
13.16.518.257 I turboprefill: version=TurboPrefill_b10451_v2.1.3 accumulation_us=302923 compute_us=586200 total_us=889123
13.16.748.704 I decode: TurboPrefill requested=1 active=0 n_tokens=232 n_ubatch=32 n_rs_seq=0 turbo_ubatches=0 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
13.28.589.222 I decode: TurboPrefill requested=1 active=1 n_tokens=505 n_ubatch=32 n_rs_seq=3 turbo_ubatches=15 devices=6 pipeline=1 split_mode=1 embeddings_nextn=1
13.28.590.014 I process_ubatch: TurboPrefill recurrent rs_z=0 first_ubatch=standard turbo_ubatches=14
13.30.170.328 I turboprefill: version=TurboPrefill_b10451_v2.1.3 accumulation_us=534260 compute_us=1030880 total_us=1565140
```

## Server command

```bash
/home/serg/workspace/versions/TurboPrefill_b10451/build/bin/llama-server -m /mnt/models/AI/LLM/Qwen3.8-27B-Q8_0.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 999 -c 260000 --override-kv llama.context_length=int:260000 -b 4097 -ub 32 -np 1 -ctk f16 -ctv f16 -sm layer -ts 11/11/11/11/11/9 --flash-attn auto --no-warmup --no-mmproj --spec-type draft-mtp --spec-draft-n-max 3
```

Server PID: `76256`  
Stop command: `kill -INT 76256`

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 268 | 128 | 79.23 | 3.38 | 15.07 | 8.42 | 16.13 |
| ctx_000512.txt | 1 | 1 | 541 | 128 | 128.75 | 4.20 | 14.76 | 8.61 | 13.96 |
| ctx_001024.txt | 1 | 1 | 1082 | 128 | 205.19 | 5.27 | 11.71 | 10.85 | 17.39 |
| ctx_002048.txt | 1 | 1 | 2330 | 128 | 262.82 | 8.87 | 16.43 | 7.73 | 18.11 |
| ctx_004096.txt | 1 | 1 | 4288 | 128 | 311.72 | 13.76 | 12.50 | 10.16 | 25.84 |
| ctx_008192.txt | 1 | 1 | 8853 | 128 | 337.48 | 26.23 | 14.75 | 8.61 | 41.53 |
| ctx_016384.txt | 1 | 1 | 17670 | 128 | 315.55 | 56.00 | 13.62 | 9.33 | 69.75 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 100.0 | 100.0 | 51.4 | 51.4 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.0 | 52.0 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.9 | 50.9 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.3 | 53.3 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 9.0 | 9.0 | 49.7 | 49.7 | 7796 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 16.0 | 74.9 | 180.0 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 6.2 | 15.0 | 63.4 | 83.0 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 10.0 | 17.0 | 93.7 | 160.2 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 6.2 | 15.0 | 70.2 | 149.9 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 18.3 | 56.0 | 54.7 | 68.9 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 48.8 | 99.0 | 69.3 | 135.7 | 7796 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 97.0 | 97.0 | 140.0 | 140.0 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 90.0 | 90.0 | 145.9 | 145.9 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 97.0 | 97.0 | 163.1 | 163.1 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 91.0 | 91.0 | 168.5 | 168.5 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 85.0 | 85.0 | 159.5 | 159.5 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 62.0 | 62.0 | 163.2 | 163.2 | 7796 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 13.4 | 17.0 | 60.5 | 103.1 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 14.6 | 16.0 | 46.4 | 52.3 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 17.2 | 32.0 | 45.2 | 52.1 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 15.4 | 30.0 | 49.4 | 59.6 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 15.6 | 16.0 | 54.5 | 91.6 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 30.0 | 42.0 | 84.2 | 149.1 | 7796 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 46.5 | 93.0 | 109.8 | 168.1 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 45.0 | 90.0 | 117.3 | 182.6 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 49.0 | 98.0 | 113.4 | 176.7 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 45.0 | 90.0 | 114.6 | 175.9 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 45.5 | 91.0 | 122.8 | 194.4 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 59.5 | 98.0 | 72.4 | 85.9 | 7796 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 15.3 | 17.0 | 69.8 | 109.2 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 9.2 | 15.0 | 69.6 | 117.3 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 11.7 | 17.0 | 68.6 | 151.1 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 10.8 | 15.0 | 58.3 | 73.5 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 16.7 | 39.0 | 78.6 | 169.8 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 34.7 | 49.0 | 87.6 | 145.4 | 7796 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 48.5 | 97.0 | 108.9 | 170.4 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 44.8 | 90.0 | 113.8 | 186.0 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 48.8 | 98.0 | 115.0 | 183.8 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 63.8 | 92.0 | 109.0 | 181.3 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 63.8 | 92.0 | 107.1 | 180.1 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 33.5 | 63.0 | 90.2 | 157.0 | 7796 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 9.0 | 17.0 | 64.6 | 99.0 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 13.2 | 15.0 | 81.5 | 140.6 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 12.8 | 17.0 | 84.2 | 165.0 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 15.0 | 15.0 | 80.6 | 148.1 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 15.0 | 15.0 | 85.2 | 130.4 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 33.8 | 42.0 | 67.6 | 116.1 | 7796 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 58.2 | 97.0 | 104.5 | 169.0 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 58.8 | 91.0 | 120.9 | 185.9 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 65.0 | 98.0 | 118.2 | 179.6 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 60.6 | 91.0 | 112.6 | 163.1 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 55.4 | 94.0 | 115.9 | 189.5 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 58.4 | 98.0 | 125.7 | 166.8 | 7796 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 14.8 | 18.0 | 53.2 | 84.1 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 13.3 | 16.0 | 76.8 | 183.6 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 3.7 | 10.0 | 52.7 | 82.1 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 13.8 | 17.0 | 63.6 | 95.6 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 12.8 | 26.0 | 57.7 | 99.1 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 48.2 | 90.0 | 72.0 | 119.3 | 7796 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 56.8 | 98.0 | 124.0 | 170.1 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 53.2 | 91.0 | 110.9 | 177.6 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 52.0 | 98.0 | 109.2 | 181.6 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 53.2 | 94.0 | 113.1 | 187.9 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 57.8 | 92.0 | 116.1 | 189.2 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 50.0 | 70.0 | 85.9 | 162.3 | 7796 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 7.6 | 19.0 | 76.1 | 167.2 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 8.3 | 17.0 | 51.8 | 59.5 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 10.6 | 19.0 | 56.5 | 101.3 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 19.0 | 65.0 | 66.3 | 151.5 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 17.0 | 63.0 | 52.2 | 56.1 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 43.9 | 98.0 | 70.1 | 136.7 | 7796 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 59.4 | 98.0 | 122.0 | 179.6 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 53.3 | 92.0 | 114.4 | 183.2 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 59.5 | 99.0 | 119.3 | 185.6 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 56.7 | 95.0 | 122.6 | 190.8 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 59.0 | 98.0 | 118.0 | 186.1 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 63.2 | 98.0 | 98.0 | 162.6 | 7796 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 8.2 | 20.0 | 73.2 | 168.6 | 7976 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 8.7 | 17.0 | 68.9 | 123.2 | 6582 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 21.3 | 82.0 | 64.6 | 121.3 | 7976 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 12.0 | 18.0 | 55.9 | 57.3 | 7572 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 8.8 | 18.0 | 55.3 | 60.2 | 7572 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 31.5 | 79.0 | 69.7 | 126.6 | 7796 |


## CPU / RAM / swap load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 38.9 %, max 38.9 %

RAM used: avg 5126 MiB, max 5126 MiB, avg 32.3 %, max 32.3 %

Swap used: avg 364 MiB, max 364 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 98.1 | 98.1 |
| 1 | 22.5 | 22.5 |
| 2 | 19.2 | 19.2 |
| 3 | 14.4 | 14.4 |

Decode stage:

CPU total: avg 39.0 %, max 51.5 %

RAM used: avg 5004 MiB, max 5155 MiB, avg 31.5 %, max 32.5 %

Swap used: avg 363 MiB, max 364 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 23.1 | 62.0 |
| 1 | 99.9 | 100.0 |
| 2 | 15.8 | 30.6 |
| 3 | 17.0 | 23.8 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 35.8 %, max 35.8 %

RAM used: avg 5454 MiB, max 5454 MiB, avg 34.4 %, max 34.4 %

Swap used: avg 363 MiB, max 363 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 16.4 | 16.4 |
| 1 | 9.3 | 9.3 |
| 2 | 90.7 | 90.7 |
| 3 | 26.8 | 26.8 |

Decode stage:

CPU total: avg 40.7 %, max 51.4 %

RAM used: avg 5420 MiB, max 5485 MiB, avg 34.1 %, max 34.5 %

Swap used: avg 363 MiB, max 363 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 17.2 | 25.2 |
| 1 | 45.1 | 100.0 |
| 2 | 82.6 | 100.0 |
| 3 | 17.4 | 21.3 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 40.0 %, max 42.4 %

RAM used: avg 5718 MiB, max 5736 MiB, avg 36.0 %, max 36.1 %

Swap used: avg 363 MiB, max 363 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 18.2 | 20.9 |
| 1 | 17.8 | 24.7 |
| 2 | 45.3 | 67.3 |
| 3 | 78.8 | 100.0 |

Decode stage:

CPU total: avg 36.2 %, max 36.7 %

RAM used: avg 6009 MiB, max 6073 MiB, avg 37.9 %, max 38.3 %

Swap used: avg 363 MiB, max 363 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 15.2 | 21.2 |
| 1 | 15.2 | 22.5 |
| 2 | 14.1 | 18.0 |
| 3 | 99.8 | 100.0 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 42.5 %, max 46.3 %

RAM used: avg 6444 MiB, max 6463 MiB, avg 40.6 %, max 40.7 %

Swap used: avg 362 MiB, max 362 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 19.9 | 28.4 |
| 1 | 93.5 | 100.0 |
| 2 | 33.8 | 52.4 |
| 3 | 22.5 | 27.0 |

Decode stage:

CPU total: avg 36.2 %, max 36.5 %

RAM used: avg 6500 MiB, max 6527 MiB, avg 40.9 %, max 41.1 %

Swap used: avg 362 MiB, max 362 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 17.4 | 23.4 |
| 1 | 100.0 | 100.0 |
| 2 | 13.1 | 21.0 |
| 3 | 14.2 | 20.3 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 42.0 %, max 51.1 %

RAM used: avg 6978 MiB, max 7074 MiB, avg 44.0 %, max 44.6 %

Swap used: avg 362 MiB, max 362 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 21.8 | 28.6 |
| 1 | 52.7 | 100.0 |
| 2 | 72.9 | 100.0 |
| 3 | 20.6 | 29.6 |

Decode stage:

CPU total: avg 38.7 %, max 40.3 %

RAM used: avg 7090 MiB, max 7145 MiB, avg 44.7 %, max 45.0 %

Swap used: avg 362 MiB, max 362 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 18.3 | 23.1 |
| 1 | 94.8 | 100.0 |
| 2 | 16.9 | 22.9 |
| 3 | 24.4 | 49.8 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 43.5 %, max 52.0 %

RAM used: avg 6843 MiB, max 7901 MiB, avg 43.1 %, max 49.8 %

Swap used: avg 362 MiB, max 362 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 24.0 | 36.3 |
| 1 | 23.7 | 32.9 |
| 2 | 63.6 | 100.0 |
| 3 | 62.5 | 100.0 |

Decode stage:

CPU total: avg 39.8 %, max 51.6 %

RAM used: avg 6859 MiB, max 6993 MiB, avg 43.2 %, max 44.1 %

Swap used: avg 362 MiB, max 362 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 89.7 | 100.0 |
| 1 | 18.4 | 25.5 |
| 2 | 31.1 | 99.5 |
| 3 | 19.5 | 31.3 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

CPU total: avg 42.7 %, max 52.8 %

RAM used: avg 7956 MiB, max 8209 MiB, avg 50.1 %, max 51.7 %

Swap used: avg 362 MiB, max 362 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 65.4 | 100.0 |
| 1 | 23.7 | 34.0 |
| 2 | 54.7 | 100.0 |
| 3 | 26.7 | 94.5 |

Decode stage:

CPU total: avg 39.3 %, max 53.1 %

RAM used: avg 8359 MiB, max 8430 MiB, avg 52.7 %, max 53.1 %

Swap used: avg 362 MiB, max 362 MiB, avg 1.5 %, max 1.5 %

| Logical CPU | avg util % | max util % |
|---:|---:|---:|
| 0 | 96.4 | 100.0 |
| 1 | 14.4 | 18.1 |
| 2 | 26.9 | 90.4 |
| 3 | 19.1 | 25.6 |

