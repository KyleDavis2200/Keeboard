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

4 Hours

Today, I worked on getting the connectors for the external modules added to the PCB. I modeled each connector in Solidworks and then creasted a footprint for the connector with the 3D model in Kicad.
![image](https://github.com/user-attachments/assets/3c1c91c1-450c-4678-8fec-c3d1306704b4)

![image](https://github.com/user-attachments/assets/2949abdd-50ed-413b-b478-fc2a3739ff97)

After this, I created the ground planes to finish the board layout and exported the board as a STEP file.

6/5/25

1 Hour

I imported the board into Solidworks and modeled the baseplate.

6/9/25

4 Hours

Today, I imported all of the keycaps into the model and modeled the plate. To create the cutouts for each key in the plate I used https://www.keyboard-layout-editor.com to make the layout and http://builder.swillkb.com to create a DXF profile where all of the cutouts for the keys would be. Then, I imported this to Solidworks as a DxF which I then used to create the cutouts in the plate.
![image](https://github.com/user-attachments/assets/847e725d-674e-4b05-a5f9-9edd6c486875)

6/10/25

6 Hours

All I had left to do today is design the case. I needed to design the case to split in half to fit on my printer. The case will be printed out of PLA and the feet on the bottom of the board will be printed out of TPU. The two halves of the case are aligned with keying features and are held together with the four M3 screws that hold the entire keyboard together. Each of the upper feet are held on with two M3 screws and also have a keying feature for alignment, while the lower feet are held on with four snap fit joints.

![image](https://github.com/user-attachments/assets/64914736-fe9f-4736-9849-146ac79f6e92)

Finished Product:

![image](https://github.com/user-attachments/assets/000ffb94-b1bc-40e2-98c2-b1048e56a59c)

![image](https://github.com/user-attachments/assets/1d9acb10-5df5-4355-878d-e9188b7a2685)

![image](https://github.com/user-attachments/assets/0a6baa3a-fc72-44a8-9d63-af3da7d6a95a)

Well... It turns out I wasn't finished. The keyboard came out way over budget, so I will need to redesign it to cut costs. Instead of using an aluminum plate and an aluminum base plate, I am going to make them both out of PLA (base plate integrated into case). This should cut costs significantly, but that will have to wait for another day.
![image](https://github.com/user-attachments/assets/61493d56-6516-4113-9cf7-1fe43a3d00d3)

6/11/25

1 Hour

Remade the case to incorporate the base plate into the print. I used heat set inserts to replace the tapped holes in the aluminum baseplate. Also split the plate in half to allow it to fit on my printer. With this, the design is done and all I have left to do is to optimize the BOM to get it under budget and to fully ship the project.

The board looks pretty much identical to how it did in the "finished product" above.

![image](https://github.com/user-attachments/assets/e91ab193-1a94-40e1-aff9-fbbbc6620f59)



