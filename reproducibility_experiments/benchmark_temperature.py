import os
import json
import time
import subprocess
import numpy as np
import matplotlib.pyplot as plt

def modify_temperature_config(temp_value: float) -> None:
    config_path = os.path.expanduser("~/.nanobot/config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    if "agents" not in config: config["agents"] = {}
    if "defaults" not in config["agents"]: config["agents"]["defaults"] = {}
    config["agents"]["defaults"]["temperature"] = temp_value
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)

def run_trials(temp_value: float, trials: int = 5) -> dict:
    modify_temperature_config(temp_value)
    latencies = []
    success_count = 0
    command = "I need the current NVDA price. Do not read local files. Use web_search for Nasdaq data, and web_fetch for Bloomberg data. Compare them, explain your choice, and calculate the cost of 100 shares."
    
    print(f"[Running T={temp_value}] Initiating {trials} trials...")
    for i in range(trials):
        start_time = time.time()
        process = subprocess.run(["python3", "-m", "nanobot.cli.commands", "agent", "-m", command], capture_output=True, text=True)
        duration = time.time() - start_time
        latencies.append(duration)
        if "184.89" in process.stdout and "195.50" in process.stdout:
            success_count += 1
    return {"mean": np.mean(latencies), "std": np.std(latencies), "success_rate": (success_count / trials) * 100 if trials > 0 else 0}

if __name__ == "__main__":
    temperatures = [0.0, 0.3, 0.6, 0.9]
    means, stds, success_rates = [], [], []
    for t in temperatures:
        res = run_trials(t, 5)
        means.append(res["mean"])
        stds.append(res["std"])
        success_rates.append(res["success_rate"])

    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.errorbar(temperatures, means, yerr=stds, fmt='-o', color='tab:blue', capsize=8, label='Mean Latency')
    ax1.set_xlabel('LLM Temperature (Stochasticity)', fontweight='bold')
    ax1.set_ylabel('Execution Latency (s)', color='tab:blue', fontweight='bold')
    ax1.grid(True, linestyle='--')
    plt.title('Agentic Decision Reliability vs. LLM Temperature', fontweight='bold')
    plt.savefig('temperature_ablation_plot.png', dpi=300, bbox_inches='tight')
    print("Plot saved as temperature_ablation_plot.png")
