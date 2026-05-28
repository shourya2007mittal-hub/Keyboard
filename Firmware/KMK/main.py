import board
import digitalio
import usb_hid
import rotaryio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import time

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# =========================
# MATRIX SETUP
# =========================

ROW_PINS = [board.GP2, board.GP3, board.GP4, board.GP5, board.GP6]
COL_PINS = [
    board.GP7, board.GP8, board.GP9, board.GP10,
    board.GP11, board.GP12, board.GP13,
    board.GP14, board.GP15, board.GP16,
    board.GP17, board.GP18, board.GP19, board.GP20
]

rows = []
cols = []

for pin in ROW_PINS:
    r = digitalio.DigitalInOut(pin)
    r.direction = digitalio.Direction.OUTPUT
    r.value = True
    rows.append(r)

for pin in COL_PINS:
    c = digitalio.DigitalInOut(pin)
    c.direction = digitalio.Direction.INPUT
    c.pull = digitalio.Pull.UP
    cols.append(c)

# Example 60% partial keymap (edit fully yourself)
keymap = [
    [Keycode.ESCAPE, Keycode.ONE, Keycode.TWO, Keycode.THREE, Keycode.FOUR,
     Keycode.FIVE, Keycode.SIX, Keycode.SEVEN, Keycode.EIGHT,
     Keycode.NINE, Keycode.ZERO, Keycode.MINUS,
     Keycode.EQUALS, Keycode.BACKSPACE],

    [Keycode.TAB, Keycode.Q, Keycode.W, Keycode.E, Keycode.R,
     Keycode.T, Keycode.Y, Keycode.U, Keycode.I,
     Keycode.O, Keycode.P, Keycode.LEFT_BRACKET,
     Keycode.RIGHT_BRACKET, Keycode.BACKSLASH],

    [Keycode.CAPS_LOCK, Keycode.A, Keycode.S, Keycode.D, Keycode.F,
     Keycode.G, Keycode.H, Keycode.J, Keycode.K,
     Keycode.L, Keycode.SEMICOLON, Keycode.QUOTE,
     Keycode.ENTER, None],

    [Keycode.LEFT_SHIFT, Keycode.Z, Keycode.X, Keycode.C, Keycode.V,
     Keycode.B, Keycode.N, Keycode.M, Keycode.COMMA,
     Keycode.PERIOD, Keycode.FORWARD_SLASH,
     Keycode.RIGHT_SHIFT, None, None],

    [Keycode.LEFT_CONTROL, Keycode.LEFT_GUI,
     Keycode.LEFT_ALT, None, None, None,
     Keycode.SPACE, None, None,
     Keycode.RIGHT_ALT, Keycode.FN,
     Keycode.RIGHT_CONTROL, None, None]
]

pressed_keys = set()

# =========================
# ROTARY ENCODERS
# =========================

# Encoder 1 (Volume)
encoder1 = rotaryio.IncrementalEncoder(board.GP26, board.GP27)
last_pos1 = encoder1.position

# Encoder 2 (Brightness)
encoder2 = rotaryio.IncrementalEncoder(board.GP28, board.GP21)
last_pos2 = encoder2.position

# Encoder buttons
enc1_btn = digitalio.DigitalInOut(board.GP22)
enc1_btn.direction = digitalio.Direction.INPUT
enc1_btn.pull = digitalio.Pull.UP

enc2_btn = digitalio.DigitalInOut(board.GP1)
enc2_btn.direction = digitalio.Direction.INPUT
enc2_btn.pull = digitalio.Pull.UP

# =========================
# MAIN LOOP
# =========================

while True:

    # ----- MATRIX SCAN -----
    for r_idx, row in enumerate(rows):
        row.value = False

        for c_idx, col in enumerate(cols):
            if not col.value:
                key = keymap[r_idx][c_idx]
                if key and key not in pressed_keys:
                    kbd.press(key)
                    pressed_keys.add(key)
            else:
                key = keymap[r_idx][c_idx]
                if key and key in pressed_keys:
                    kbd.release(key)
                    pressed_keys.remove(key)

        row.value = True

    # ----- ENCODER 1 (Volume) -----
    pos1 = encoder1.position
    if pos1 > last_pos1:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif pos1 < last_pos1:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    last_pos1 = pos1

    # ----- ENCODER 2 (Brightness) -----
    pos2 = encoder2.position
    if pos2 > last_pos2:
        cc.send(ConsumerControlCode.BRIGHTNESS_INCREMENT)
    elif pos2 < last_pos2:
        cc.send(ConsumerControlCode.BRIGHTNESS_DECREMENT)
    last_pos2 = pos2

    # ----- Encoder Buttons -----
    if not enc1_btn.value:
        # Screenshot (Win+Shift+S)
        kbd.press(Keycode.LEFT_GUI, Keycode.LEFT_SHIFT, Keycode.S)
        time.sleep(0.1)
        kbd.release_all()

    if not enc2_btn.value:
        # Delete
        kbd.send(Keycode.DELETE)

    time.sleep(0.01)
