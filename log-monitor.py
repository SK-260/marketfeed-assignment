#!/usr/bin/env python3


import subprocess
import signal
import re
from collections import Counter

# Function to handle keyboard interrupt (Ctrl+C)
def signal_handler(signal, frame):
    print("\nMonitoring stopped.")
    exit(0)

# Function to monitor log file and perform analysis
def monitor_log(log_file):
    try:
        # Open the log file for reading
        with subprocess.Popen(['tail', '-F', log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) as process:
            # Initialize keyword counter
            keyword_counter = Counter()

            # Continuous monitoring loop
            for line in process.stdout:
                # Display new log entries in real-time
                print(line.strip())

                # Perform basic analysis (count occurrences of specific keywords or patterns)
                keywords = ['error', 'HTTP status']
                for keyword in keywords:
                    if re.search(keyword, line, re.IGNORECASE):
                        keyword_counter[keyword] += 1

                # Generate summary reports
                if keyword_counter:
                    print("\nSummary Report:")
                    for keyword, count in keyword_counter.items():
                        print(f"{keyword}: {count}")

    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)

if __name__ == "__main__":
    # Log file to monitor
    log_file = "output.log"

    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Start monitoring log file
    print(f"Monitoring log file: {log_file}")
    monitor_log(log_file)
