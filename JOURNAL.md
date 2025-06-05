---
title: KeeBoard
author: Kyle Davis
description: A custom keyboard designed with future expandability in mind
created_at: 2025-05-25
---

title work in progress

5/25/2025

4 Hours

I began this project by first researching how keyboard PCBs were laid out, as I knew that would be the main challenge in this project. I came across [a video series by Joe Scotto](https://www.youtube.com/playlist?list=PLBD2IS_t_iWZDMdG_ZF57x9Ebm3kxKqxF) that helped me understand exactly how everything would be laid out. These tutorials guided me towards keyboard-layout-editor.com, where I layed out a standard TKL layout for this keyboard.

![](https://github.com/KyleDavis2200/Keyboard/blob/main/Images/Main-Board.png)

Following the instructions in these tutorials, I then began to plan out how I would layout the columns and rows for this keyboard. 
![](https://github.com/KyleDavis2200/Keyboard/blob/main/Images/Main%20Board-ANNOTATED.png)

5/26/2025

8 Hours

Using the previous drawing of the rows and columns for the key matrix, I began making a schematic in KiCad of the keyboard, using symbols from [Joe Scotto's library](https://github.com/joe-scotto/scottokeebs).

![](https://github.com/KyleDavis2200/Keyboard/blob/main/Images/image_2025-06-01_213113712.png)

I then moved onto selecting exactly which switches and keycaps I would use. I opted for Princess Tactile switches and 8008 keycaps. I also selected the cable and stabilizers I would be using for this build at this time.

![image](https://github.com/user-attachments/assets/e1c56e34-e744-4a74-a08f-48c2ef5b5f28)

Next, I created a rough layout of the PCB, including the Pico, the diodes, and all of the key switches.
![image](https://github.com/user-attachments/assets/ec49ce8c-d264-4926-8151-4691e298af1a)
![image](https://github.com/user-attachments/assets/484fb0c8-4ec5-4803-a765-1c700029485c)

5/30/25

2 Hours

Today, I polished up the board layout by adjusting the location of the Pico to better fit between the switches and made some of the remaining traces that I had not made previously. At this point, the remaining steps in the PCB design in Kicad are to add the connectors for expanding with future modules, adding a ground plane, and creating mounting for the stabilizers. After that, the rest of the design, designing the case and plate, will be done in Solidworks.

6/1/25

1 Hour

Today, I focused on getting the journal up to date and adding images to the journal. I also went back and switched from 3 pin connectors (which I had only been using 2 pins on, as I could not find 2 pin connectors) for the expandable modules to 4 pin connectors, which allowed me to use I²C to communicate with the external modules. This would allow me to use wired communication to the external modules, instead of just using the connection as a charging port for wireless modules. I do still aim to make a wireless macropad/keypad, but this creates the option of making a screen module or a slider/knob module. As of writing this, I am realizing that the signals for the I²C communication should be sent to seperate GPIO pins from the connector on each side of the keyboard, instead of sharing GPIO pins, which would make it possible to use two modules at a time. After some research, I found that I can connect the devices in parallel as I had previously designed them, which is ideal as I would have been one GPIO pin too short to make seperate a seperate I²C channel for each side of the board.

6/4/25

Today, I worked on getting the connectors for the external modules added to the PCB. I modeled each connector in Solidworks and then creasted a footprint for the connector with the 3D model in Kicad.
![image](https://github.com/user-attachments/assets/3c1c91c1-450c-4678-8fec-c3d1306704b4)

![image](https://github.com/user-attachments/assets/2949abdd-50ed-413b-b478-fc2a3739ff97)
