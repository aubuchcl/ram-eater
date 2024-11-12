import time

# List to hold large memory allocations
memory_eater = []

print("Starting to eat RAM...")

try:
    while True:
        # Allocate 10MB of memory in each loop iteration
        memory_eater.append(" " * 10**7)
        time.sleep(0.1)  # Sleep to let memory usage accumulate
except MemoryError:
    print("Out of memory! Halting.")

