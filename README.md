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
* KMK Firmware

# Background

My main inspiration when designing this keyboard came from the Mountain Everest Max. The Everest Max features a removable number pad which can be attached to either side of the keyboard. This allows you to put it on the left side, which is more convenient for daily usage as it allows you to type in numbers with your left hand and move the mouse with your right hand without stretching your hand too far over. This setup is also ideal for gaming as it helps to maximize the mamount of mouse room on the right side of the board. To replicate this functionality in my own board, I put magnetic pogo pins on the sides of the board that allow the macropad/numberpad to connect to the keyboard. The four pins include a 5V pin, a ground pin, and two pins for I²C communication. This should leave me with plenty of options for expandability in the future.

The keyboard itself runs off of a Pi Pico clone, which was chosen for its high quanitity of GPIO pins and USB C port (compared to the Micro USB B port of the actual Pico). It uses MMD Princess V2 Tactile Switches, and its keys are arranged in a 6x17 matrix. The keyboard has a white color scheme with Blue 8008 keycaps. The case and plate are designed to be printed in two halves and then assembled, where they will then be held to gether by keying features, heat set inserts, and the screws running through the case and PCB. The case also features carefully placed cylinders to act like standoffs to support the PCB. The aim with this was to give the board a more solid feel than it otherwise would have, as I was worried about the PCB flexing if a key is pressed too hard.

# Images

### PCB:

Schematic:

