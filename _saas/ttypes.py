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


class CMD:
  NONE = 0
  OPEN = 1
  CLOSE = 2
  REBOOT = 3
  RM = 4
  BANDWIDTH = 5
  OS = 6
  UPGRADE = 7
  MIGRATE = 8
  MONITOR = 9
  PRE_SYNC = 10
  RESET_PW = 11

  _VALUES_TO_NAMES = {
    0: "NONE",
    1: "OPEN",
    2: "CLOSE",
    3: "REBOOT",
    4: "RM",
    5: "BANDWIDTH",
    6: "OS",
    7: "UPGRADE",
    8: "MIGRATE",
    9: "MONITOR",
    10: "PRE_SYNC",
    11: "RESET_PW",
  }

  _NAMES_TO_VALUES = {
    "NONE": 0,
    "OPEN": 1,
    "CLOSE": 2,
    "REBOOT": 3,
    "RM": 4,
    "BANDWIDTH": 5,
    "OS": 6,
    "UPGRADE": 7,
    "MIGRATE": 8,
    "MONITOR": 9,
    "PRE_SYNC": 10,
    "RESET_PW": 11,
  }


class Ip:
  """
  Attributes:
   - ipv4
   - ipv4_netmask
   - mac
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'ipv4', None, None, ), # 1
    (2, TType.I64, 'ipv4_netmask', None, None, ), # 2
    (3, TType.STRING, 'mac', None, None, ), # 3
  )

  def __init__(self, ipv4=None, ipv4_netmask=None, mac=None,):
    self.ipv4 = ipv4
    self.ipv4_netmask = ipv4_netmask
    self.mac = mac

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
          self.ipv4 = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.ipv4_netmask = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.mac = iprot.readString();
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
    oprot.writeStructBegin('Ip')
    if self.ipv4 is not None:
      oprot.writeFieldBegin('ipv4', TType.I64, 1)
      oprot.writeI64(self.ipv4)
      oprot.writeFieldEnd()
    if self.ipv4_netmask is not None:
      oprot.writeFieldBegin('ipv4_netmask', TType.I64, 2)
      oprot.writeI64(self.ipv4_netmask)
      oprot.writeFieldEnd()
    if self.mac is not None:
      oprot.writeFieldBegin('mac', TType.STRING, 3)
      oprot.writeString(self.mac)
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

class Vps:
  """
  Attributes:
   - id
   - ext_ips
   - gateway
   - password
   - os
   - harddisks
   - ram
   - cpu
   - host_id
   - state
   - int_ip
   - bandwidth
   - qos
   - template_image
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'id', None, None, ), # 1
    (2, TType.LIST, 'ext_ips', (TType.STRUCT,(Ip, Ip.thrift_spec)), None, ), # 2
    (3, TType.STRUCT, 'gateway', (Ip, Ip.thrift_spec), None, ), # 3
    (4, TType.STRING, 'password', None, None, ), # 4
    (5, TType.I32, 'os', None, None, ), # 5
    (6, TType.MAP, 'harddisks', (TType.I32,None,TType.I32,None), None, ), # 6
    (7, TType.I64, 'ram', None, None, ), # 7
    (8, TType.I16, 'cpu', None, None, ), # 8
    (9, TType.I64, 'host_id', None, None, ), # 9
    (10, TType.I16, 'state', None, None, ), # 10
    (11, TType.STRUCT, 'int_ip', (Ip, Ip.thrift_spec), None, ), # 11
    (12, TType.DOUBLE, 'bandwidth', None, None, ), # 12
    (13, TType.I32, 'qos', None, None, ), # 13
    (14, TType.STRING, 'template_image', None, None, ), # 14
  )

  def __init__(self, id=None, ext_ips=None, gateway=None, password=None, os=None, harddisks=None, ram=None, cpu=None, host_id=None, state=None, int_ip=None, bandwidth=None, qos=None, template_image=None,):
    self.id = id
    self.ext_ips = ext_ips
    self.gateway = gateway
    self.password = password
    self.os = os
    self.harddisks = harddisks
    self.ram = ram
    self.cpu = cpu
    self.host_id = host_id
    self.state = state
    self.int_ip = int_ip
    self.bandwidth = bandwidth
    self.qos = qos
    self.template_image = template_image

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
        if ftype == TType.LIST:
          self.ext_ips = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = Ip()
            _elem5.read(iprot)
            self.ext_ips.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.gateway = Ip()
          self.gateway.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.password = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.os = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.MAP:
          self.harddisks = {}
          (_ktype7, _vtype8, _size6 ) = iprot.readMapBegin() 
          for _i10 in xrange(_size6):
            _key11 = iprot.readI32();
            _val12 = iprot.readI32();
            self.harddisks[_key11] = _val12
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.ram = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I16:
          self.cpu = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I64:
          self.host_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I16:
          self.state = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.STRUCT:
          self.int_ip = Ip()
          self.int_ip.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.DOUBLE:
          self.bandwidth = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.I32:
          self.qos = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.STRING:
          self.template_image = iprot.readString();
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
    if self.ext_ips is not None:
      oprot.writeFieldBegin('ext_ips', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.ext_ips))
      for iter13 in self.ext_ips:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.gateway is not None:
      oprot.writeFieldBegin('gateway', TType.STRUCT, 3)
      self.gateway.write(oprot)
      oprot.writeFieldEnd()
    if self.password is not None:
      oprot.writeFieldBegin('password', TType.STRING, 4)
      oprot.writeString(self.password)
      oprot.writeFieldEnd()
    if self.os is not None:
      oprot.writeFieldBegin('os', TType.I32, 5)
      oprot.writeI32(self.os)
      oprot.writeFieldEnd()
    if self.harddisks is not None:
      oprot.writeFieldBegin('harddisks', TType.MAP, 6)
      oprot.writeMapBegin(TType.I32, TType.I32, len(self.harddisks))
      for kiter14,viter15 in self.harddisks.items():
        oprot.writeI32(kiter14)
        oprot.writeI32(viter15)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.ram is not None:
      oprot.writeFieldBegin('ram', TType.I64, 7)
      oprot.writeI64(self.ram)
      oprot.writeFieldEnd()
    if self.cpu is not None:
      oprot.writeFieldBegin('cpu', TType.I16, 8)
      oprot.writeI16(self.cpu)
      oprot.writeFieldEnd()
    if self.host_id is not None:
      oprot.writeFieldBegin('host_id', TType.I64, 9)
      oprot.writeI64(self.host_id)
      oprot.writeFieldEnd()
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I16, 10)
      oprot.writeI16(self.state)
      oprot.writeFieldEnd()
    if self.int_ip is not None:
      oprot.writeFieldBegin('int_ip', TType.STRUCT, 11)
      self.int_ip.write(oprot)
      oprot.writeFieldEnd()
    if self.bandwidth is not None:
      oprot.writeFieldBegin('bandwidth', TType.DOUBLE, 12)
      oprot.writeDouble(self.bandwidth)
      oprot.writeFieldEnd()
    if self.qos is not None:
      oprot.writeFieldBegin('qos', TType.I32, 13)
      oprot.writeI32(self.qos)
      oprot.writeFieldEnd()
    if self.template_image is not None:
      oprot.writeFieldBegin('template_image', TType.STRING, 14)
      oprot.writeString(self.template_image)
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

