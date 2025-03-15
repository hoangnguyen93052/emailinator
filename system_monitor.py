import os
import psutil
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')

def get_cpu_usage():
    """Returns the current CPU usage as a percentage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Returns the current memory usage as a percentage."""
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    """Returns the current disk usage as a percentage."""
    disk = psutil.disk_usage('/')
    return disk.percent

def log_system_usage():
    """Logs the CPU, memory, and disk usages to a log file."""
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    
    logging.info(f'CPU Usage: {cpu_usage}%')
    logging.info(f'Memory Usage: {memory_usage}%')
    logging.info(f'Disk Usage: {disk_usage}%')

def monitor_system(interval):
    """Monitors system usage at a specified interval."""
    try:
        while True:
            log_system_usage()
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")

def main():
    """Main function to run the system monitor."""
    logging.info("System monitor started.")
    monitor_interval = 5  # seconds
    monitor_system(monitor_interval)

if __name__ == "__main__":
    main()

# Additional functions for system health check
def get_network_usage():
    """Returns the current network usage."""
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def log_network_usage():
    """Logs network usage information."""
    bytes_sent, bytes_recv = get_network_usage()
    logging.info(f'Bytes Sent: {bytes_sent}, Bytes Received: {bytes_recv}')

def monitor_network(interval):
    """Monitors network usage at a specified interval."""
    try:
        while True:
            log_network_usage()
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Network monitoring stopped by user.")

# Function for generating a report
def generate_report():
    """Generates a usage report and prints it to the console."""
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    bytes_sent, bytes_recv = get_network_usage()

    report = f"""
    System Monitoring Report
    ------------------------
    CPU Usage: {cpu_usage}%
    Memory Usage: {memory_usage}%
    Disk Usage: {disk_usage}%
    Bytes Sent: {bytes_sent}
    Bytes Received: {bytes_recv}
    """
    print(report)

# Scheduler for periodic reporting
def schedule_report(interval):
    """Schedules periodic reports on system usage."""
    try:
        while True:
            generate_report()
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Scheduled reporting stopped by user.")

def main_menu():
    """Displays the main menu for user interaction."""
    print("System Monitor Menu:")
    print("1. Start monitoring")
    print("2. Start network monitoring")
    print("3. Generate report")
    print("4. Exit")

def run_monitor():
    """Runs the monitor based on user choice."""
    while True:
        main_menu()
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            print("Starting system monitoring...")
            monitor_system(5)
        elif choice == '2':
            print("Starting network monitoring...")
            monitor_network(5)
        elif choice == '3':
            print("Generating report...")
            generate_report()
        elif choice == '4':
            print("Exiting the system monitor.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    run_monitor()
    
class SystemMonitor:
    """Class to encapsulate system monitoring functionality."""
    
    def __init__(self, interval=5):
        self.interval = interval
    
    def start_monitoring(self):
        """Starts monitoring the system."""
        logging.info("Starting system monitoring.")
        try:
            while True:
                log_system_usage()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logging.info("System monitoring stopped.")

    def start_network_monitoring(self):
        """Starts monitoring network usage."""
        logging.info("Starting network monitoring.")
        try:
            while True:
                log_network_usage()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logging.info("Network monitoring stopped.")
    
    def generate_report(self):
        """Generates and displays a report of system usage."""
        report = generate_report()
        logging.info("Report generated and displayed.")
    
if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.start_monitoring()