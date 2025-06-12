# Keeboard

In this project, I made a custom mechanical keyboard using a Raspberry Pi Pico clone. The main feature that makes this unique is the connectors on either side of the board that allow it to be connected to external modules. I plan to make a wireless macropad / numberpad in a future project, that can be connected to either side of the keyboard to charge. These connectors will also include I²C communication, which should give me the option of adding more features, such as a screen, in the future.

![image](https://github.com/user-attachments/assets/000ffb94-b1bc-40e2-98c2-b1048e56a59c)

# Features

* Modular design allows for future expansions.
* Tenkeyless Layout
* 87 Keys
* 3D Printed Case and Plate
* 3D Printed TPU Feet
* USB C Connector

# Background

My main inspiration when designing this keyboard came from the Mountain Everest Max. The Everest Max features a removable number pad which can be attached to either side of the keyboard. This allows you to put it on the left side, which is more convenient for daily usage as it allows you to type in numbers with your left hand and move the mouse with your right hand without stretching your hand too far over. This setup is also ideal for gaming as it helps to maximize the mamount of mouse room on the right side of the board. To replicate this functionality in my own board, I put magnetic pogo pins on the sides of the board that allow the macropad/numberpad to connect to the keyboard. The four pins include a 5V pin, a ground pin, and two pins for I²C communication. This should leave me with plenty of options for expandability in the future.

The keyboard itself runs off of a Pi Pico clone, which was chosen for its high quanitity of GPIO pins and USB C port (compared to the Micro USB B port of the actual Pico). It uses MMD Princess V2 Tactile Switches, and its keys are arranged in a 6x17 matrix. The keyboard has a white color scheme with Blue 8008 keycaps. The case and plate are designed to be printed in two halves and then assembled, where they will then be held to gether by keying features, heat set inserts, and the screws running through the case and PCB.
