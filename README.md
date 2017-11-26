# esp32 projects 
#### Dcoumenting my experince with micro Python and Adafruit ESP32 feather HUZZAH32 mcu

contains micro python code snippets for ESP32 MCU**

** Contents **

1. Connecting the MCU (Linux)

    You need a USB micro cable, make sure it is a data cable and not  a charge only cable, you can save your self from lot of trouble if you  use a good data cable , find [here](https://electronics.stackexchange.com/questions/140225/how-can-i-tell-charge-only-usb-cables-from-usb-data-cables?newreg=126ef6c2fd84421eb8caa4daa15d509e) how to check if a USB cable is data or charge only cable.

    after connecting the mcu board look for devices under /dev/,

    _$ ls -l /dev/tty*_

    genrally if you only connected one mcu board to your linux host then it will  be _/dev/ttyUSB0_

1. Erasing Flash
1. Flasing micro python
1. Hello World
1. Blink onboard LED
1. Controling relay




