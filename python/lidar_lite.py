import smbus2 as smbus
import time

class Lidar_Lite():
  def __init__(self):
    self.address = 0x62
    self.measureCount = 0
    self.distWriteReg = 0x00
    self.distWriteVal = 0x03
    self.distWriteRBC = 0x04
    self.distReadReg1 = 0x0f
    self.distReadReg2 = 0x10
    self.velWriteReg = 0x04
    self.velWriteVal = 0x08
    self.velReadReg = 0x09

  def connect(self, bus):
    try:
      self.bus = smbus.SMBus(bus)
      time.sleep(0.5)
      return 0
    except:
      return -1

  def writeAndWait(self, register, value):
    self.bus.write_byte_data(self.address, register, value);
    time.sleep(0.02)

  def readAndWait(self, register):
    self.bus.write_byte(self.address, register)
    res = self.bus.read_byte(self.address)
    # time.sleep(0.02)
    return res

  def getDistance(self):
    if self.measureCount % 100 == 0:
        self.writeAndWait(self.distWriteReg, self.distWriteRBC)
    else:
        self.writeAndWait(self.distWriteReg, self.distWriteVal)
    dist1 = self.readAndWait(self.distReadReg1)
    dist2 = self.readAndWait(self.distReadReg2)
    self.count += 1
    return (dist1 << 8) + dist2

  def getVelocity(self):
    # Not true velocity, just difference between current distance and previous distance.
    # Use free running mode to get a proper velocity measurement.
    # (i.e. free running mode at 10 Hz results in velocity measurements in 0.1 m/s)
    self.getDistance(self)
    self.writeAndWait(self.velWriteReg, self.velWriteVal)
    vel = self.readAndWait(self.velReadReg)
    return self.signedInt(vel)

  def signedInt(self, value):
    if value > 127:
      return (256-value) * (-1)
    else:
      return value