![image](https://github.com/user-attachments/assets/87a5833b-df61-42e8-8393-87130a53c252)

Front:

![image](https://github.com/user-attachments/assets/87d26551-021b-4a17-a9c9-2c0e55f7c9ba)

Back:

![image](https://github.com/user-attachments/assets/6082f38e-1d38-45b1-a5c3-80429cf883bc)

3D View:

![image](https://github.com/user-attachments/assets/1532ab9e-a589-4e56-ad91-9fef29abcda1)


### CAD:

Isometric:

![image](https://github.com/user-attachments/assets/2d376f18-136c-4a6b-be7e-b61e0ae7a144)

Front View:

![image](https://github.com/user-attachments/assets/5d17b7b1-2008-4b0b-a14d-b673a3c53a87)

Side View:

![image](https://github.com/user-attachments/assets/3f54e12b-c284-4a91-9348-8b9789435811)

Top View:

![image](https://github.com/user-attachments/assets/d5cb60e5-5211-4f2c-9b56-5e2546696687)

Back View:

![image](https://github.com/user-attachments/assets/12e8ded4-1b9a-4817-b722-becd98614d5d)

# BOM

| Item                  | Price  | Link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| RP2040 Pico USB C     | 1.99   | https://www.aliexpress.us/item/3256808040042288.html?spm=a2g0o.productlist.main.2.7b5d328f2rZ0Kk&algo_pvid=4e296762-5c0e-459b-b1f6-ba2306fd98c6&algo_exp_id=4e296762-5c0e-459b-b1f6-ba2306fd98c6-1&pdp_ext_f=%7B"order"%3A"30"%2C"eval"%3A"1"%7D&pdp_npi=4%40dis%21USD%2110.51%213.69%21%21%2175.16%2126.43%21%40210337c117496162516362210eb7d4%2112000044297086886%21sea%21US%216330817038%21X&curPageLogUid=oRgrVCWBuHse&utparam-url=scene%3Asearch%7Cquery_from%3A                                                                                                                                                                                                                                                                                        |
| Switches x110         | 23.6   | https://www.amazon.com/KPREPUBLIC-Princess-Tactile-Mechanical-Keyboard/dp/B0C533CCXY?th=1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Key Caps              | 29.99  | https://www.amazon.com/Sumgsn-Spacebar-Switches-Mechanical-Keyboard/dp/B0BNN2M9QD/?_encoding=UTF8&pd_rd_w=Owgs7&content-id=amzn1.sym.255b3518-6e7f-495c-8611-30a58648072e%3Aamzn1.symc.a68f4ca3-28dc-4388-a2cf-24672c480d8f&pf_rd_p=255b3518-6e7f-495c-8611-30a58648072e&pf_rd_r=SR0ZSF2C3SRVJ6WBDXZ4&pd_rd_wg=cmrkw&pd_rd_r=99deb115-383c-4166-b5aa-908d03b4ab75&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1                                                                                                                                                                                                                                                                                                                                                |
| Stabilizers           | 5.54   | https://www.aliexpress.us/item/3256801499984864.html?spm=a2g0o.productlist.main.2.5e802Ptr2PtrTU&algo_pvid=894e96cb-5856-42ec-b70d-f3d1f1ab610d&algo_exp_id=894e96cb-5856-42ec-b70d-f3d1f1ab610d-1&pdp_ext_f=%7B"order"%3A"111"%2C"eval"%3A"1"%7D&pdp_npi=4%40dis%21USD%215.54%215.54%21%21%215.54%215.54%21%40210318e817496929936517433e29c3%2112000017133740376%21sea%21US%216330817038%21X&curPageLogUid=4ANDMTxK2PfM&utparam-url=scene%3Asearch%7Cquery_from%3A                                                                                                                                                                                                                                                                                          |
| Cable                 | 2.59   | https://www.amazon.com/FEMORO-Monitor-Display-Transfer-Thunderbolt/dp/B0F23ZT4LV/ref=sr_1_9?crid=2ZKUO80E5SP4L&dib=eyJ2IjoiMSJ9.a99dA3Xkjh7kuCLJPGQ2w054v8sE_aP7os6HZe7ytSPJiTMGqsE7HuaqPAtd1a3zuaMVoQJrTKKsrSQHJpsi8vS-W7E6vbY89hHuhvpkfkeG4o6GhmpTfCiDUu-5lZSol22VuA1Ba0a5nhJrrq8EP_EZwHwvoMC1stC9nnUkoIQQTduGNrMQYjUpZbl7L0n7ey4Yf4511wipaNn38RS3PkKullkE1e1DvtnHBdEws-8h8J8aPsmIx5VRWdyiVi7A3NyJ_uR7ZrmGwf51hGABbnt-1DGXWqk3uVoJZLORkWA.jJ-LFd0boDIYZOtuu-53lBCiVccYsCGkF-oIuI3DvOs&dib_tag=se&keywords=usb+c+cable+6ft+data&qid=1749609642&s=industrial&sprefix=usb+c+cable+6ft+data%2Cindustrial%2C81&sr=1-9                                                                                                                                           |
| PCB                   | 73.05  | JLC PCB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Diodes                | 1.39   | idk how to link it since its in dollar express                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Right Angle Pogo Pins | 6.04   | https://www.aliexpress.us/item/3256807268443322.html?spm=a2g0o.cart.0.0.3ba038dahY2nVH&mp=1&pdp_npi=5%40dis%21USD%21USD%206.04%21USD%206.04%21%21USD%205.47%21%21%21%402101ef5e17496929103664858e21ef%2112000040826212953%21ct%21US%216330817038%21%211%210&_gl=1*4pbm4g*_gcl_aw*R0NMLjE3NDM2NTYyOTYuQ2p3S0NBand3TE9fQmhCMkVpd0F4MmUtMzhTVXhwSnVVaFY3RDJGTEt4dHVKa3pZa1FfMXBDelhMN3dDNEpjNjlwWkxjUUIzc19PMVNob0NsdzRRQXZEX0J3RQ..*_gcl_dc*R0NMLjE3NDM2NTYyOTYuQ2p3S0NBand3TE9fQmhCMkVpd0F4MmUtMzhTVXhwSnVVaFY3RDJGTEt4dHVKa3pZa1FfMXBDelhMN3dDNEpjNjlwWkxjUUIzc19PMVNob0NsdzRRQXZEX0J3RQ..*_gcl_au*ODM0OTgyNzI4LjE3NDkxODQwOTI.*_ga*MTY5NzgyMzkxMS4xNzQ5MTg0MDky*_ga_VED1YSGNC7*czE3NDk2OTI1MTckbzgkZzEkdDE3NDk2OTI5MDkkajU5JGwwJGgw&gatewayAdapt=glo2usa    |
| Schottky Diode        | 4.65   | https://www.aliexpress.us/item/3256803563924504.html?spm=a2g0o.detail.0.0.4761scYYscYYhd&mp=1&pdp_npi=5%40dis%21USD%21USD%204.65%21USD%204.65%21%21USD%204.22%21%21%21%402101c59817496929409135558e8112%2112000027034712557%21ct%21US%216330817038%21%211%210&_gl=1*147gwp3*_gcl_aw*R0NMLjE3NDM2NTYyOTYuQ2p3S0NBand3TE9fQmhCMkVpd0F4MmUtMzhTVXhwSnVVaFY3RDJGTEt4dHVKa3pZa1FfMXBDelhMN3dDNEpjNjlwWkxjUUIzc19PMVNob0NsdzRRQXZEX0J3RQ..*_gcl_dc*R0NMLjE3NDM2NTYyOTYuQ2p3S0NBand3TE9fQmhCMkVpd0F4MmUtMzhTVXhwSnVVaFY3RDJGTEt4dHVKa3pZa1FfMXBDelhMN3dDNEpjNjlwWkxjUUIzc19PMVNob0NsdzRRQXZEX0J3RQ..*_gcl_au*ODM0OTgyNzI4LjE3NDkxODQwOTI.*_ga*MTY5NzgyMzkxMS4xNzQ5MTg0MDky*_ga_VED1YSGNC7*czE3NDk2OTI1MTckbzgkZzEkdDE3NDk2OTI5NTYkajEyJGwwJGgw&gatewayAdapt=glo2usa |
| 8x M3 Heat Set Insert | N/A    | Already have                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 4x M3 x 20mm Screw    | N/A    | Already have                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 4x M3 x 12mm Screw    | N/A    | Already have                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PLA Filament          | N/A    | Already have                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| TPU Filament          | N/A    | Already have                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Total:                | 148.84 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
