
# Project Title

A brief description of what this project does and who it's for

# Computer Information Application

## Overview

This Python application, `NiceTestApp.py`, provides detailed information about your computer, including its name, physical memory, CPU details, hard disk count, and the top 5 processes in terms of CPU usage. The application can display this information on the command line and, optionally, log it to a file.

The application is designed to be OS-agnostic, running on both Windows and Linux platforms. It leverages external libraries like `psutil` for gathering system information.

## Features

- **Computer Name**: Displays the fully qualified domain name (FQDN) of the computer.
- **Total Physical Memory**: Shows the total physical memory installed on the machine in gigabytes.
- **Total Number of Physical Processors**: Lists the number of physical CPUs installed.
- **Total Number of Cores**: Lists the total number of cores available.
- **Total Number of Hard Disks**: Lists the number of hard disks (excluding removable drives).
- **Top 5 Processes**: Lists the top 5 CPU-consuming processes.

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```



### 2. Set Up a Virtual Environment

### Windows

1. Create a Virtual Environment:

```bash
python -m venv venv
```
2. Activate the Virtual Environment:

```bash
.\venv\Scripts\activate
```

### Linux/MacOS

1. Create a Virtual Environment:

```bash
python3 -m venv venv
```
2. Activate the Virtual Environment:

```bash
source venv/bin/activate
```
### 3. Install Dependencies
Make sure your virtual environment is activated, then install the required dependencies:
```bash
pip install -r requirements.txt
```
This ensures that the necessary libraries are installed in your virtual environment.

## Usage
### Command-Line Arguments
The application accepts the following arguments:

- -logInfo: Logs the computer information to a file.
- -help: Displays the help message and exits.

### Example Commands

1. Display Information on Console:

```bash
python NiceTestApp.py
```

2. Display Information on Console and Log to File:

```bash
python NiceTestApp.py -logInfo

```

3. Display Help Message:

```bash
python NiceTestApp.py -help
```

### Log File
If the -logInfo flag is specified, the application logs the computer information to a file, located in the logs directory. The log files are organized by date within this directory.

### Log Structure
- Log Directory: logs/test_<mm_dd_yyyy>
- Log File: <mm_dd_yyyy>.log

Each log entry includes the timestamp, line number, logger name, log level, and the message.

### Example Output
Console Output:

```bash
Computer Name: LAPTOP-P41I43PL
Total Physical Memory: 7.77 Gb
Total Number of Physical Processors: 4
Total Number of Cores: 8
Total Number of Hard Disks: 2
Top 5 processes in terms of CPU: {'Process1': 'System Idle Process: 0.0%', 'Process2': 'System: 0.0%', 'Process3': ': 0.0%', 'Process4': 'Registry: 0.0%',
'Process5': 'csrss.exe: 0.0%'}


```

### Log File Entry:

```
[08/09/2024 10:00:00] 45 root - INFO - Computer Name: MyLaptop
[08/09/2024 10:00:00] 46 root - INFO - Total Physical Memory: 8.00 Gb
[08/09/2024 10:00:00] 47 root - INFO - Total Number of Physical Processors: 2
```

### Customization
You can modify the code to suit your needs, such as changing the log directory structure, the log format, or the system information displayed.

### Adding More Information
To add more details about your system, modify the get_computer_info() function in NiceTestApp.py. Use the psutil library to retrieve additional system information.

### Changing the Log Format
To modify the log format, edit the setup_logger() function in the logger_config.py file.