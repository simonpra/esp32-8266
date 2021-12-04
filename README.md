# ESP8266 micropython

**Somme usefull docs & scripts to install and develop for the ESP8266 / ESP32 using micropython.**

## VSCODE integration

I do want to do everything from the VSCODE IDE and terminal.

### Prerequisite

> [\*] VSCODE <br>
> [\*] Python 3 with PIP <small>_(< 3.10 because rshell doesn't support it)_</small>

<br><br>
## Installation

**Rshell**<br>
[https://github.com/dhylands/rshell](https://github.com/dhylands/rshell)<br>
To communicate directly with the module ESP8266 / ESP32, giving an interactive shell for micropython.

```
pip install rshell
```

**Ampy**<br>
[https://github.com/scientifichackers/ampy](https://github.com/scientifichackers/ampy)<br>
An Adafruit extension to manipulate files on the module ESP8266 / ESP32.

```
pip install adafruit-ampy
```

**micropy-cli**<br>
[https://github.com/BradenM/micropy-cli](https://github.com/BradenM/micropy-cli)<br>
Usefull to have IntelliSense & Linting specific to micropython into the IDE. It also include a dependency management system specific to micropython.

```
pip install --upgrade micropy-cli
```

and then searching for stubs using micropy : <small>_(change `esp32` with `esp8266` depending on your chip)_</small>

```
micropy stubs search esp32
```
```
    MicroPy  Searching Stub Repositories...

    MicroPy  Results for esp32:
    MicroPy  esp32-micropython-1.10.0
    MicroPy  esp32-micropython-1.11.0
    MicroPy  esp32-micropython-1.12.0
    MicroPy  esp32-micropython-1.15.0
    MicroPy  esp32-micropython-1.9.4
```

Installing the stubs for the ESP32 : <small>_(change `esp32` with `esp8266` depending on your chip)_</small>

```
micropy stubs add esp32-micropython-1.15.0
```

Now is time to init ^^<br>
(this will create a `.micropy` folder containing the stubs and a folder for dependecies)

```
micropy init
```
<img src="_docs\imgs\micropy-init.jpg">

After closing and reopening VScode, you could be ask to install or activate some other extensions (pyLint, Intellisense, ...)

<br><br>
## USB installation

Make sur to have the good USBtoUART driver. Check the USB chip on your board for ID reference.

<img src="_docs\imgs\usb_chip_silicon-labs.jpg">

Here is the 2104 from SiliconLabs. You can download and install VCP Drivers for SiliconLabs Chips 210x on https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers

<br><br>
## Getting the port

**Windows** <br>
In the Device Manager, it should appear under _ports_

<img src="_docs\imgs\peripherals-ports.jpg"><br>
_COM3 in this case_

**Mac OSX / Linux**<br>
List the ports in /_dev_/ and search for the one(s) containing [SLAB_USBtoUART]

```
ls /dev/*SLAB*
```

In my case its **/dev/cu.SLAB_USBtoUART**

<br><br>
## Firmeware

**MicroPython**<br>
get the latest micropython firmeware for your chip here :<br>
[https://micropython.org/download/](https://micropython.org/download/)

> you can get informations about your chip using **esptool.py**<br>
> it will scan different USB port and give you the correct port to use later
```
./esptool.py flash_id
```

**[esptool.py](https://github.com/espressif/esptool)**<br>
esptool let you manipulate different ESP chips.<br>
You can get infos about your chip using :

> - _(remember to change the port to yours)_<br>
> - _(change `esp32` with `esp32c3` or `esp8266` or `...` depending on your chip)_
> - _CHANGE the BINARY filename ACCORDING to YOURS !_

```
./esptool.py flash_id
```

Before installing micropython on the chip, make sur to erase it : _(remember to change the port to yours)_

```
./esptool.py --chip esp32 --baud 115200 --port /dev/cu.SLAB_USBtoUART erase_flash
```
And finaly you can upload the firmeware for micropython into the chip :

```
./esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART --baud 460800 write_flash -z 0x1000 esp32-20210902-v1.17.bin
```
> if your chip is an ESP32-**C3**, it need to write the flash starting @ 0x00 !! <br>
> => [https://community.m5stack.com/topic/3733/micropython-on-m5stamp-c3](https://community.m5stack.com/topic/3733/micropython-on-m5stamp-c3) <br>
> => [https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/bootloader.html](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/bootloader.html)

```
./esptool.py -p COMx -b 1000000 --before default_reset erase_flash

./esptool.py -p COMx -b 1500000 --before default_reset write_flash -z 0x0 esp32c3-20210902-v1.17.bin
```

<br><br>
## Ref.

[https://lemariva.com/blog/2019/08/micropython-vsc-ide-intellisense](https://lemariva.com/blog/2019/08/micropython-vsc-ide-intellisense)<br>
[https://lemariva.com/blog/2018/03/tutorial-installing-dependencies-on-micropython](https://lemariva.com/blog/2018/03/tutorial-installing-dependencies-on-micropython)

USB Driver for M5stack<br>
[https://github.com/Xinyuan-LilyGO/LilyGo-T-Call-SIM800/issues/139#issuecomment-904390716](https://github.com/Xinyuan-LilyGO/LilyGo-T-Call-SIM800/issues/139#issuecomment-904390716)

Micropython firmware<br>
[https://micropython.org/download/](https://micropython.org/download/)

Webserver<br>
[https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/](https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/)

I2C for sensor<br>
[https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-main](https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-main)<br>
[https://docs.micropython.org/en/latest/library/machine.I2C.html](https://docs.micropython.org/en/latest/library/machine.I2C.html)

MCP9808 temperature sensor Datasheet<br>
[https://cdn-shop.adafruit.com/datasheets/MCP9808.pdf](https://cdn-shop.adafruit.com/datasheets/MCP9808.pdf)