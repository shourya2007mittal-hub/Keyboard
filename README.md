# KEYBOARD
So I am making an 60% layout keyboard with 2 rotor encoders .So In total there will be 61 Keys and 2 rotor encoders for volume and britness controle but there aren't that many gpios in any devboard therefore I would be using keyboard matrix and diodes to restrict gosting and I choosed Raspberry Pico as controller because it supports KMK and have enought Gpios as well.I also added stabalizers for any keys whose size is over 1.75U
## Features

- Base on Raspberry pico
- Has 61 keys ( 60% Keyboard Matrix)
- Has 2 Rotor Encoder
  ### Schematic
  br><img width="953" height="676" alt="Screenshot 2026-05-28 121645" src="https://github.com/user-attachments/assets/7dfaafa4-fcb3-44d4-ac15-0d798fb7ef2c" />

  ###  PCB Design
<br><img width="1379" height="463" alt="Screenshot 2026-05-28 123357" src="https://github.com/user-attachments/assets/df8385af-7e9b-41be-adf5-534a1874c514" />
<img width="1535" height="497" alt="Screenshot 2026-05-28 123220" src="https://github.com/user-attachments/assets/666dae93-1ae6-4b11-8631-de25a87bbf26" />

### 3D Design


<img width="816" height="348" alt="Screenshot 2026-05-28 124031" src="https://github.com/user-attachments/assets/1d5decf0-106b-405a-b507-27c890baacf9" />




- ## Bill of Materials (BOM)

| # | Item | Description | Quantity | Unit Price (USD) | Total (USD) | Link |
|---|------|-------------|----------|------------------|-------------|------|
| 1 | 80Retros x HMX Volume | Mechanical switches (pack of 35) | 2 packs | 17.8 | 35.6 | https://stackskb.com/store/hmx-volume-0-pack-of-35/ |
| 2 | 1N4148 Diode | DO-35 switching diode | 61 | 0 | 0 | | Already have
| 3 | Raspberry Pi Pico H | RP2040 microcontroller board | 1 | 5.5 | 5.5 | https://robu.in/product/raspberry-pi-pico-with-headers/ |
| 4 |  Keycap Set | Full keycap set | 1 | 26.2 | 26.2 | https://stackskb.com/store/blue-and-blue-double-shot-abs-cherry-profile-keycaps-pre-order/
| 5 | Screw-In Stabilizers V2 | Keyboard stabilizers | 1 | 0 |0 | Already have |
| 6 | PCB  + Shipping | PCB fabrication (JLCPCB) | 1 |31.55| 31.55 | https://jlcpcb.com |

**Estimated Total Hardware Cost:** **USD 98.85**

## Hardware
- Raspberry Pico 
- Cherry MX compatible Switches
- Diode
- 2 layer PCB
- 2 Rotor Encoder

## Firmware
- It is Based on KMK and Circuit Python
