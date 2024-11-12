import time
import psutil  # We will use psutil to monitor memory usage

# Define the memory target in bytes (15.5 GB)
TARGET_MEMORY_USAGE = 15.5 * (1024**3)  # Convert GB to bytes

# List to hold large memory allocations
memory_eater = []

print("Starting to eat RAM...")

try:
    while True:
        # Allocate 10MB of memory in each loop iteration
        memory_eater.append(" " * 10**7)  # 10 MB allocation
        # Check the current memory usage of the process
        process = psutil.Process()
        current_memory_usage = process.memory_info().rss

        # Stop once we reach the target memory usage
        if current_memory_usage >= TARGET_MEMORY_USAGE:
            print(f"Target memory of {TARGET_MEMORY_USAGE / (1024**3):.1f} GB reached. Halting.")
            break

        # Small sleep to accumulate memory consumption at a steady rate
        time.sleep(0.1)
except MemoryError:
    print("Out of memory! Halting.")
