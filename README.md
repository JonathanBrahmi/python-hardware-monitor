# 💻 Python Hardware Monitor

A real-time hardware monitoring application with a modern GUI built with Python and Tkinter. Monitor your system's performance, disk usage, and network information in real-time.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📋 Table of Contents

- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [File Descriptions](#-file-descriptions)
- [Screenshots](#-screenshots)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🖥️ System Information Tab
- **Processor:** Model and core count
- **Operating System:** Name and version
- **RAM:** Total and available memory
- **System Uptime:** How long system has been running
- **Architecture:** System architecture (32-bit/64-bit)

### ⚡ Performance Tab
- **CPU Usage:** Real-time CPU usage percentage
  - Per-core visualization with Unicode bar charts
  - Total average usage
- **Memory Usage:** RAM usage with visual progress bar
- **Swap Usage:** Virtual memory usage
- **Load Average:** System load metrics
- **1-Second Updates:** Auto-refreshes every second

### 💾 Disk & Network Tab
- **Disk Usage:** Storage capacity and available space for each drive
- **Disk Percentage:** Visual representation of disk usage
- **Network Information:** Network adapter details
- **Mount Points:** File system information

### 🎨 Modern GUI Features
- **Tabbed Interface:** Easy navigation between system stats
- **Real-time Updates:** Auto-refreshing information
- **Professional Styling:** Clean, modern appearance
- **Status Bar:** Shows last update time
- **Error Handling:** Graceful handling of permission issues
- **Threading:** Non-blocking UI during updates

---

## 📦 Requirements

### System Requirements
- **OS:** Windows 10 or later
- **Python:** 3.7 or higher
- **RAM:** Minimum 512 MB (1 GB recommended)
- **Disk Space:** ~50 MB

### Python Dependencies
- `psutil==5.9.4` - Cross-platform system and process utilities

---

## 💾 Installation

### Method 1: Using pip (Recommended)

```bash
# Clone the repository
git clone https://github.com/JonathanBrahmi/python-hardware-monitor.git
cd python-hardware-monitor

# Install dependencies
pip install -r requirements.txt
```

### Method 2: Manual Installation

```bash
# Install psutil directly
pip install psutil==5.9.4

# Then download the .py files
```

### Method 3: From Source

1. Download the files:
   - `hardware_monitor_gui.py`
   - `hardware_info.py`
   - `requirements.txt`

2. Place them in a folder

3. Install dependencies:
   ```bash
   pip install psutil
   ```

---

## 🚀 Usage

### Quick Start

```bash
# Navigate to the folder
cd python-hardware-monitor

# Run the application
python hardware_monitor_gui.py
```

The GUI window will open automatically showing your system information.

### Using the Application

1. **Launch:** Run `python hardware_monitor_gui.py`
2. **View Tabs:** Click tabs to switch between:
   - **System:** Basic system information
   - **Performance:** Real-time CPU, memory, and swap usage
   - **Disk/Network:** Storage and network adapter information
3. **Auto-Refresh:** Information updates automatically every 1 second
4. **Status Bar:** Shows the last update timestamp
5. **Exit:** Close the window or click X button

---

## 📂 Project Structure

```
python-hardware-monitor/
├── hardware_monitor_gui.py      # Main GUI application (Tkinter)
├── hardware_info.py             # System information library
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── LICENSE                      # MIT License
```

---

## 📝 File Descriptions

### `hardware_monitor_gui.py` (Main Application)
**Purpose:** Tkinter-based GUI for monitoring hardware

**Key Components:**
- `HardwareMonitorApp` class - Main application window
- Tabbed interface with 3 tabs (System, Performance, Disk/Network)
- Background threading for real-time updates
- Auto-refresh every 1 second
- Status bar showing last update time

**Features:**
- Multi-threaded to prevent UI freezing
- Error handling for permission issues
- Professional styling with colors
- Unicode progress bars
- Per-core CPU visualization

**Methods:**
- `update_system_info()` - Updates system tab
- `update_performance_info()` - Updates performance tab
- `update_disk_info()` - Updates disk/network tab
- `schedule_next_update()` - Handles auto-refresh

### `hardware_info.py` (Library)
**Purpose:** Collect and format hardware information

**Key Functions:**
- `get_hardware_info()` - Retrieves complete system information
- `get_cpu_info()` - CPU details and usage
- `get_memory_info()` - RAM and swap information
- `get_disk_info()` - Storage device information
- `get_network_info()` - Network adapter information

**Return Values:** Dictionary format with formatted strings

---

## 📸 Screenshots

### System Tab
```
┌─────────────────────────────────────────┐
│ Processor:        Intel Core i7 (8 cores)|
│ Operating System: Windows 10 Pro         |
│ Total RAM:        16.0 GB                |
│ Available RAM:    8.5 GB                 |
│ System Uptime:    45 days, 23:15:30     |
│ Architecture:     64-bit (x86_64)        |
└─────────────────────────────────────────┘
```

### Performance Tab
```
┌─────────────────────────────────────────┐
│ CPU Usage:  ███████░░░░░░░░  65.4%      |
│ Memory:     █████████░░░░░░  53.1%      |
│ Swap:       ██░░░░░░░░░░░░░   8.2%      |
│ Per-Core:                                |
│   Core 0: ███████░░░ 72%                |
│   Core 1: █████░░░░░ 45%                |
│   Core 2: ████████░░ 78%                |
│   Core 3: ██░░░░░░░░ 18%                |
└─────────────────────────────────────────┘
```

### Disk & Network Tab
```
┌─────────────────────────────────────────┐
│ Drive C:\  ██████████░░░░░░  67.2%      |
│ Drive D:\  ████░░░░░░░░░░░░  32.1%      |
│ Network:                                 |
│   Adapter: Ethernet (192.168.1.100)    |
│   Bytes Sent: 1.2 GB                    |
│   Bytes Recv: 3.4 GB                    |
└─────────────────────────────────────────┘
```

---

## 🔧 Technical Details

### Technologies Used
- **GUI Framework:** Tkinter (built-in with Python)
- **System Monitoring:** psutil library
- **Threading:** Python's threading module
- **Data Format:** Dictionary/JSON-compatible structures

### Performance
- **Update Frequency:** 1 second (configurable)
- **CPU Usage:** ~2-5% when idle
- **Memory Usage:** ~30-50 MB
- **Startup Time:** <1 second

### Compatibility
- ✅ Windows 10
- ✅ Windows 11
- ⚠️ macOS (with modifications)
- ⚠️ Linux (with modifications)

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'psutil'"
**Solution:** Install psutil
```bash
pip install psutil==5.9.4
```

### Issue: Permission Denied Error on Disk Information
**Solution:** Run as Administrator or ignore the error (it's handled gracefully)
```bash
# Right-click Command Prompt → Run as Administrator
# Then run: python hardware_monitor_gui.py
```

### Issue: GUI doesn't respond / freezes
**Solution:** This shouldn't happen due to threading, but if it does:
- Close and reopen the application
- Check that psutil is properly installed

### Issue: CPU usage per core not showing
**Solution:** Some systems may have CPU core info disabled. The application will show total usage instead.

### Issue: Low memory available
**Solution:** Close other applications. The monitor itself uses ~50MB.

### Issue: Network information not displaying
**Solution:** Network adapters might be unavailable. This is handled gracefully.

---

## 📊 What the Application Monitors

### CPU Metrics
- ✅ Overall CPU percentage
- ✅ Per-core CPU usage
- ✅ Number of cores
- ✅ CPU frequency
- ✅ System load average

### Memory Metrics
- ✅ Total RAM
- ✅ Used RAM
- ✅ Available RAM
- ✅ Memory percentage
- ✅ Swap usage (virtual memory)

### Disk Metrics
- ✅ Drive letters/mount points
- ✅ Total capacity
- ✅ Used space
- ✅ Free space
- ✅ Usage percentage

### System Metrics
- ✅ Processor model
- ✅ Operating system
- ✅ System uptime
- ✅ Architecture (32/64-bit)
- ✅ Boot time

### Network Metrics
- ✅ Network adapters
- ✅ IP addresses
- ✅ MAC addresses
- ✅ Bytes sent/received
- ✅ Connection status

---

## 🚀 Advanced Usage

### Customizing Update Frequency

Edit `hardware_monitor_gui.py`, find:
```python
UPDATE_INTERVAL = 1000  # milliseconds (1 second)
```

Change to desired interval:
```python
UPDATE_INTERVAL = 2000  # 2 seconds
UPDATE_INTERVAL = 500   # 0.5 seconds
```

### Running as a Service

Create a scheduled task in Windows:
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger: At startup
4. Set action: Run `python hardware_monitor_gui.py`
5. Check "Run with highest privileges"

### Integrating with Other Projects

You can import and use the library:

```python
from hardware_info import get_hardware_info, get_cpu_info

# Get complete hardware info
info = get_hardware_info()
print(f"CPU: {info['processor']}")
print(f"RAM: {info['total_ram']}")

# Get specific CPU info
cpu = get_cpu_info()
print(f"CPU Usage: {cpu['cpu_percent']}%")
```

---

## 📈 Performance Impact

The application has minimal system impact:

| Metric | Value |
|--------|-------|
| CPU Usage (Idle) | ~2-5% |
| Memory Usage | ~30-50 MB |
| Startup Time | <1 second |
| Update Time | ~100-200 ms |
| Disk I/O | Minimal |

---

## 🔐 Security & Privacy

- ✅ No data collection
- ✅ No network communication (local only)
- ✅ No tracking
- ✅ Open source (you can audit the code)
- ✅ Runs locally on your machine

---

## 🤝 Contributing

### How to Contribute

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -am "Add feature"`
6. Push: `git push origin feature-name`
7. Open a Pull Request

### Ideas for Improvements

- [ ] Add GPU monitoring
- [ ] Add temperature monitoring
- [ ] Add process management
- [ ] Add alerts/notifications
- [ ] Add data export (CSV/JSON)
- [ ] Add dark/light theme toggle
- [ ] Add macOS support
- [ ] Add Linux support

---

## 📄 License

This project is licensed under the **MIT License** - see LICENSE file for details.

```
MIT License

Copyright (c) 2026 Jonathan Brahmi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👤 Author

**Jonathan Brahmi**
- GitHub: [@JonathanBrahmi](https://github.com/JonathanBrahmi)
- Project: [python-hardware-monitor](https://github.com/JonathanBrahmi/python-hardware-monitor)

---

## 🆘 Support

### Getting Help

1. **Check Troubleshooting Section** - Most common issues are covered above
2. **Check GitHub Issues** - See if someone reported the same issue
3. **Create an Issue** - Describe the problem clearly with:
   - Your Windows version
   - Python version (run `python --version`)
   - Error message
   - Steps to reproduce

### Resources

- **Python Documentation:** https://docs.python.org/
- **psutil Documentation:** https://psutil.readthedocs.io/
- **Tkinter Guide:** https://docs.python.org/3/library/tkinter.html
- **Windows Performance Monitoring:** https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/

---

## 🎯 Roadmap

### Version 1.0 (Current)
- ✅ System information display
- ✅ Real-time performance monitoring
- ✅ Disk usage tracking
- ✅ Network information

### Version 1.1 (Planned)
- 🔲 Temperature monitoring
- 🔲 Data export functionality
- 🔲 Custom refresh rates
- 🔲 Theme customization

### Version 2.0 (Future)
- 🔲 Web-based dashboard
- 🔲 Historical data tracking
- 🔲 Alerts and notifications
- 🔲 Multi-system monitoring

---

## 📚 Related Projects

Check out these related projects:

- **[python-error-checker](https://github.com/JonathanBrahmi/python-error-checker)** - Python code analyzer with GUI
- **[python-analyzer-react](https://github.com/JonathanBrahmi/python-analyzer-react)** - Full-stack code analyzer

---

## ⭐ If You Like This Project

- ⭐ Star this repository
- 🍴 Fork it for your own use
- 📢 Share it with others
- 🐛 Report bugs
- 💡 Suggest improvements

---

## 📞 Contact & Feedback

Have suggestions? Found a bug? Want to collaborate?

- **Open an Issue:** https://github.com/JonathanBrahmi/python-hardware-monitor/issues
- **Start a Discussion:** https://github.com/JonathanBrahmi/python-hardware-monitor/discussions
- **Email:** [your-email@example.com]

---

## 📝 Changelog

### Version 1.0 - Initial Release
- ✅ Complete hardware monitoring
- ✅ Real-time performance tracking
- ✅ Disk and network information
- ✅ Professional GUI with Tkinter
- ✅ Error handling and threading

---

## 🏆 Best Practices Demonstrated

This project demonstrates:
- ✅ Object-oriented programming (OOP)
- ✅ GUI development with Tkinter
- ✅ Multi-threading for responsiveness
- ✅ Error handling and logging
- ✅ Code organization and structure
- ✅ Documentation best practices
- ✅ Cross-platform compatibility considerations

---

**Made with ❤️ by Jonathan Brahmi**

---

*Last Updated: February 2026*
*Python 3.7+ | Windows 10+ | MIT License*
