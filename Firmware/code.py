print("Starting")

import board
import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins= (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16) #Cols
keyboard.row_pins = (board.GP22, board.GP21, board.GP20, board.GP19, board.GP18, board.GP17) #Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#Keymap
keyboard.keymap =[
    [
        KC.ESC, KC.NO, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.INS, KC.HOME, KC.PGUP,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL, KC.END, KC.PGDN,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.NO, KC.ENT, KC.NO, KC.NO, KC.NO,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.NO, KC.RSHIFT, KC.NO, KC.NO, KC.UP, KC.NO,
        KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.NO, KC.RALT, KC.RGUI, KC.NO, KC.NO, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,
    ]
]

if __name__ == "__main__":
    keyboard.go()

