# Nozzle_Probe_RP2040_and_HX711
Nozzle Probe using Load Cell + HX711 + RP2040 This project implements a simple, reliable probing system for 3D printers, where the nozzle itself acts as the probe
Instead of relying on BLTouch, inductive sensors, or microswitches, this design uses an off-the-shelf load cell with HX711 amplifier connected to an RP2040 microcontroller running CircuitPython.

When the nozzle touches the print bed, the load cell detects the contact force and signals the printer firmware (Klipper) through a GPIO pin. This allows accurate Z-homing and bed leveling with minimal hardware and no extra moving parts.

Features:

Direct nozzle contact = highly accurate probing

Works with Klipper via GPIO trigger

Uses inexpensive, off-the-shelf hardware (HX711 + load cell + RP2040)

Runs on lightweight CircuitPython firmware

Simple wiring and setup

Use Case:
Designed for custom 3D printers that need a reliable and low-cost probing method without the complexity of mechanical or optical probes.

📹 Demo/Setup Video

👉 (Insert YouTube link here)

---------------------------------RP2040 micropython setup----------------------------------

https://www.waveshare.com/wiki/RP2040-Zero#Flash_Firmware
Firmware file is in the repo.
How to download the firmware library for RP2040/RP2350 in windows:- 
After connecting to the computer, press the BOOT key and the RESET key at the same time, release the RESET key first and then release the BOOT key, a removable disk will appear on the computer, copy the firmware library into it 
