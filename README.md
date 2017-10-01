# Lidar-Lite

## Libraries for interacting with Lidar-Lite over I2C

This library will only work in a linux environment
please install i2c-dev and i2c-tools

For recent Raspberry Pis or if you get an error such as 

`/src/lidar_lite.cpp:36:64: error: ‘i2c_smbus_write_byte_data’ was not declared in this scope`

use this command to install `i2c-dev`:

`apt-get install libi2c-dev`

## Python3 on raspberry pi 
You need to get smbus working. The easiest way to do this is to:
pip install smbus2

I changed the import statement to import smbus2 as smbus.
I also changed the syntax to comply with python3 