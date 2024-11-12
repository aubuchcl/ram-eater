import time
import psutil  # Import to monitor memory usage

# Target memory usage in bytes (15 GB)
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

        # Allocate memory only if we haven't reached the target usage
        if current_memory_usage < TARGET_MEMORY_USAGE:
            # Allocate 10 MB of memory in each iteration
            memory_eater.append(" " * 40**7)  # 40 MB allocation
        else:
            # Print confirmation and hold the memory
            print(f"Reached target memory of {TARGET_MEMORY_USAGE / (1024**3):.1f} GB. Holding...")

        # Pause for a moment to slow down allocations
        time.sleep(0.1)
except MemoryError:
    print("Out of memory! Holding at maximum allocated memory.")
