import glob
import sys
sys.path.append('gen-py')
# sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])

from player.ttypes import Order
from player.PlayerServer import Processor
import random


from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class TankHandler:
    tankIds = []
    actions = ['fire', 'turnTo', 'move', '']

    def __init__(self):
        self.log = {}

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
        self.tankIds = tanks

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
