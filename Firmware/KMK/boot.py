import board
import digitalio
import storage
import usb_cdc
import usb_hid
import time

# ---- SET YOUR ROW PINS HERE ----
ROW_PINS = [
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6
]

pressed = False
rows = []

for pin in ROW_PINS:
    row = digitalio.DigitalInOut(pin)
    row.direction = digitalio.Direction.INPUT
    row.pull = digitalio.Pull.UP
    rows.append(row)

time.sleep(0.1)

for row in rows:
    if not row.value:   # LOW = key pressed
        pressed = True
        break

if not pressed:
    # Normal keyboard mode
    storage.disable_usb_drive()
    usb_cdc.disable()
