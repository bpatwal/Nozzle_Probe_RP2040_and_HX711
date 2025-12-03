# Nozzle_Probe_RP2040_and_HX711
Nozzle Probe using Load Cell + HX711 + RP2040 This project implements a simple, reliable probing system for 3D printers, where the nozzle itself acts as the probe
Instead of relying on BLTouch, inductive sensors, or microswitches, this design uses an off-the-shelf load cell with HX711 amplifier connected to an RP2040 microcontroller running CircuitPython.

When the nozzle touches the print bed, the load cell detects the contact force and signals the printer firmware (Klipper) through a GPIO pin. This allows accurate Z-homing and bed leveling with minimal hardware and no extra moving parts.

## Features:

Direct nozzle contact = highly accurate probing

Works with Klipper via GPIO trigger

Uses inexpensive, off-the-shelf hardware (HX711 + load cell + RP2040)

Runs on lightweight CircuitPython firmware

Simple wiring and setup

## Use Case:
Designed for custom 3D printers that need a reliable and low-cost probing method without the complexity of mechanical or optical probes.

## Part List / BOM
### Electronic hardware required:
- 1x RP2040-Zero Microcontroller [aliexpress](https://de.aliexpress.com/item/1005008738491752.html?spm=a2g0o.productlist.main.4.36187ad7kNz51F&aem_p4p_detail=202512030315101422183467135040001165774&algo_pvid=1d2c2777-12ae-4727-a041-9ae23e20b267&algo_exp_id=1d2c2777-12ae-4727-a041-9ae23e20b267-3&pdp_ext_f=%7B%22order%22%3A%22103%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21EUR%212.55%212.55%21%21%2120.46%2120.46%21%40211b612817647605102062844ebea4%2112000046469133178%21sea%21DE%214721848451%21X%211%210%21n_tag%3A-29919%3Bd%3Aaa28fb7f%3Bm03_new_user%3A-29895&curPageLogUid=cYBmaCTgJfim&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005008738491752%7C_p_origin_prod%3A&search_p4p_id=202512030315101422183467135040001165774_2)
- 2x HX711AD circuit board for loadcell + 2x 5kg Loadcell aluminium [aliexpress](https://de.aliexpress.com/item/1005006824220368.html?spm=a2g0o.productlist.main.1.4df83cd12nl2vJ&aem_p4p_detail=2025120303142317607648952630440001624976&algo_pvid=48cde8e7-0453-427e-a971-4be0ab53d8ee&algo_exp_id=48cde8e7-0453-427e-a971-4be0ab53d8ee-0&pdp_ext_f=%7B%22order%22%3A%22271%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21EUR%211.02%210.94%21%21%218.18%217.54%21%40211b612817647604639121706ebea4%2112000038424399891%21sea%21DE%214721848451%21X%211%210%21n_tag%3A-29919%3Bd%3Aaa28fb7f%3Bm03_new_user%3A-29895%3BpisId%3A5000000194150333&curPageLogUid=iW1lWNou6C29&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006824220368%7C_p_origin_prod%3A&search_p4p_id=2025120303142317607648952630440001624976_1)
- 1x " 4-channel bidirectional logic level converter (also called a level shifter)" (identified by chatGPT, idk if that is correct) [aliexpress](https://de.aliexpress.com/item/1005009794388281.html?spm=a2g0o.productlist.main.6.582d24adkpbr1B&algo_pvid=27881e1c-5a4c-4c66-8b79-74edf6a75c41&algo_exp_id=27881e1c-5a4c-4c66-8b79-74edf6a75c41-5&pdp_ext_f=%7B%22order%22%3A%2258%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21EUR%211.79%210.99%21%21%2114.35%217.93%21%4021038df617647598075934604ef98d%2112000051519092574%21sea%21DE%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Aaa28fb7f%3Bm03_new_user%3A-29895%3BpisId%3A5000000187464813&curPageLogUid=lHpii6LRNog7&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009794388281%7C_p_origin_prod%3A)

### Additional/Recommended:
- cables to connect everything [5 pin flatband cable](https://de.aliexpress.com/item/1005001915248222.html?spm=a2g0o.order_list.order_list_main.29.21875c5fE93KKg&gatewayAdapt=glo2deu)
- jst xh 5 pin connector for bl_touch sensor input on board [aliexpress](https://de.aliexpress.com/item/1005007460897865.html?spm=a2g0o.order_list.order_list_main.23.21875c5fE93KKg&gatewayAdapt=glo2deu)

### Tools:
- usb-c data cable to flash RP zero from computer (!most usb-A to usb-C cables are not data cables, only power cables!)
- soldering iron


## 📹 Demo/Setup Video
👉 (https://youtu.be/r3Bz-Iza5p8)


---------------------------------RP2040 micropython setup----------------------------------

https://www.waveshare.com/wiki/RP2040-Zero#Flash_Firmware
Firmware file is in the repo Nozzle_Probe_RP2040_and_HX711.
How to download the firmware library for RP2040/RP2350 in windows:- 
After connecting to the computer, press the BOOT key and the RESET key at the same time, release the RESET key first and then release the BOOT key, a removable disk will appear on the computer, copy the firmware library into it 
