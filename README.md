

# 🌐 Python HTTP Server with Custom Logging


This project is a simple Python HTTP server that serves files over the network and **logs the access of each device in a clear format**:

* ✅ Detects client IP
* ✅ Assigns a name based on `config.json`
* ✅ Logs: time, name, IP, requested file, HTTP code
* ✅ Does not use the old log format (clean output!)
* ✅ **Device configuration and logging** is managed through the **Config Editor** (a graphical user interface for editing configurations)

---

## 📁 Project Structure

```
project/
├── server.py          # main server script
├── config.json        # configuration for IP addresses and port
├── server_log.txt     # automatically generated detailed log
├── config_editor.py   # script to edit config.json via UI
├── README.md          # this guide
└── (your files)       # HTML/CSS/JS served by the server
```

---

## ⚙️ Configuration

### `config.json`

```json
{
  "host": "192.168.1.49",
  "port": 8080,
  "ip_to_name": {
    "xxx.xxx.1.171": "mobile",
    "xxx.xxx.1.49": "pc"
  }
}
```

* `host`: IP address on which the server runs
* `port`: port (e.g., 8080)
* `ip_to_name`: mapping IP to device names

---

## 🛠️ **Config Editor** - Configuration Editing

For convenient editing of IP addresses and device configurations, the project includes a simple **Config Editor** (`config_editor.py`). This script provides a graphical interface that allows you to:

* Add, edit, or remove devices and their associated IP addresses.
* View the current configuration of devices assigned to IP addresses.
* Save the modified settings to the `config.json` file.

### How to use Config Editor:

1. Run the script `config_editor.py`:

   ```bash
   python config_editor.py
   ```

2. A simple graphical interface will open, where you can:

   * **Add a new device**: Enter the IP address and device name.
   * **Edit an existing device**: Select a device from the list and modify its IP or name.
   * **Remove a device**: Select a device and delete it.

3. After each change, the new configuration will automatically be saved to `config.json`.

---

## 🚀 Starting the Server

1. Make sure you have **Python 3** installed.
2. In the project directory, run:

```bash
python server.py
```

3. Open your browser and go to:

```
http://192.168.1.49:8080
```

(replace with your IP and port)

---

## 📝 Log Example

```
xxx.xxx.1.49 - kok - - [21/Apr/2025 13:30:44] "GET / HTTP/1.1" 200 -
xxx.xxx.1.49 - kok - - [21/Apr/2025 13:30:46] code 404, message File not found
xxx.xxx.1.49 - kok - - [21/Apr/2025 13:30:46] "GET /favicon.ico HTTP/1.1" 404
```

---

## 💡 Notes

* Logs are saved to `server_log.txt`
* The old logging format is **completely disabled** (no "192.168.x.x - -")
* HTML and other files should be placed in the same directory as `server.py`
* **Config Editor** allows managing devices easily without manually editing `config.json`.

---

## 🔧 In future updates

* Admin interface for viewing logs in the browser
* 404 error notifications
* Log search functionality
* Logging into different files based on the device

---
ver.:2.0.0
> Denis Varga 😀 ` denisvarga.eu`
