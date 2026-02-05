import tkinter as tk
from tkinter import ttk
import psutil
import platform
import socket
from datetime import datetime
import threading

class HardwareMonitorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hardware Monitor - Real-time System Monitoring")
        self.root.geometry("900x800")
        self.root.resizable(True, True)
        
        # Configure style
        self.setup_styles()
        
        # Data storage
        self.update_interval = 1000
        self.monitoring = True
        
        # Main container
        main_container = ttk.Frame(root)
        main_container.pack(side="top", fill="both", expand=True)
        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(main_container)
        self.notebook.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # System Tab
        self.system_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.system_frame, text="System Info")
        self.create_system_tab()
        
        # Performance Tab
        self.perf_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.perf_frame, text="Performance")
        self.create_performance_tab()
        
        # Disk Tab
        self.disk_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.disk_frame, text="Disk & Network")
        self.create_disk_tab()
        
        # Bottom status bar
        self.status_var = tk.StringVar()
        status_bar = ttk.Label(root, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side="bottom", fill="x", padx=5, pady=5)
        
        # Start update loop
        self.schedule_update()
    
    def setup_styles(self):
        """Configure visual styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('Title.TLabel', font=("Arial", 14, "bold"))
        style.configure('Header.TLabel', font=("Arial", 11, "bold"))
        style.configure('Info.TLabel', font=("Courier", 9))
    
    def create_system_tab(self):
        """Create system information tab"""
        # System info text area
        text_frame = ttk.Frame(self.system_frame)
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.system_text = tk.Text(text_frame, height=35, width=100,
                                  font=("Courier", 9), bg="#f5f5f5",
                                  yscrollcommand=scrollbar.set)
        self.system_text.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar.config(command=self.system_text.yview)
    
    def create_performance_tab(self):
        """Create performance monitoring tab"""
        # CPU Section
        cpu_frame = ttk.LabelFrame(self.perf_frame, text="CPU Performance", padding=10)
        cpu_frame.pack(fill="x", padx=5, pady=5)
        
        self.cpu_label = ttk.Label(cpu_frame, text="CPU Usage: 0%", 
                                  style="Header.TLabel")
        self.cpu_label.pack(anchor="w", pady=5)
        
        self.cpu_progress = ttk.Progressbar(cpu_frame, length=400, mode='determinate')
        self.cpu_progress.pack(fill="x", pady=5)
        
        self.cpu_detail_label = ttk.Label(cpu_frame, text="")
        self.cpu_detail_label.pack(anchor="w")
        
        # Memory Section
        mem_frame = ttk.LabelFrame(self.perf_frame, text="Memory", padding=10)
        mem_frame.pack(fill="x", padx=5, pady=5)
        
        self.mem_label = ttk.Label(mem_frame, text="Memory Usage: 0%", 
                                  style="Header.TLabel")
        self.mem_label.pack(anchor="w", pady=5)
        
        self.mem_progress = ttk.Progressbar(mem_frame, length=400, mode='determinate')
        self.mem_progress.pack(fill="x", pady=5)
        
        self.mem_detail_label = ttk.Label(mem_frame, text="")
        self.mem_detail_label.pack(anchor="w")
        
        # Swap Section
        swap_frame = ttk.LabelFrame(self.perf_frame, text="Swap Memory", padding=10)
        swap_frame.pack(fill="x", padx=5, pady=5)
        
        self.swap_label = ttk.Label(swap_frame, text="Swap Usage: 0%", 
                                   style="Header.TLabel")
        self.swap_label.pack(anchor="w", pady=5)
        
        self.swap_progress = ttk.Progressbar(swap_frame, length=400, mode='determinate')
        self.swap_progress.pack(fill="x", pady=5)
        
        self.swap_detail_label = ttk.Label(swap_frame, text="")
        self.swap_detail_label.pack(anchor="w")
        
        # Per-core info
        core_frame = ttk.LabelFrame(self.perf_frame, text="Per-Core Usage", padding=10)
        core_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        scrollbar = ttk.Scrollbar(core_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.core_text = tk.Text(core_frame, height=8, font=("Courier", 9),
                                bg="#f5f5f5", yscrollcommand=scrollbar.set)
        self.core_text.pack(fill="both", expand=True)
        scrollbar.config(command=self.core_text.yview)
    
    def create_disk_tab(self):
        """Create disk and network tab"""
        scrollbar = ttk.Scrollbar(self.disk_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.disk_text = tk.Text(self.disk_frame, font=("Courier", 9),
                                bg="#f5f5f5", yscrollcommand=scrollbar.set)
        self.disk_text.pack(fill="both", expand=True, padx=5, pady=5)
        scrollbar.config(command=self.disk_text.yview)
    
    def schedule_update(self):
        """Schedule the next update"""
        if self.monitoring:
            # Run update in separate thread to prevent UI freezing
            thread = threading.Thread(target=self.update_all_info, daemon=True)
            thread.start()
            self.root.after(self.update_interval, self.schedule_update)
    
    def update_all_info(self):
        """Update all information"""
        try:
            # Update system tab
            system_info = self.get_system_info()
            self.system_text.config(state=tk.NORMAL)
            self.system_text.delete(1.0, tk.END)
            self.system_text.insert(tk.END, system_info)
            self.system_text.config(state=tk.DISABLED)
            
            # Update performance tab
            self.update_performance_tab()
            
            # Update disk tab
            disk_info = self.get_disk_info()
            self.disk_text.config(state=tk.NORMAL)
            self.disk_text.delete(1.0, tk.END)
            self.disk_text.insert(tk.END, disk_info)
            self.disk_text.config(state=tk.DISABLED)
            
            # Update status bar
            self.status_var.set(f"Last Updated: {datetime.now().strftime('%H:%M:%S')}")
            
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
    
    def update_performance_tab(self):
        """Update performance metrics"""
        try:
            # CPU
            cpu_usage = psutil.cpu_percent(interval=0.5)
            self.cpu_progress['value'] = cpu_usage
            self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
            
            cpu_freq = psutil.cpu_freq()
            freq_text = f"Cores: {psutil.cpu_count(logical=False)} | Frequency: {cpu_freq.current:.0f}/{cpu_freq.max:.0f} MHz" if cpu_freq else ""
            self.cpu_detail_label.config(text=freq_text)
            
            # Memory
            memory = psutil.virtual_memory()
            self.mem_progress['value'] = memory.percent
            self.mem_label.config(text=f"Memory Usage: {memory.percent}%")
            mem_text = f"Used: {memory.used / (1024**3):.1f} GB / {memory.total / (1024**3):.1f} GB"
            self.mem_detail_label.config(text=mem_text)
            
            # Swap
            swap = psutil.swap_memory()
            self.swap_progress['value'] = swap.percent
            self.swap_label.config(text=f"Swap Usage: {swap.percent}%")
            swap_text = f"Used: {swap.used / (1024**3):.1f} GB / {swap.total / (1024**3):.1f} GB"
            self.swap_detail_label.config(text=swap_text)
            
            # Per-core
            per_cpu = psutil.cpu_percent(interval=0.1, percpu=True)
            self.core_text.config(state=tk.NORMAL)
            self.core_text.delete(1.0, tk.END)
            core_info = "Per-Core CPU Usage:\n" + "-" * 40 + "\n"
            for i, usage in enumerate(per_cpu):
                bar_length = int(usage / 5)
                bar = "█" * bar_length + "░" * (20 - bar_length)
                core_info += f"Core {i:2d}: {bar} {usage:5.1f}%\n"
            self.core_text.insert(tk.END, core_info)
            self.core_text.config(state=tk.DISABLED)
        except Exception as e:
            self.status_var.set(f"Error updating performance: {str(e)}")
    
    def get_system_info(self):
        """Get system information"""
        try:
            info = ""
            info += f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            info += "=" * 70 + "\n\n"
            
            # System Information
            info += "SYSTEM INFORMATION\n"
            info += "-" * 70 + "\n"
            info += f"Computer Name: {socket.gethostname()}\n"
            info += f"Operating System: {platform.system()} {platform.release()}\n"
            info += f"OS Version: {platform.version()}\n"
            info += f"Processor: {platform.processor()}\n"
            info += f"Architecture: {platform.architecture()[0]}\n"
            info += "\n"
            
            # CPU Information
            info += "CPU INFORMATION\n"
            info += "-" * 70 + "\n"
            cpu_cores = psutil.cpu_count(logical=False)
            cpu_logical = psutil.cpu_count(logical=True)
            cpu_freq = psutil.cpu_freq()
            
            info += f"Physical Cores: {cpu_cores}\n"
            info += f"Logical Cores: {cpu_logical}\n"
            
            if cpu_freq:
                info += f"Current Frequency: {cpu_freq.current:.2f} MHz\n"
                info += f"Min Frequency: {cpu_freq.min:.2f} MHz\n"
                info += f"Max Frequency: {cpu_freq.max:.2f} MHz\n"
            
            # Load average
            try:
                load_avg = psutil.getloadavg()
                info += f"Load Average: {load_avg[0]:.2f}, {load_avg[1]:.2f}, {load_avg[2]:.2f}\n"
            except AttributeError:
                info += "Load Average: N/A (Windows)\n"
            
            info += "\n"
            return info
        except Exception as e:
            return f"Error gathering system info: {str(e)}"
    
    def get_disk_info(self):
        """Get disk and network information"""
        try:
            info = ""
            info += f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            info += "=" * 70 + "\n\n"
            
            # Disk Information
            info += "DISK INFORMATION\n"
            info += "-" * 70 + "\n"
            
            try:
                for partition in psutil.disk_partitions():
                    if partition.fstype:
                        try:
                            usage = psutil.disk_usage(partition.mountpoint)
                            info += f"\nDrive: {partition.device}\n"
                            info += f"  Mount Point: {partition.mountpoint}\n"
                            info += f"  File System: {partition.fstype}\n"
                            info += f"  Total: {usage.total / (1024**3):.2f} GB\n"
                            info += f"  Used: {usage.used / (1024**3):.2f} GB\n"
                            info += f"  Free: {usage.free / (1024**3):.2f} GB\n"
                            info += f"  Usage: {usage.percent}%\n"
                        except PermissionError:
                            pass
            except Exception as e:
                info += f"Error reading disk info: {str(e)}\n"
            
            info += "\n"
            
            # Network Information
            info += "NETWORK INFORMATION\n"
            info += "-" * 70 + "\n"
            
            try:
                net_if_addrs = psutil.net_if_addrs()
                for interface_name, addrs in net_if_addrs.items():
                    info += f"\n{interface_name}:\n"
                    for addr in addrs:
                        info += f"  {addr.family.name}: {addr.address}\n"
            except Exception as e:
                info += f"Error reading network info: {str(e)}\n"
            
            return info
        except Exception as e:
            return f"Error gathering disk info: {str(e)}"


if __name__ == "__main__":
    root = tk.Tk()
    app = HardwareMonitorGUI(root)
    root.mainloop()

