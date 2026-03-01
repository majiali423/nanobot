import subprocess
import time

command = "I need the current NVDA price. Do not read local files. Attempt to get both Nasdaq and Bloomberg data. If any source fails, report the failure, rely on the working source, and calculate the cost of 100 shares."

print("Starting Resilience Benchmark (3 Trials)...")
for i in range(3):
    start_time = time.time()
    process = subprocess.run(["python3", "-m", "nanobot.cli.commands", "agent", "-m", command], capture_output=True, text=True)
    duration = time.time() - start_time
    output = process.stdout
    if "nanobot" in output:
        print(f"Trial {i+1} Output Snippet:\n", output.split("nanobot")[-1][:500])
    print(f"Trial {i+1} Latency: {duration:.2f}s\n{'-'*40}")
