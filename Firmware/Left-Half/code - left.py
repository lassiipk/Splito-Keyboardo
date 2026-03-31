print("Mee0w from Left side of Splito keyboard!")
print("Launching Mee0w... inthe KMK world!")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display.ssd1306 import SSD1306
import busio

#-----------------------------------------------------------------------------------

keyboard = KMKKeyboard()

# ==============================
#Switch setup
# ==============================

keyboard.col_pins = (board.D9, board.D15, board.D18, board.D19 board.D21)
keyboard.row_pins = (board.D4, board.D5, board.D6, board.D7, board.D8, board.DNO)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 5x6 matrix

keyboard.keymap = [

    [KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5, KC.NO,
     KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N10,KC.NO,
     KC.N11, KC.N12, KC.N13, KC.N14, KC.N15,KC.NO,
     KC.N16, KC.N17, KC.N18, KC.N19, KC.N20,KC.NO,
     KC.N21, KC.N22, KC.N23, KC.N24, KC.N25 KC.NO],      
    
    ],

#------------------------------------------------------------------------------------

# ==============================
#Display setup
# ==============================

# I2C setup
i2c = busio.I2C(board.D3, board.D2)

# Driver FIRST
driver = SSD1306(
    i2c=i2c,
    device_address=0x3C,
)

# Then Display

display = Display(
    display=driver,
    entries=[

        #TextEntry(text="Made with ♥ by SAIM", x=0, y=0, inverted=True, layer=0   ),
        #TextEntry(text="Is't it Cool???? Huh?", x=0, y=16, inverted=True, layer=0 ),

        ImageEntry(
            
            image="1.bmp"#, x=0, y=0
        
        ),    
           
        ],

    width=128,
    height=32,
    flip = True, # flips your display content
    #flip_left = False, # flips your display content on left side split
    #flip_right = True, # flips your display content on right side split
    #brightness=0.8, # initial screen brightness level
    #brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=15, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=30, # time in seconds to turn off screen
    #powersave_dim_time=10, # time in seconds to reduce screen brightness
    #powersave_dim_target=0.1, # set level for brightness decrease
    #powersave_off_time=30, # time in seconds to turn off screen

)

keyboard.extensions.append(display)

#------------------------------------------------------------------------------------

if __name__ == '__main__':
    keyboard.go()