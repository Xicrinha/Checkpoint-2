import network
import time
import json
from machine import Pin, I2C
from i2c_lcd import I2cLcd
import urequests
from umqtt.simple import MQTTClient

# --- CONFIGURAÇÕES DE REDE E API ---
SSID = "Wokwi-GUEST"
PASSWORD = ""

API_KEY = "66608d49d80bb4eca2ac840c408bc7e4"
CIDADE = "Sao%20Paulo"

# --- CONFIGURAÇÕES MQTT ---
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "esp32_fiap_grupo01"
MQTT_TOPIC = "fiap/iot/grupo01/temperatura"

# --- CONFIGURAÇÃO DO DISPLAY LCD I2C ---
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
lcd = I2cLcd(i2c, 0x27, 4, 20)

lcd.putstr("Conectando Wi-Fi...")

# --- CONEXÃO WI-FI ---
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    time.sleep(0.5)

lcd.clear()
lcd.putstr("Wi-Fi Conectado!")
time.sleep(1)

# --- CONEXÃO MQTT ---
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
client.connect()

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    "?q=" + CIDADE +
    "&appid=" + API_KEY +
    "&units=metric"
)

while True:
    try:
        lcd.clear()
        lcd.putstr("Buscando dados...")
        
        response = urequests.get(url)
        
        if response.status_code == 200:
            dados = response.json()
            temp = dados["main"]["temp"]
            hum = dados["main"]["humidity"]
            cond = dados["weather"][0]["description"]
            
            # Exibe no LCD 20x4
            lcd.clear()
            lcd.putstr("Cidade: " + dados["name"][:12])
            lcd.move_to(0, 1)
            lcd.putstr("Temp: " + str(temp) + " C")
            lcd.move_to(0, 2)
            lcd.putstr("Umidade: " + str(hum) + "%")
            lcd.move_to(0, 3)
            lcd.putstr(cond[:20])
            
            # Publica via MQTT em formato JSON
            payload = {
                "temperatura": temp,
                "umidade": hum,
                "cidade": dados["name"]
            }
            client.publish(MQTT_TOPIC, json.dumps(payload))
            print("Dados publicados via MQTT:", payload)
            
        else:
            lcd.clear()
            lcd.putstr("Erro API: " + str(response.status_code))
            
        response.close()
        
    except Exception as e:
        print("Erro no ciclo:", e)
        
    # Aguarda 15 segundos antes de atualizar novamente
    time.sleep(15)