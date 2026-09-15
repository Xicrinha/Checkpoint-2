# Checkpoint 2 - Computational Thinking for Engineering

**Autor:** César Augusto da Silva Castelo Branco Coelho Filho (RM: 565273)

Este repositório contém a solução prática para a atividade de Internet das Coisas (IoT) utilizando o microcontrolador **ESP32** com **MicroPython**.

## Objetivo do Projeto
Desenvolver e testar aplicações de comunicação integrando os seguintes recursos:
- Controle de **Display LCD 20x4** via protocolo I2C.
- Consulta de dados meteorológicos em formato JSON via **API HTTP** (OpenWeather).
- Comunicação de telemetria utilizando o protocolo **MQTT**.

## Funcionalidades e Etapas

### 1. Display LCD 20x4
- Simulação do circuito no Wokwi acoplado a um display 20x4.
- Utilização dos drivers `lcd_api.py` e `i2c_lcd.py` para comunicação I2C.
- Exibição local de mensagens customizadas.

### 2. Consulta à API OpenWeather
- Conexão Wi-Fi utilizando a rede simulada `Wokwi-GUEST`.
- Requisições HTTP com a biblioteca `urequests`.
- Extração de dados meteorológicos fundamentais (Temperatura, Umidade e Condição do Tempo) a partir da resposta em JSON.

### 3. Comunicação MQTT
- Conexão ao broker público **HiveMQ**.
- Publicação periódica de payloads estruturados em JSON.
- Inscrição (Subscribe) em tópico próprio da equipe e visualização dos dados via **Node-RED**.

### Desafio de Integração
O sistema final consolida os três pilares operando de forma contínua no seguinte fluxo de informações:
> **OpenWeather API** → **ESP32** → **LCD + MQTT** → **Node-RED**

1. O ESP32 acessa a internet e obtém o clima atual da plataforma OpenWeather.
2. Trata os dados recebidos e os exibe no Display LCD 20x4.
3. Empacota os dados processados em um novo JSON e publica no tópico via MQTT.
4. O Node-RED recebe o pacote MQTT e permite a visualização interativa das informações.

##️ Tecnologias Utilizadas
* **Hardware:** ESP32
* **Linguagem:** MicroPython
* **Simulador:** Wokwi
* **Plataformas de Integração:** MQTT (HiveMQ), Node-RED, API REST (OpenWeather)

## Referência
Projeto desenvolvido com base no documento descritivo da disciplina: *Atividade_ESP32_MicroPython_LCD_API_MQTT.pdf*.
