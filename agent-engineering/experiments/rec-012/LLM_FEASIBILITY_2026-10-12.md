# REC-012 — Local LLM feasibility preflight (2026-10-12)

Status: **EXECUTED ENVIRONMENT AUDIT / BLOCKED FOR REAL-MODEL COMPARISON**  
Host: **ephemeral ChatGPT execution container**, not the user's Windows/Android hardware.  
Scope: do not infer properties of the user's own workstation.

## Purpose

Test whether the missing real-model single-agent vs manager-specialists experiment can be executed **now**, without model API charges, GitHub Actions, outside hosting or speculative subscriptions. This is a feasibility receipt, **not** a completed experiment.

## Observed local hardware/software

| Dimension | Observed | Evidence type |
|---|---|---|
| Operating system | Linux x86_64, kernel 6.18.44 | `uname` / Python platform |
| Logical CPU count | 5 | `nproc` / `os.cpu_count()` |
| RAM | 5.8 GiB total, ~4.6 GiB available at inspection | `free -h`, `/proc/meminfo` |
| Swap | 0 GiB | `free -h` |
| GPU | no NVIDIA tools, no exposed CUDA or `/dev/dri` | `nvidia-smi` not found, device inspection, `torch.cuda.is_available() == False` |
| PyTorch | 2.10.0+cpu installed | module import |
| Inference runtimes | no `ollama`, `llama-cli`, `llama-server`, `llama_cpp`, `transformers`, `vllm` | command/module probes |
| Potential build tools | `g++` and `cmake` present | command resolution |
| Model assets | no visible GGUF/safetensors/ONNX/torch checkpoint in inspected cache/workspace paths | bounded `find`/workspace scan |
| Network | `huggingface.co` and `pypi.org` direct HEAD requests failed at DNS with HTTP `000` | `curl` probes |
| Alternate asset fetch | container downloader of Qwen3-0.6B `config.json` failed | downloader returned `download failed` |
| Model inference | **NOT RUN** | absent model and failed download |
| Token count/model cost | **NOT_MEASURED** | no model calls |

All values are point-in-time readings. Environment RAM/GPU and network permissions may differ on another host.

## Candidate for a future permitted environment — not installed or tested

A publicly documented [GGUF quantization of Qwen3-0.6B](https://huggingface.co/tensorblock/Qwen_Qwen3-0.6B-GGUF) advertises `Q4_K_M` weights ~0.484 GB. The [upstream Qwen3 project](https://github.com/QwenLM/Qwen3) documents a switch to disable thinking for earlier Qwen3 models; [llama.cpp](https://github.com/ggml-org/llama.cpp/releases) publishes Linux CPU builds.

**Inference:** the model file alone is smaller than available memory. **Not established:** complete runtime residency, time per token, actual task-solving quality, inference token counts, precision loss, security/compliance or trustworthy agent baseline. A 0.6B model may not successfully perform the intended multi-agent reasoning: treat agent capability as a gating question, not an assumed success.

No external model executable or weights have been downloaded. No dependency or network egress permission was changed to force the test.

## Admission decision

```yaml
rec012_llm_execution:
  host: ephemeral_chatgpt_container
  decision: BLOCKED_ENVIRONMENT
  blockers:
    - NO_LOCAL_LLM_WEIGHTS
    - NO_WORKING_MODEL_DOWNLOAD_PATH
    - NO_INSTALLED_SUPPORTED_INFERENCE_RUNNER
  potential_ram_fit: PLAUSIBLE_FILE_ONLY_NOT_RUNTIME_VERIFIED
  model_execution: NOT_RUN
  g7: OPEN
  mk1: IN_PROGRESS
  mk2: BLOCKED
```

This is an **environment-specific NO_GO**, not evidence that local CPU inference is impossible elsewhere. Do not request a paid API or add a runner just to make the gate green.

## Exact retry trigger (not continuous polling)

Re-evaluate **only** when one of these changes:
- user-supplied legal, local model weights + supported local inference runner become available in a permitted workspace;
- a device with a verified working offline inference runner is available for an on-device experiment;
- user explicitly authorizes an alternative model provider, credentials and bounded spending (not assumed).

Do not treat ChatGPT conversation completions as interchangeable controlled benchmark calls: provider/model decoding, token telemetry, system context and repeated independent trials are not reliably pinned by this approach.

## Remaining comparison contract

On a runnable host, preserve [REC-012 spec](../../mk/MK1/MULTI_AGENT_BASELINE_SPEC.md): same held-out tasks, tools, model/revision/config and evaluator; genuine model-decided bounded tool invocation versus manager + two genuine model-based specialists; repeated trials; wall-time, calls, input/output tokens, failures, handoffs, budgets, evidence IDs. Keep deterministic [prior run](./README.md) as a **separate control** only. Negative or inconclusive outcomes remain acceptable.

## Scope closure

Environment feasibility audit **CLOSED: BLOCKED**. Real-model comparison **NOT RUN**. No changes to MK1 schema, REC-012 G7 pass, MK2 gate, model installation, paid quotas or application repositories.
