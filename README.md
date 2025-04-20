




# Lokálny Web Server v Pythone s Logovaním

Tento projekt vytvára jednoduchý lokálny web server v Pythone, ktorý obsluhuje požiadavky na HTML súbory. Server zaznamenáva logy o pripojení klientov, vrátane **IP adresy** a **požiadavky**. Všetky požiadavky sa ukladajú do súboru `server_logs.txt` .

## Funkcionalita

- **Obsluha HTML súborov**: Server dokáže obslúžiť HTML súbory v aktuálnom priečinku. Ak zadáš URL ako `http://localhost:8080/s.html`, server načíta a zobrazí obsah súboru `s.html` alebo `http://localhost:8080/` tak načíta a zobrazí obsah súboru `index.html`.
- **Logovanie pripojení**: Každé pripojenie a požiadavka sú zaznamenané do súboru `server_logs.txt`. Záznam obsahuje:
  - **IP adresu klienta**
  - **Požiadavku** (čo sa klient snažil otvoriť)
- **Zobrazovanie 404 chyby**: Ak požadovaný súbor neexistuje, server vráti **404 Not Found**.

## Požiadavky

- **Python 3.x** (so zabudovaným moduly `http.server`)
- **Raspberry Pi** (alebo akýkoľvek počítač so systémom Linux/Mac/Windows s Pythonom)
- **Prístup k terminálu / príkazovému riadku**

## Inštalácia

1. **Nainštaluj Python 3**:
   Ak nemáš ešte nainštalovaný Python 3, môžeš ho nainštalovať podľa týchto krokov:
   
   - Na **Windows**: Stiahni a nainštaluj Python z [python.org](https://www.python.org/downloads/).
   - Na **Linux/Mac**: Python je často predinštalovaný. Skontroluj, či ho máš pomocou príkazu:
     ```bash
     python3 --version
     ```
     Ak nie, nainštaluj ho cez balíčkový manažér:
     ```bash
     sudo apt install python3
     ```

2. **Skopíruj kód do súboru**:
   Ulož kód servera (predchádzajúci Python kód) do súboru s názvom `server.py`.

3. **Vytvor priečinok s HTML súbormi**:
   Vytvor priečinok s HTML súbormi, ktoré chceš, aby server zobrazil. Môžeš pridať napríklad súbory `index.html`, `s.html` a ďalšie.

4. **Spusti server**:
   Otvor terminál a prejdite do adresára, kde je súbor `server.py` a HTML súbory. Potom spusti server príkazom:
   ```bash
   python3 server.py
   ```

5. **Prístup k serveru**:
   Otvor webový prehliadač a navštív:
   ```
   http://localhost:8080
   ```
   - Ak zadáš `http://localhost:8080/s.html`, server načíta súbor `s.html` (ak existuje).
   - Ak zadáš neexistujúci súbor, server vráti **404 Not Found**.

## Logy

Logy o požiadavkách sú uložené v súbore **`server_logs.txt`**. Každý záznam obsahuje:
- **IP adresu klienta**
- **Požiadavku** (čo sa klient snažil otvoriť)

Príklad záznamu v logu:
```
IP: 192.168.1.100 požiadavka: /index.html
IP: 192.168.1.101 požiadavka: /s.html
```

## Možnosti rozšírenia

- Pridať podporu pre ďalšie typy súborov (napr. CSS, obrázky).
- Zlepšiť logovanie o časových pečiatkach alebo podrobnejších informáciách.
- Pridať autentifikáciu na zabezpečený prístup k serveru.
- Podpora pre rôzne porty alebo iné metódy HTTP (POST, PUT, DELETE).

---

**Autor**: Denis  
**Licencia**: MIT


---

### 🚀 Ako to používať:

1. **Inštalácia Pythonu**: Ak ešte nemáš Python, nainštaluj si ho. Môžeš si stiahnuť najnovšiu verziu Pythonu z [python.org](https://www.python.org/downloads/), alebo na Linuxe použiť príkaz:
   ```bash
   sudo apt install python3
   ```

2. **Spustenie servera**:
   - Ulož kód do súboru `server.py`.
   - Pridaj svoje HTML súbory (napr. `index.html`, `s.html`).
   - Spusti server:
     ```bash
     python3 server.py
     ```

3. **Prístup cez prehliadač**:
   - Navštív **http://localhost:8080** v prehliadači.
   - Otvor požiadavku, napríklad **http://localhost:8080/s.html**, ak máš súbor `s.html`.

4. **Logovanie**:
   - Logy o pripojeniach a požiadavkách sa ukladajú do súboru **`server_logs.txt`**.

---

Týmto by mal byť projekt plne funkčný, a ty môžeš sledovať pripojenia a spravovať HTML súbory cez server! 😊

Ak budeš potrebovať ďalšiu pomoc alebo vylepšenia, určite sa ozvi!
