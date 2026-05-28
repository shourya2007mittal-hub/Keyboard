# KEYBOARD
I started with picking up Raspberry Pico as out main microcontroller and this would be a 60 % layout Keyboard with 2 rotor encoders.
The rotor encoders will be use to control Brightness and Volume and the switch in those 2 encoders will act as a custom key to take screenshot and to delete.
I also did the schematic of the keyboard, I added the stabilizers to the switches which were longer then 1.75U.
The Keyboard uses a matrix grid so i need only a few gpio pins for the whole keyboard to work.
## Features

- Base on Raspberry pico
- Has 61 keys ( 60% Keyboard Matrix)
- Has 2 Rotor Encoder
  ### Schematic
  <img width="1309" height="939" alt="Screenshot (97)" src="https://github.com/user-attachments/assets/f3ae7811-5523-4442-93c6-677eab70dc50" /><br>
  ###  PCB Design
<img width="1536" height="605" alt="Screenshot (98)" src="https://github.com/user-attachments/assets/bb2fe7f3-91fb-42c6-ace2-83d5c71401bc" /><br>

### 3D Design
<img width="826" height="511" alt="Screenshot (295)" src="https://github.com/user-attachments/assets/3a7c6106-6f94-494e-9434-45eb0a77490b" />
<br>
<img width="829" height="637" alt="Screenshot (294)" src="https://github.com/user-attachments/assets/19efdbb8-bcef-42e3-8874-303b7ffaff0f" />
<img width="1223" height="687" alt="Screenshot (293)" src="https://github.com/user-attachments/assets/97220df1-c722-4c20-a60e-d5e13c18a0f2" />



- ## Bill of Materials (BOM)

| # | Item | Description | Quantity | Unit Price (USD) | Total (USD) | Link |
|---|------|-------------|----------|------------------|-------------|------|
| 1 | 80Retros x HMX Volume | Mechanical switches (pack of 35) | 2 packs | 17.8 | 35.6 | https://stackskb.com/store/hmx-volume-0-pack-of-35/ |
| 2 | 1N4148 Diode | DO-35 switching diode | 61 | 0 | 0 | | Already have
| 3 | Raspberry Pi Pico H | RP2040 microcontroller board | 1 | 5.5 | 5.5 | https://robu.in/product/raspberry-pi-pico-with-headers/ |
| 4 |  Keycap Set | Full keycap set | 1 | 27.7 | 27.7 | https://stackskb.com/store/blue-and-blue-double-shot-abs-cherry-profile-keycaps-pre-order/ |
| 5 | Screw-In Stabilizers V2 | Keyboard stabilizers | 1 | 0 |0 | Already have |
| 6 | PCB + Shipping | PCB fabrication (JLCPCB) | 1 | 29.51 | 29.51 | https://jlcpcb.com |

**Estimated Total Hardware Cost:** **USD 98.31**

## Hardware
- Raspberry Pico 
- Cherry MX compatible Switches
- Diode
- 2 layer PCB
- 2 Rotor Encoder

## Firmware
- It is Based on KMK and Circuit Python
