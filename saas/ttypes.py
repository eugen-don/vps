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


class Cmd:
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
   - id
   - ipv4
   - ipv4_netmask
   - ipv4_gateway
   - password
   - os
   - hd
   - ram
   - cpu
   - host_id
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'id', None, None, ), # 1
    (2, TType.I64, 'ipv4', None, None, ), # 2
    (3, TType.I64, 'ipv4_netmask', None, None, ), # 3
    (4, TType.I64, 'ipv4_gateway', None, None, ), # 4
    (5, TType.STRING, 'password', None, None, ), # 5
    (6, TType.I64, 'os', None, None, ), # 6
    (7, TType.I16, 'hd', None, None, ), # 7
    (8, TType.I64, 'ram', None, None, ), # 8
    (9, TType.I16, 'cpu', None, None, ), # 9
    (10, TType.I64, 'host_id', None, None, ), # 10
  )

  def __init__(self, id=None, ipv4=None, ipv4_netmask=None, ipv4_gateway=None, password=None, os=None, hd=None, ram=None, cpu=None, host_id=None,):
    self.id = id
    self.ipv4 = ipv4
    self.ipv4_netmask = ipv4_netmask
    self.ipv4_gateway = ipv4_gateway
    self.password = password
    self.os = os
    self.hd = hd
    self.ram = ram
    self.cpu = cpu
    self.host_id = host_id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.ipv4 = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.ipv4_netmask = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.ipv4_gateway = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.password = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.os = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I16:
          self.hd = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.ram = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I16:
          self.cpu = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I64:
          self.host_id = iprot.readI64();
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
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 1)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    if self.ipv4 is not None:
      oprot.writeFieldBegin('ipv4', TType.I64, 2)
      oprot.writeI64(self.ipv4)
      oprot.writeFieldEnd()
    if self.ipv4_netmask is not None:
      oprot.writeFieldBegin('ipv4_netmask', TType.I64, 3)
      oprot.writeI64(self.ipv4_netmask)
      oprot.writeFieldEnd()
    if self.ipv4_gateway is not None:
      oprot.writeFieldBegin('ipv4_gateway', TType.I64, 4)
      oprot.writeI64(self.ipv4_gateway)
      oprot.writeFieldEnd()
    if self.password is not None:
      oprot.writeFieldBegin('password', TType.STRING, 5)
      oprot.writeString(self.password)
      oprot.writeFieldEnd()
    if self.os is not None:
      oprot.writeFieldBegin('os', TType.I64, 6)
      oprot.writeI64(self.os)
      oprot.writeFieldEnd()
    if self.hd is not None:
      oprot.writeFieldBegin('hd', TType.I16, 7)
      oprot.writeI16(self.hd)
      oprot.writeFieldEnd()
    if self.ram is not None:
      oprot.writeFieldBegin('ram', TType.I64, 8)
      oprot.writeI64(self.ram)
      oprot.writeFieldEnd()
    if self.cpu is not None:
      oprot.writeFieldBegin('cpu', TType.I16, 9)
      oprot.writeI16(self.cpu)
      oprot.writeFieldEnd()
    if self.host_id is not None:
      oprot.writeFieldBegin('host_id', TType.I64, 10)
      oprot.writeI64(self.host_id)
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

class Task:
  """
  Attributes:
   - cmd
   - id
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'cmd', None,     0, ), # 1
    (2, TType.I64, 'id', None, None, ), # 2
  )

  def __init__(self, cmd=thrift_spec[1][4], id=None,):
    self.cmd = cmd
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
      if fid == 1:
        if ftype == TType.I32:
          self.cmd = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.id = iprot.readI64();
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
    oprot.writeStructBegin('Task')
    if self.cmd is not None:
      oprot.writeFieldBegin('cmd', TType.I32, 1)
      oprot.writeI32(self.cmd)
      oprot.writeFieldEnd()
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 2)
      oprot.writeI64(self.id)
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

class SaasException(TException):
  """
  Attributes:
   - state
   - message
   - host_id
   - todo
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'state', None, None, ), # 1
    (2, TType.STRING, 'message', None, None, ), # 2
    (3, TType.I64, 'host_id', None, None, ), # 3
    (4, TType.STRUCT, 'todo', (Task, Task.thrift_spec), None, ), # 4
  )

  def __init__(self, state=None, message=None, host_id=None, todo=None,):
    self.state = state
    self.message = message
    self.host_id = host_id
    self.todo = todo

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.state = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.host_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.todo = Task()
          self.todo.read(iprot)
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
    oprot.writeStructBegin('SaasException')
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I32, 1)
      oprot.writeI32(self.state)
      oprot.writeFieldEnd()
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 2)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.host_id is not None:
      oprot.writeFieldBegin('host_id', TType.I64, 3)
      oprot.writeI64(self.host_id)
      oprot.writeFieldEnd()
    if self.todo is not None:
      oprot.writeFieldBegin('todo', TType.STRUCT, 4)
      self.todo.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)