


# 🌐 Python HTTP Server s vlastným logovaním

Tento projekt je jednoduchý Python HTTP server, ktorý slúži súbory cez sieť a **loguje prístup každého zariadenia prehľadne**:

✅ Zistí IP klienta  
✅ Priradí mu meno podľa `config.json`  
✅ Loguje: čas, meno, IP, požadovaný súbor, HTTP kód  
✅ Nepoužíva starý formát logov (čistý výpis!)



## 📁 Štruktúra projektu

```
projekt/
├── server.py          # hlavný serverový skript
├── config.json        # konfigurácia IP adries a portu
├── server_log.txt     # automaticky generovaný prehľadný log
├── README.md          # tento návod
└── (tvoje súbory)     # HTML/CSS/JS ktoré server obsluhuje
```



## ⚙️ Konfigurácia

### `config.json`
```json
{
  "host": "192.168.1.49",
  "port": 8080,
  "ip_to_name": {
    "xxx.xxx.1.171": "mobil",
    "xxx.xxx.1.49": "pc"
  }
}
```

- `host`: IP adresa, na ktorej server beží
- `port`: port (napr. 8080)
- `ip_to_name`: mapovanie IP na mená zariadení

---

## 🚀 Spustenie servera

1. Uisti sa, že máš nainštalovaný **Python 3**.
2. V adresári spusti:

```bash
python server.py
```

3. Otvor prehliadač a choď na:

```
http://192.168.1.49:8080
```

(nahradiť podľa tvojej IP a portu)

---

## 📝 Ukážka logu

```
xxx.xxx.1.49 - kok - - [21/Apr/2025 13:30:44] "GET / HTTP/1.1" 200 -
xxx.xxx.1.49 - kok - - [21/Apr/2025 13:30:46] code 404, message File not found
xxx.xxx.1.49 - kok - - [21/Apr/2025 13:30:46] "GET /favicon.ico HTTP/1.1" 404
```

---

## 💡 Poznámky

- Logy sa ukladajú do `server_log.txt`
- Starý formát logovania je **úplne vypnutý** (žiadne „192.168.x.x - -“)
- HTML a iné súbory daj do rovnakého priečinka ako `server.py`

---

## 🔧 Možné rozšírenia

- Admin rozhranie pre zobrazovanie logov v prehliadači
- Upozornenie pri 404
- Vyhľadávanie v logoch
- Logovanie do rôznych súborov podľa zariadenia

---

>Denis Varga 😀 ``` denisvarga.eu```
