from logging import info
import tkinter as tk
from tkinter import ttk
import main
import psutil
import requests
import pyuac
import platform
import subprocess
import time
test = main.custom()

cpu_name = subprocess.check_output("wmic cpu get caption", shell=True).decode().strip().split("\n")[1]
virtual_memory = psutil.virtual_memory()
response = requests.get('https://api.ipify.org?format=json')
ip_address = response.json().get('ip')
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
        time.sleep(10)
        
    else:
     print("test 1")
     root = tk.Tk()
     root.title("T-weaker")
     root.geometry("400x300")
     

     print("test2")

    # Create a notebook (tabbed interface)
     notebook = ttk.Notebook(root)
     notebook.pack(fill='both', expand=True)

    # System Information Tab
     sys_info_tab = ttk.Frame(notebook)
     notebook.add(sys_info_tab, text=f"System information")
     tk.Label(sys_info_tab, text=f"System Info:{platform.system()}").pack(pady=5)
     tk.Label(sys_info_tab, text=f"Processor: {cpu_name}").pack(pady=5)
     tk.Label(sys_info_tab, text=f"RAM : {virtual_memory.total / (1024 ** 3)} GB").pack(pady=5)
     tk.Label(sys_info_tab, text=f"IP Address : {ip_address}").pack(pady=5)
     print("test3")
    # Performance Tab
     performance_tab = ttk.Frame(notebook)
     notebook.add(performance_tab, text="Performance")
     tk.Button(performance_tab, text="Remove Bloatware", command=test.rbloat).pack(pady=5)
     tk.Button(performance_tab, text="Disable Start Apps", command=test.stapps).pack(pady=5)
     tk.Button(performance_tab, text="Enable Mouse acc", command=test.onmouseacc).pack(pady=5)
     tk.Button(performance_tab, text="Disable Mouse acc", command=test.rmouseacc).pack(pady=5)
     print("test4")
    # Customization Tab
     customization_tab = ttk.Frame(notebook)
     notebook.add(customization_tab, text="Customization")
    
     label = tk.Label(customization_tab, text="Theme:", font=("Arial", 12), justify="left")
     label.pack(anchor="w")
     theme_var = tk.StringVar(value="Dark mode")
     tk.Radiobutton(customization_tab, text="Dark mode", variable=theme_var, value="Dark mode",
                   anchor="w", command=test.changedark).pack(pady=5)
     tk.Radiobutton(customization_tab, text="Light mode", variable=theme_var, value="Light mode",
                   anchor="w", command=test.changelight).pack(pady=5)
     print("test5")
     label = tk.Label(customization_tab, text="Start Button Position:", font=("Arial", 12), justify="left")
     label.pack(anchor="w")
     start_button_var = tk.StringVar(value="Center")
     tk.Radiobutton(customization_tab, text="Start Button Center", variable=start_button_var, value="Center",
                   command=test.changemid).pack(pady=5)
     tk.Radiobutton(customization_tab, text="Start Button Left", variable=start_button_var, value="Left",
                   command=test.changeleft).pack(pady=5)
    
     label = tk.Label(customization_tab, text="Animation:", font=("Arial", 12), justify="left")
     label.pack(anchor="w")
     animation_var = tk.StringVar(value="Enable")
     tk.Radiobutton(customization_tab, text="Enable Animation", variable=animation_var, value="Enable",
                   command=test.enable_animation).pack(pady=5)
     tk.Radiobutton(customization_tab, text="Disable Animation", variable=animation_var, value="Disable",
                   command=test.remove_animation).pack(pady=5)
     print("test6")
    # Backup Tab
     backup_tab = ttk.Frame(notebook)
     notebook.add(backup_tab, text="Backup")
     tk.Button(backup_tab, text="Create Backup",
              command=test.createarestorepoint).pack(pady=5)
     tk.Button(backup_tab, text="Restore Backup", command=test.restorepoint).pack(pady=5)
     print("test7")
     root.mainloop()
