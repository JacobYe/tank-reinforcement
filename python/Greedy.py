import sys
sys.path.append('gen-py')

from player.ttypes import Order
from player.PlayerServer import Processor
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import random
import copy
import numpy as np
from strategy import Strategy

class TankHandler:
    actions = ['fire', 'turnTo', 'move', '']
    tankIds = None
    lastState = None
    state = None

    def __init__(self):
        self.log = {}
        self.strategy = Strategy()

    def uploadMap(self, gamemap):
        self.strategy.gamemap = np.matrix(gamemap)


    def uploadParamters(self, arguments):
        self.strategy.arguments = arguments

    def assignTanks(self, tanks):
        self.tankIds = tanks

    def latestState(self, state):
        self.lastState = copy.deepcopy(self.state)
        self.state = state

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
