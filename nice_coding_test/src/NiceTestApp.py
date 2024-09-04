import argparse
import platform
import psutil
import socket
import logging
from logger_config import setup_logger


def get_computer_info():
    """
    Retrieves information about the computer including:
    - Computer Name: Fully qualified domain name of the computer.
    - Total Physical Memory: Total physical memory in gigabytes.
    - Total Number of Physical Processors: The number of physical CPU processors.
    - Total Number of Cores: The total number of CPU cores.
    - Total Number of Hard Disks: The number of hard disk drives (excluding removable drives).
    - Top 5 processes in terms of CPU: List of top 5 processes using the most CPU.

    :return: Dictionary containing the computer's information.
    """
    info = {
        "Computer Name": socket.getfqdn(),
        "Total Physical Memory": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} Gb",
        "Total Number of Physical Processors": psutil.cpu_count(logical=False),
        "Total Number of Cores": psutil.cpu_count(logical=True),
        "Total Number of Hard Disks": sum(1 for disk in psutil.disk_partitions() if 'removable' not in disk.opts),
        "Top 5 processes in terms of CPU": get_top_cpu_processes()
    }
    return info


def get_top_cpu_processes():
    """
    Retrieves the top 5 processes in terms of CPU usage at the time of execution.

    :return: Dictionary containing the names and CPU usage percentages of the top 5 processes.
    """
    processes = []
    # Iterate over all running processes and collect their PID, name, and CPU usage.
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        processes.append(proc.info)

    # Sort processes by CPU usage in descending order
    processes.sort(key=lambda proc: proc['cpu_percent'], reverse=True)

    # Select the top 5 processes
    top_processes = processes[:5]

    # Format the output as a dictionary
    return {f"Process{idx + 1}": f"{proc['name']}: {proc['cpu_percent']}%" for idx, proc in enumerate(top_processes)}


def display_info(info):
    """
    Prints the computer information to the console.

    :param info: Dictionary containing the computer's information.
    :return: None
    """
    # Print each key-value pair from the info dictionary
    for key, value in info.items():
        print(f"{key}: {value}")


def log_info(info):
    """
    Logs the computer information to the log file.

    :param info: Dictionary containing the computer's information.
    :return: None
    """
    # Log each key-value pair from the info dictionary
    for key, value in info.items():
        logging.info(f"{key}: {value}")


def main():
    """
    Main function that handles command-line arguments and runs the application.

    - If -logInfo is specified, sets up logging and logs the computer information.
    - If -help is specified, displays a help message.
    - Always displays the computer information to the console.

    :return: None
    """
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Computer Information Application")

    # Define the -logInfo argument
    parser.add_argument("-logInfo", action="store_true", help="Log the computer information to a file")

    # Define the -help argument
    parser.add_argument("-help", action="store_true", help="Display help message and exit")

    # Parse the command-line arguments
    args = parser.parse_args()

    # If -help is specified, display the help message and exit
    if args.help:
        parser.print_help()
        return

    # If -logInfo is specified, set up logging
    if args.logInfo:
        setup_logger()

    # Retrieve computer information
    info = get_computer_info()

    # Display the information on the console
    display_info(info)

    # If -logInfo is specified, log the information
    if args.logInfo:
        log_info(info)


if __name__ == "__main__":
    main()
