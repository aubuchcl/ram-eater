import time
import psutil  # Import to monitor memory usage
import os

# Get the target memory usage from an environment variable, default to 15 GB if not set
TARGET_MEMORY_GB = float(os.getenv("TARGET_MEMORY_GB", 15))
TARGET_MEMORY_USAGE = TARGET_MEMORY_GB * (1024**3)  # Convert GB to bytes

# List to hold memory allocations
memory_eater = []

print("Starting to eat RAM...")

try:
    while True:
        # Check the current memory usage of the process
        process = psutil.Process()
        current_memory_usage = process.memory_info().rss
        print(f"Current memory usage: {current_memory_usage} bytes")
        print(f"Target memory: {TARGET_MEMORY_USAGE} bytes")

        # Allocate memory only if we haven't reached the target usage
        if current_memory_usage < TARGET_MEMORY_USAGE:
            # Adjust allocation size to stay close to the target without large jumps
            allocation_size = min(10**7, TARGET_MEMORY_USAGE - current_memory_usage)
            memory_eater.append(" " * allocation_size)  # Dynamically allocate memory
        else:
            # Print confirmation and hold the memory
            print(f"Reached target memory of {TARGET_MEMORY_USAGE / (1024**3):.1f} GB. Holding...")
            time.sleep(10)  # Sleep to avoid further allocations but keep the process alive

        # Small sleep to control the rate of allocation
        time.sleep(0.1)
except MemoryError:
    print("Out of memory! Holding at maximum allocated memory.")
