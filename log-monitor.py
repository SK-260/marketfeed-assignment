import logging
import time
import os
from collections import Counter

# Configuring Logging
logging.basicConfig(level=logging.DEBUG, filename="server.log", format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
# Creating a logger
logger = logging.getLogger(__name__)

# Creating a counter to count the keywords
keyword_counter = Counter()


def log_monitoring(file_path):
    try:
        with open(file_path, "r") as file:  # Opening the Log File
            file.seek(0, 2)  # Moving to End of file
            while True:
                line = file.readline()  # Read new logs
                if line:
                    print(line)  # Print the log
                    analyze_new_line(line)  # Analyse the log
                else:
                    time.sleep(1)  # Sleep if no new log entered

    # To exit the script
    except KeyboardInterrupt:  # On pressing Ctrl+C
        print("Report Summary")
        for keyword, count in keyword_counter.items():
            print(f"{keyword}: {count}")  # Print the keyword counts
        print("\n Logging has been Interrupted. Exiting.")


# Analysing each new log entered
def analyze_new_line(new_line):
    if "error" in new_line.lower():
        logger.error(new_line)  # IF error is there log it as an Error
        keyword_counter["error"] += 1
    elif "debug" in new_line.lower() or "warning" in new_line.lower():
        logger.debug(new_line)  # if warning is there log it as debug
        keyword_counter["warning"] += 1
    else:
        logger.info(new_line)  # every other log is logged as info


# main program
if __name__ == "__main__":
    # Ask user to enter the file path
    file_path = input("Enter the path of file: ")

    # Check for file existence
    if not os.path.exists(file_path):
        print(f"The path {file_path} does not exist.")
        exit()
    # Call the log monitoring
    log_monitoring(file_path)
