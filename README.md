# ESP8266 micropython

**Somme usefull docs & scripts to install and develop for the ESP8266 / ESP32 using micropython.**

## VSCODE integration

I do want to do everything from the VSCODE IDE and terminal.

### Prerequisite

> [\*] VSCODE <br>
> [\*] Python 3 with PIP

### Installation

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

### USB installation

Make sur to have the good USBtoUART driver.Check the USB chip on your board for ID référence.

<img src="_docs\imgs\usb_chip_silicon-labs.jpg">

Here is the 2104 from SiliconLabs. You can download and install VCP Drivers for SiliconLabs Chips 210x on https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers

### Getting the port

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

## Ref.

[https://lemariva.com/blog/2019/08/micropython-vsc-ide-intellisense](https://lemariva.com/blog/2019/08/micropython-vsc-ide-intellisense)<br>
[https://lemariva.com/blog/2018/03/tutorial-installing-dependencies-on-micropython](https://lemariva.com/blog/2018/03/tutorial-installing-dependencies-on-micropython)

ESP8266 micropython firmware<br>
[https://docs.micropython.org/en/latest/tutorial/intro.html#intro](https://docs.micropython.org/en/latest/tutorial/intro.html#intro)

Webserver<br>
[https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/](https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/)

I2C for sensor<br>
[https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-main](https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-main)<br>
[https://docs.micropython.org/en/latest/library/machine.I2C.html](https://docs.micropython.org/en/latest/library/machine.I2C.html)

MCP9808 temperature sensor Datasheet<br>
[https://cdn-shop.adafruit.com/datasheets/MCP9808.pdf](https://cdn-shop.adafruit.com/datasheets/MCP9808.pdf)