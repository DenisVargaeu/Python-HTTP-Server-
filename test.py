import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging

class MalyServer(SimpleHTTPRequestHandler):
    
    def log_request(self, code='-', size='-'):
        # Získanie IP adresy klienta
        client_ip = self.client_address[0]
        # Získanie požiadavky od klienta
        requested_path = self.path
        
        # Zaznamenanie informácií do log súboru
        logging.basicConfig(filename='server_logs.txt', level=logging.INFO)
        logging.info(f"IP: {client_ip} požiadavka: {requested_path}")
        
        # Zavoláme predvolenú metódu na logovanie
        super().log_request(code, size)
    
    def do_GET(self):
        # Nastavenie cesty k súborom
        if self.path == "/":
            self.path = "/index.html"  # Prednastavená stránka, ak sa nešpecifikuje súbor

        # Správne spracovanie cesty k súborom
        file_path = os.getcwd() + self.path
        
        if os.path.exists(file_path) and os.path.isfile(file_path):
            # Zobrazí požadovaný súbor
            super().do_GET()
        else:
            # Ak súbor neexistuje, zobrazí 404
            self.send_error(404, "Súbor nenájdený")

def run():
    print("🚀 Server beží na http://localhost:8080 ...")
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MalyServer)
    httpd.serve_forever()

run()