class Host:
  """
  Attributes:
   - id
   - ext_ip
   - int_ip
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'id', None, None, ), # 1
    (2, TType.I64, 'ext_ip', None, None, ), # 2
    (3, TType.I64, 'int_ip', None, None, ), # 3
  )

  def __init__(self, id=None, ext_ip=None, int_ip=None,):
    self.id = id
    self.ext_ip = ext_ip
    self.int_ip = int_ip

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
          self.ext_ip = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.int_ip = iprot.readI64();
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
    oprot.writeStructBegin('Host')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 1)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    if self.ext_ip is not None:
      oprot.writeFieldBegin('ext_ip', TType.I64, 2)
      oprot.writeI64(self.ext_ip)
      oprot.writeFieldEnd()
    if self.int_ip is not None:
      oprot.writeFieldBegin('int_ip', TType.I64, 3)
      oprot.writeI64(self.int_ip)
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

class MigrateTask:
  """
  Attributes:
   - id
   - vps_id
   - from_host_id
   - to_host_id
   - to_host_ip
   - new_ext_ips
   - new_int_ip
   - new_gateway
   - bandwidth
   - state
   - speed
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'id', None, None, ), # 1
    (2, TType.I64, 'vps_id', None, None, ), # 2
    (3, TType.I64, 'from_host_id', None, None, ), # 3
    (4, TType.I64, 'to_host_id', None, None, ), # 4
    (5, TType.I64, 'to_host_ip', None, None, ), # 5
    (6, TType.LIST, 'new_ext_ips', (TType.STRUCT,(Ip, Ip.thrift_spec)), None, ), # 6
    (7, TType.STRUCT, 'new_int_ip', (Ip, Ip.thrift_spec), None, ), # 7
    (8, TType.STRUCT, 'new_gateway', (Ip, Ip.thrift_spec), None, ), # 8
    (9, TType.I16, 'bandwidth', None, None, ), # 9
    (10, TType.I16, 'state', None, None, ), # 10
    (11, TType.I16, 'speed', None, None, ), # 11
  )

  def __init__(self, id=None, vps_id=None, from_host_id=None, to_host_id=None, to_host_ip=None, new_ext_ips=None, new_int_ip=None, new_gateway=None, bandwidth=None, state=None, speed=None,):
    self.id = id
    self.vps_id = vps_id
    self.from_host_id = from_host_id
    self.to_host_id = to_host_id
    self.to_host_ip = to_host_ip
    self.new_ext_ips = new_ext_ips
    self.new_int_ip = new_int_ip
    self.new_gateway = new_gateway
    self.bandwidth = bandwidth
    self.state = state
    self.speed = speed

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
          self.vps_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.from_host_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.to_host_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.to_host_ip = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.new_ext_ips = []
          (_etype19, _size16) = iprot.readListBegin()
          for _i20 in xrange(_size16):
            _elem21 = Ip()
            _elem21.read(iprot)
            self.new_ext_ips.append(_elem21)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRUCT:
          self.new_int_ip = Ip()
          self.new_int_ip.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRUCT:
          self.new_gateway = Ip()
          self.new_gateway.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I16:
          self.bandwidth = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I16:
          self.state = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I16:
          self.speed = iprot.readI16();
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
    oprot.writeStructBegin('MigrateTask')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 1)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    if self.vps_id is not None:
      oprot.writeFieldBegin('vps_id', TType.I64, 2)
      oprot.writeI64(self.vps_id)
      oprot.writeFieldEnd()
    if self.from_host_id is not None:
      oprot.writeFieldBegin('from_host_id', TType.I64, 3)
      oprot.writeI64(self.from_host_id)
      oprot.writeFieldEnd()
    if self.to_host_id is not None:
      oprot.writeFieldBegin('to_host_id', TType.I64, 4)
      oprot.writeI64(self.to_host_id)
      oprot.writeFieldEnd()
    if self.to_host_ip is not None:
      oprot.writeFieldBegin('to_host_ip', TType.I64, 5)
      oprot.writeI64(self.to_host_ip)
      oprot.writeFieldEnd()
    if self.new_ext_ips is not None:
      oprot.writeFieldBegin('new_ext_ips', TType.LIST, 6)
      oprot.writeListBegin(TType.STRUCT, len(self.new_ext_ips))
      for iter22 in self.new_ext_ips:
        iter22.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.new_int_ip is not None:
      oprot.writeFieldBegin('new_int_ip', TType.STRUCT, 7)
      self.new_int_ip.write(oprot)
      oprot.writeFieldEnd()
    if self.new_gateway is not None:
      oprot.writeFieldBegin('new_gateway', TType.STRUCT, 8)
      self.new_gateway.write(oprot)
      oprot.writeFieldEnd()
    if self.bandwidth is not None:
      oprot.writeFieldBegin('bandwidth', TType.I16, 9)
      oprot.writeI16(self.bandwidth)
      oprot.writeFieldEnd()
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I16, 10)
      oprot.writeI16(self.state)
      oprot.writeFieldEnd()
    if self.speed is not None:
      oprot.writeFieldBegin('speed', TType.I16, 11)
      oprot.writeI16(self.speed)
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

class NetFlow:
  """
  Attributes:
   - vps_id
   - rx
   - tx
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'vps_id', None, None, ), # 1
    (2, TType.I64, 'rx', None, None, ), # 2
    (3, TType.I64, 'tx', None, None, ), # 3
  )

  def __init__(self, vps_id=None, rx=None, tx=None,):
    self.vps_id = vps_id
    self.rx = rx
    self.tx = tx

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
          self.vps_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.rx = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.tx = iprot.readI64();
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
    oprot.writeStructBegin('NetFlow')
    if self.vps_id is not None:
      oprot.writeFieldBegin('vps_id', TType.I64, 1)
      oprot.writeI64(self.vps_id)
      oprot.writeFieldEnd()
    if self.rx is not None:
      oprot.writeFieldBegin('rx', TType.I64, 2)
      oprot.writeI64(self.rx)
      oprot.writeFieldEnd()
    if self.tx is not None:
      oprot.writeFieldBegin('tx', TType.I64, 3)
      oprot.writeI64(self.tx)
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
