import http.server
import socketserver
import logging
import json

# Načítanie konfigurácie zo súboru
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

PORT = config['port']
HOST = config['host']
IP_TO_NAME = config['ip_to_name']

# Nastavenie logovania
logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(message)s')

# Vlastný handler
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_request(self, code='-', size='-'):
        client_ip = self.client_address[0]
        device_name = IP_TO_NAME.get(client_ip, "Unknown Device")
        request_path = self.path
        status_code = code

        # Formátovaný log
        log_entry = (
            f"[{self.log_date_time_string()}] "
            f"MENO: {device_name} | IP: {client_ip} | SUBOR: {request_path} | STATUS: {status_code}"
        )

        logging.info(log_entry)
        print(log_entry)

# Spustenie servera
Handler = MyHandler
with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"✅ Server beží na http://{HOST}:{PORT}")
    httpd.serve_forever()

