# FTEC5660 Reproducibility Work: NanoBot Agentic System

## 1. Project Overview
This repository contains the reproducibility work for the **NanoBot** agentic system. We specifically targeted the agent's **tool-call reliability, conflict resolution, and fault tolerance**.

## 2. Core Modifications
* **Model Swap**: Transitioned the underlying LLM to **DeepSeek-V3**.
* **Prompt Policy Change**: Implemented a strict deterministic prompt (`SOUL.md`) to eliminate data hallucination.
* **Tool Ablation & Mocking**: Modified `nanobot/agent/tools/web.py` to inject controlled dual-source conflicts (Nasdaq vs. Bloomberg) and forced `HTTP 503` timeouts.

## 3. Key Findings
* The system demonstrated excellent **fault resilience**, successfully identifying the 503 error and executing a single-source fallback without crashing.
* Applying the strict prompt policy achieved a **100% success rate** in conflict resolution.
