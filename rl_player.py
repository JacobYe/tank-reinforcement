from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from player.ttypes import Order
from player.PlayerServer import Processor
import random

import sys
import glob
sys.path.append('gen-py')
# sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])


class TankHandler:
    tankIds = []
    actions = ['fire', 'turnTo', 'move', '']

    def __init__(self):
        self.log = {}

    def uploadMap(self, gamemap):
        pass

    def uploadParamters(self, arguments):
        pass

    def assignTanks(self, tanks):
        self.tankIds = tanks

    def latestState(self, state):
        pass

    def getNewOrders(self):
        rst = []
        for tid in self.tankIds:
            action = random.choice(self.actions)
            dirt = random.randint(1,4)
            rst.append(Order(tid, action, dirt))
        return rst


if __name__ == '__main__':
    handler = TankHandler()
    processor = Processor(handler)
    transport = TSocket.TServerSocket(port=9100)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')
