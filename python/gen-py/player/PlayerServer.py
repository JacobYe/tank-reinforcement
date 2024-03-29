#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport


class Iface(object):
    def uploadMap(self, gamemap):
        """
        Upload the map to player.
        The map is made of two-dimesional array of integer. The first dimension means row of the map. The second dimension means column of the map.
        For example, if N is the map size, position(0,0) means upper left corner, position(0,N) means the upper right corner.
        In the map array, 0 means empty field, 1 means barrier, 2 means woods, 3 means flag.


        Parameters:
         - gamemap
        """
        pass

    def uploadParamters(self, arguments):
        """
        Parameters:
         - arguments
        """
        pass

    def assignTanks(self, tanks):
        """
        Assign a list of tank id to the player.
        each player may have more than one tank, so the parameter is a list.


        Parameters:
         - tanks
        """
        pass

    def latestState(self, state):
        """
        Report latest game state to player.


        Parameters:
         - state
        """
        pass

    def getNewOrders(self):
        """
        Ask for the tank orders for this round.
        If this funtion does not return orders within the given round timeout, game engine will make all this player's tank to stick around.
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def uploadMap(self, gamemap):
        """
        Upload the map to player.
        The map is made of two-dimesional array of integer. The first dimension means row of the map. The second dimension means column of the map.
        For example, if N is the map size, position(0,0) means upper left corner, position(0,N) means the upper right corner.
        In the map array, 0 means empty field, 1 means barrier, 2 means woods, 3 means flag.


        Parameters:
         - gamemap
        """
        self.send_uploadMap(gamemap)
        self.recv_uploadMap()

    def send_uploadMap(self, gamemap):
        self._oprot.writeMessageBegin('uploadMap', TMessageType.CALL, self._seqid)
        args = uploadMap_args()
        args.gamemap = gamemap
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_uploadMap(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = uploadMap_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def uploadParamters(self, arguments):
        """
        Parameters:
         - arguments
        """
        self.send_uploadParamters(arguments)
        self.recv_uploadParamters()

    def send_uploadParamters(self, arguments):
        self._oprot.writeMessageBegin('uploadParamters', TMessageType.CALL, self._seqid)
        args = uploadParamters_args()
        args.arguments = arguments
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_uploadParamters(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = uploadParamters_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def assignTanks(self, tanks):
        """
        Assign a list of tank id to the player.
        each player may have more than one tank, so the parameter is a list.


        Parameters:
         - tanks
        """
        self.send_assignTanks(tanks)
        self.recv_assignTanks()

    def send_assignTanks(self, tanks):
        self._oprot.writeMessageBegin('assignTanks', TMessageType.CALL, self._seqid)
        args = assignTanks_args()
        args.tanks = tanks
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_assignTanks(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = assignTanks_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def latestState(self, state):
        """
        Report latest game state to player.


        Parameters:
         - state
        """
        self.send_latestState(state)
        self.recv_latestState()

    def send_latestState(self, state):
        self._oprot.writeMessageBegin('latestState', TMessageType.CALL, self._seqid)
        args = latestState_args()
        args.state = state
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_latestState(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = latestState_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def getNewOrders(self):
        """
        Ask for the tank orders for this round.
        If this funtion does not return orders within the given round timeout, game engine will make all this player's tank to stick around.
        """
        self.send_getNewOrders()
        return self.recv_getNewOrders()

    def send_getNewOrders(self):
        self._oprot.writeMessageBegin('getNewOrders', TMessageType.CALL, self._seqid)
        args = getNewOrders_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getNewOrders(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getNewOrders_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getNewOrders failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["uploadMap"] = Processor.process_uploadMap
        self._processMap["uploadParamters"] = Processor.process_uploadParamters
        self._processMap["assignTanks"] = Processor.process_assignTanks
        self._processMap["latestState"] = Processor.process_latestState
        self._processMap["getNewOrders"] = Processor.process_getNewOrders

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_uploadMap(self, seqid, iprot, oprot):
        args = uploadMap_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = uploadMap_result()
        try:
            self._handler.uploadMap(args.gamemap)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("uploadMap", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_uploadParamters(self, seqid, iprot, oprot):
        args = uploadParamters_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = uploadParamters_result()
        try:
            self._handler.uploadParamters(args.arguments)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("uploadParamters", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_assignTanks(self, seqid, iprot, oprot):
        args = assignTanks_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = assignTanks_result()
        try:
            self._handler.assignTanks(args.tanks)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("assignTanks", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_latestState(self, seqid, iprot, oprot):
        args = latestState_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = latestState_result()
        try:
            self._handler.latestState(args.state)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("latestState", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getNewOrders(self, seqid, iprot, oprot):
        args = getNewOrders_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getNewOrders_result()
        try:
            result.success = self._handler.getNewOrders()
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getNewOrders", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class uploadMap_args(object):
    """
    Attributes:
     - gamemap
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'gamemap', (TType.LIST, (TType.I32, None, False), False), None, ),  # 1
    )

    def __init__(self, gamemap=None,):
        self.gamemap = gamemap

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.gamemap = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = []
                        (_etype23, _size20) = iprot.readListBegin()
                        for _i24 in range(_size20):
                            _elem25 = iprot.readI32()
                            _elem19.append(_elem25)
                        iprot.readListEnd()
                        self.gamemap.append(_elem19)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('uploadMap_args')
        if self.gamemap is not None:
            oprot.writeFieldBegin('gamemap', TType.LIST, 1)
            oprot.writeListBegin(TType.LIST, len(self.gamemap))
            for iter26 in self.gamemap:
                oprot.writeListBegin(TType.I32, len(iter26))
                for iter27 in iter26:
                    oprot.writeI32(iter27)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class uploadMap_result(object):

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('uploadMap_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class uploadParamters_args(object):
    """
    Attributes:
     - arguments
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'arguments', (Args, Args.thrift_spec), None, ),  # 1
    )

    def __init__(self, arguments=None,):
        self.arguments = arguments

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.arguments = Args()
                    self.arguments.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('uploadParamters_args')
        if self.arguments is not None:
            oprot.writeFieldBegin('arguments', TType.STRUCT, 1)
            self.arguments.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class uploadParamters_result(object):

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('uploadParamters_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class assignTanks_args(object):
    """
    Attributes:
     - tanks
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'tanks', (TType.I32, None, False), None, ),  # 1
    )

    def __init__(self, tanks=None,):
        self.tanks = tanks

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.tanks = []
                    (_etype31, _size28) = iprot.readListBegin()
                    for _i32 in range(_size28):
                        _elem33 = iprot.readI32()
                        self.tanks.append(_elem33)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('assignTanks_args')
        if self.tanks is not None:
            oprot.writeFieldBegin('tanks', TType.LIST, 1)
            oprot.writeListBegin(TType.I32, len(self.tanks))
            for iter34 in self.tanks:
                oprot.writeI32(iter34)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class assignTanks_result(object):

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('assignTanks_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class latestState_args(object):
    """
    Attributes:
     - state
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'state', (GameState, GameState.thrift_spec), None, ),  # 1
    )

    def __init__(self, state=None,):
        self.state = state

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.state = GameState()
                    self.state.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('latestState_args')
        if self.state is not None:
            oprot.writeFieldBegin('state', TType.STRUCT, 1)
            self.state.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class latestState_result(object):

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('latestState_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class getNewOrders_args(object):

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('getNewOrders_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class getNewOrders_result(object):
    """
    Attributes:
     - success
    """

    thrift_spec = (
        (0, TType.LIST, 'success', (TType.STRUCT, (Order, Order.thrift_spec), False), None, ),  # 0
    )

    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype38, _size35) = iprot.readListBegin()
                    for _i39 in range(_size35):
                        _elem40 = Order()
                        _elem40.read(iprot)
                        self.success.append(_elem40)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('getNewOrders_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter41 in self.success:
                iter41.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
