# FTEC5660 Reproducibility Work: NanoBot Agentic System

## 📌 Reproducibility Focus
This repository contains the isolated modifications and benchmarking scripts used to evaluate the **tool-call reliability and fault tolerance** of the NanoBot agentic framework.

## 📂 Code Map (Where to find my changes)
To facilitate grading and peer review, all core modifications required by the FTEC5660 assignment have been isolated into the following specific files:
## All code in https://github.com/majiali423/nanobot/blob/main/Colabcode%20.ipynb

1. **The Isolated Modification (Mock Injection)**:
   - **File**: [`nanobot/agent/tools/web.py`](nanobot/agent/tools/web.py)
   - **Details**: The web search tools have been mocked to decouple the agent's reasoning from external network volatility. Source A (Nasdaq) is hardcoded to return a static `$184.89`, while Source B (Bloomberg) is forcefully injected with an `HTTP ERROR 503`.

2. **Experiment A: Temperature Ablation (Stochasticity)**:
   - **File**: [`reproducibility_experiments/benchmark_temperature.py`](reproducibility_experiments/benchmark_temperature.py)
   - **Details**: A fully automated script that sweeps through LLM temperature gradients (0.0 to 0.9). It executes 5 trials per gradient to measure execution latency variance and logs the task success rate, automatically generating the matplotlib variance chart.

3. **Experiment B: Fault Resilience (Graceful Degradation)**:
   - **File**: [`reproducibility_experiments/benchmark_resilience.py`](reproducibility_experiments/benchmark_resilience.py)
   - **Details**: Evaluates the agent's ability to achieve true *graceful degradation*. It forces the agent to handle the 503 error dynamically and calculate accurate financial valuations using only the surviving data source without hallucinating.

## 🚀 Execution
To reproduce the benchmarks, install the required dependencies (`matplotlib`, `numpy`) and run the Python scripts directly from the `reproducibility_experiments` folder. Please refer to the submitted PDF report for comprehensive quantitative results and log analysis.
