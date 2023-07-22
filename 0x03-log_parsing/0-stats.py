#!/usr/bin/python3

import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_counter = 0

def print_statistics():
    global total_file_size, status_code_counts
    print("File size:", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")

# Define a signal handler for CTRL + C
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Set the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Process input from stdin line by line
for line in sys.stdin:
    line_counter += 1
    try:
        # Parse the line using the input format
        ip_address, _, _, _, _, status_code, file_size = line.split()[0:7]
        status_code = int(status_code)
        file_size = int(file_size)

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1

        # Print statistics after every 10 lines
        if line_counter % 10 == 0:
            print_statistics()

    except ValueError:
        # If the line doesn't match the expected format, skip it
        continue
