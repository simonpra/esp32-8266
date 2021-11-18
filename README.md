# ESP8266 micropython

**Somme usefull docs & scripts to install and develop for the ESP8266 / ESP32 using micropython.**

## VSCODE integration

I do want to do everything from the VSCODE IDE and terminal.

#### Prerequisite

> [\*] VSCODE
> [\*] Python 3 with PIP

#### Installation

**Rshell**
[https://github.com/dhylands/rshell](https://github.com/dhylands/rshell)
To communicate directly with the module ESP8266 / ESP32, giving an interactive shell for micropython.

```
pip install rshell
```

**Ampy**
[https://github.com/scientifichackers/ampy](https://github.com/scientifichackers/ampy)
An Adafruit extension to manipulate files on the module ESP8266 / ESP32.

```
pip install adafruit-ampy
```

**Micropython IDE**
[https://github.com/dphans/micropython-ide-vscode](https://github.com/dphans/micropython-ide-vscode)
Plugin for VSCODE that automate the syncing between your folder and the module ESP8266 / ESP32, and let you install micropython using `esptool.py`.

```
search for Micropython IDE in VSCODE
```

**micropy-cli**
[https://github.com/BradenM/micropy-cli](https://github.com/BradenM/micropy-cli)
Usefull to have IntelliSense & Linting specific to micropython into the IDE. It also include a dependency management system specific to micropython.

```
pip install --upgrade micropy-cli
```

## Ref.

[https://lemariva.com/blog/2019/08/micropython-vsc-ide-intellisense](https://lemariva.com/blog/2019/08/micropython-vsc-ide-intellisense)
[https://lemariva.com/blog/2018/03/tutorial-installing-dependencies-on-micropython](https://lemariva.com/blog/2018/03/tutorial-installing-dependencies-on-micropython)
ESP8266 micropython firmware
[https://docs.micropython.org/en/latest/tutorial/intro.html#intro](https://docs.micropython.org/en/latest/tutorial/intro.html#intro)
Webserver
[https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/](https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/)
I2C for sensor
[https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-main](https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-main)
[https://docs.micropython.org/en/latest/library/machine.I2C.html](https://docs.micropython.org/en/latest/library/machine.I2C.html)
MCP9808 temperature sensor Datasheet
[https://cdn-shop.adafruit.com/datasheets/MCP9808.pdf](https://cdn-shop.adafruit.com/datasheets/MCP9808.pdf)