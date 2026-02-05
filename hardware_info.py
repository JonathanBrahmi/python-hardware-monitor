import platform
import socket
import psutil
from datetime import datetime

def get_hardware_info():
    """Returns detailed hardware information for Windows 10 or later"""
    
    info = {}
    
    # System Information
    info['Computer Name'] = socket.gethostname()
    info['OS'] = platform.system()
    info['OS Version'] = platform.release()
    info['OS Build'] = platform.version()
    
    # Processor Information
    info['Processor'] = platform.processor()
    info['CPU Cores'] = psutil.cpu_count(logical=False)
    info['CPU Logical Cores'] = psutil.cpu_count(logical=True)
    info['CPU Usage (%)'] = psutil.cpu_percent(interval=1)
    
    # Memory Information
    memory = psutil.virtual_memory()
    info['Total Memory (GB)'] = round(memory.total / (1024**3), 2)
    info['Available Memory (GB)'] = round(memory.available / (1024**3), 2)
    info['Memory Used (GB)'] = round(memory.used / (1024**3), 2)
    info['Memory Usage (%)'] = memory.percent
    
    # Disk Information
    try:
        disk = psutil.disk_usage('C:\\')  # Windows C: drive
    except:
        disk = psutil.disk_usage('/')  # Fallback for other systems
    info['Total Disk (GB)'] = round(disk.total / (1024**3), 2)
    info['Used Disk (GB)'] = round(disk.used / (1024**3), 2)
    info['Free Disk (GB)'] = round(disk.free / (1024**3), 2)
    info['Disk Usage (%)'] = disk.percent
    
    # Boot Time
    try:
        boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
        info['Last Boot'] = boot_time
    except Exception as e:
        info['Last Boot'] = f"Error: {str(e)}"
    
    return info

if __name__ == "__main__":
    hardware_info = get_hardware_info()
    
    print("=" * 50)
    print("HARDWARE INFORMATION")
    print("=" * 50)
    
    for key, value in hardware_info.items():
        print(f"{key}: {value}")
    
    print("=" * 50)
