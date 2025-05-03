import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

CONFIG_FILE = 'config.json'

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {"host": "127.0.0.1", "port": 8080, "ip_to_name": {}}
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

class ConfigEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Config Manager")
        self.config = load_config()

        self.host_label = tk.Label(root, text="HOST:")
        self.host_label.pack()
        self.host_entry = tk.Entry(root)
        self.host_entry.insert(0, self.config.get("host", "127.0.0.1"))
        self.host_entry.pack()

        self.port_label = tk.Label(root, text="PORT:")
        self.port_label.pack()
        self.port_entry = tk.Entry(root)
        self.port_entry.insert(0, str(self.config.get("port", 8080)))
        self.port_entry.pack()

        self.device_listbox = tk.Listbox(root)
        self.device_listbox.pack(fill=tk.BOTH, expand=True)
        self.refresh_device_list()

        self.add_button = tk.Button(root, text="Add Device", command=self.add_device)
        self.add_button.pack()

        self.edit_button = tk.Button(root, text="Edit Device", command=self.edit_device)
        self.edit_button.pack()

        self.delete_button = tk.Button(root, text="Delete Device", command=self.delete_device)
        self.delete_button.pack()

        self.save_button = tk.Button(root, text="Save", command=self.save_all)
        self.save_button.pack()

    def refresh_device_list(self):
        self.device_listbox.delete(0, tk.END)
        for ip, name in self.config["ip_to_name"].items():
            self.device_listbox.insert(tk.END, f"{ip} => {name}")

    def add_device(self):
        ip = simpledialog.askstring("IP Address", "Enter IP address:")
        if not ip:
            return
        name = simpledialog.askstring("Device Name", "Enter device name:")
        if not name:
            return
        self.config["ip_to_name"][ip] = name
        self.refresh_device_list()

    def edit_device(self):
        selection = self.device_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection", "Select a device to edit.")
            return
        selected_text = self.device_listbox.get(selection[0])
        ip, name = selected_text.split(" => ")
        new_ip = simpledialog.askstring("Edit IP", "New IP:", initialvalue=ip)
        new_name = simpledialog.askstring("Edit Name", "New name:", initialvalue=name)
        if new_ip and new_name:
            del self.config["ip_to_name"][ip]
            self.config["ip_to_name"][new_ip] = new_name
            self.refresh_device_list()

    def delete_device(self):
        selection = self.device_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection", "Select a device to delete.")
            return
        selected_text = self.device_listbox.get(selection[0])
        ip, _ = selected_text.split(" => ")
        confirm = messagebox.askyesno("Confirmation", f"Do you really want to delete {ip}?")
        if confirm:
            del self.config["ip_to_name"][ip]
            self.refresh_device_list()

    def save_all(self):
        self.config["host"] = self.host_entry.get()
        try:
            self.config["port"] = int(self.port_entry.get())
        except ValueError:
            messagebox.showerror("Error", "PORT must be a number.")
            return
        save_config(self.config)
        messagebox.showinfo("Saved", "Configuration has been saved.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConfigEditor(root)
    root.mainloop()

