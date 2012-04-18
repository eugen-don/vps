#
# Autogenerated by Thrift Compiler (0.8.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Action:
  NONE = 0
  OPEN = 1
  CLOSE = 2
  RESTART = 3

  _VALUES_TO_NAMES = {
    0: "NONE",
    1: "OPEN",
    2: "CLOSE",
    3: "RESTART",
  }

  _NAMES_TO_VALUES = {
    "NONE": 0,
    "OPEN": 1,
    "CLOSE": 2,
    "RESTART": 3,
  }


class Vps:
  """
  Attributes:
   - host_id
   - id
   - ipv4
   - ipv4_netmask
   - ipv4_gateway
   - password
   - os
   - hd
   - ram
   - cpu
  """

  thrift_spec = None
  def __init__(self, host_id=None, id=None, ipv4=None, ipv4_netmask=None, ipv4_gateway=None, password=None, os=None, hd=None, ram=None, cpu=None,):
    self.host_id = host_id
    self.id = id
    self.ipv4 = ipv4
    self.ipv4_netmask = ipv4_netmask
    self.ipv4_gateway = ipv4_gateway
    self.password = password
    self.os = os
    self.hd = hd
    self.ram = ram
    self.cpu = cpu

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == -1:
        if ftype == TType.I32:
          self.host_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.I32:
          self.id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.ipv4 = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.ipv4_netmask = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.ipv4_gateway = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.password = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.os = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I16:
          self.hd = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.ram = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I16:
          self.cpu = iprot.readI16();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Vps')
    if self.host_id is not None:
      oprot.writeFieldBegin('host_id', TType.I32, -1)
      oprot.writeI32(self.host_id)
      oprot.writeFieldEnd()
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I32, 1)
      oprot.writeI32(self.id)
      oprot.writeFieldEnd()
    if self.ipv4 is not None:
      oprot.writeFieldBegin('ipv4', TType.I32, 2)
      oprot.writeI32(self.ipv4)
      oprot.writeFieldEnd()
    if self.ipv4_netmask is not None:
      oprot.writeFieldBegin('ipv4_netmask', TType.I32, 3)
      oprot.writeI32(self.ipv4_netmask)
      oprot.writeFieldEnd()
    if self.ipv4_gateway is not None:
      oprot.writeFieldBegin('ipv4_gateway', TType.I32, 4)
      oprot.writeI32(self.ipv4_gateway)
      oprot.writeFieldEnd()
    if self.password is not None:
      oprot.writeFieldBegin('password', TType.STRING, 5)
      oprot.writeString(self.password)
      oprot.writeFieldEnd()
    if self.os is not None:
      oprot.writeFieldBegin('os', TType.I32, 6)
      oprot.writeI32(self.os)
      oprot.writeFieldEnd()
    if self.hd is not None:
      oprot.writeFieldBegin('hd', TType.I16, 7)
      oprot.writeI16(self.hd)
      oprot.writeFieldEnd()
    if self.ram is not None:
      oprot.writeFieldBegin('ram', TType.I32, 8)
      oprot.writeI32(self.ram)
      oprot.writeFieldEnd()
    if self.cpu is not None:
      oprot.writeFieldBegin('cpu', TType.I16, 9)
      oprot.writeI16(self.cpu)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Todo:
  """
  Attributes:
   - action
   - id
  """

  thrift_spec = None
  def __init__(self, action=None, id=None,):
    self.action = action
    self.id = id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == -1:
        if ftype == TType.I32:
          self.action = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.I32:
          self.id = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Todo')
    if self.action is not None:
      oprot.writeFieldBegin('action', TType.I32, -1)
      oprot.writeI32(self.action)
      oprot.writeFieldEnd()
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I32, 1)
      oprot.writeI32(self.id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
