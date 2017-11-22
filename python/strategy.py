import sys
sys.path.append('gen-py')
from player.ttypes import Direction
from player.ttypes import Order

import copy
import random
from enum import Enum

class Context:
    gamemap = None
    size = None
    arguments = None
    state = None
    lastState = None
    ourTankId = []
    outTanks = []
    enemyTanks = []

class Action(Enum):
    MOVE = 0
    TURN_UP = 1
    TURN_DOWN = 2
    TURN_LEFT = 3
    TURN_RIGHT = 4
    FIRE_UP = 5
    FIRE_DOWN = 6
    FIRE_LEFT = 7
    FIRE_RIGHT = 8
    NONE = -1



class Strategy:
    context = Context()
    mustRule = MustRule()
    avaibleRule = AvaibleRule()

    def __init__(self):
        self.log={}

    # return list<Order>
    def run(self,state):
        orders = []

        self.context.lastState = copy.deepcopy(self.context.state)
        self.context.state = state
        for tank in state.tanks:
            if tank.id in self.context.ourTankId:
                self.context.outTanks.append(tank)
            else:
                self.context.enemyTanks.append(tank)

        tanks = self.sortTank(self.context.outTanks)
        for tank in tanks:
            # Rule
            action = RuleFacade.action(tank, self.context)
            self.update(tank, action)
            orders.append(self.action2Order(tank,action))
        return orders

    def positionAvaiable(self, x ,y):
        if x < 0 or x >= self.context.size:
            return False
        if y < 0 or y >= self.context.size:
            return False
        pos = self.context.gamemap(x)(y)
        return (pos == 1) or (pos == 2)

    # reun list<tank>
    def sortTank(self, tanks):
        dic = {}
        for tank in tanks:
            x = tank.pos.x
            y = tank.pos.y
            c = 0
            if self.positionAvaiable(x, y-1):
                c+=1
            if self.positionAvaiable(x, y+1):
                c+=1
            if self.positionAvaiable(x+1, y):
                c+=1
            if self.positionAvaiable(x-1, y):
                c+=1
            dic[c] = tank
        score_list = sorted(dic.items(), key=lambda d: d[0], reverse=True)
        return [i for (i,j) in score_list]

    def update(self, tank, action):
        tanks = self.context.state.tanks
        for tankEach in tanks:
            if tankEach.id == tank.id:
                if action == Action.NONE:
                    pass
                if action.value >=Action.TURN_UP or action.value <= Action.TURN_RIGHT:
                    tankEach.dir = action.value
                if action.value >=Action.FIRE_UP:
                    #update shells
                if action.value == Action.MOVE:
                    if tankEach.dir == Direction.UP:
                        tankEach.pos.x = tankEach.pos.x - 1
                    if tankEach.dir == Direction.DOWN:
                        tankEach.pos.x = tankEach.pos.x + 1
                    if tankEach.dir == Direction.LEFT:
                        tankEach.pos.y = tankEach.pos.x - 1
                    if tankEach.dir == Direction.RIGHT:
                        tankEach.pos.y = tankEach.pos.x + 1
        pass

    def action2Order(self, tank, action):
        if action == Action.MOVE:
            return Order(tank.id, "move", 1)
        if action == Action.TURN_UP:
            return Order(tank.id, "turnTo", Direction.UP)
        if action == Action.TURN_DOWN:
            return Order(tank.id, "turnTo", Direction.DOWN)
        if action == Action.TURN_LEFT:
            return Order(tank.id, "turnTo", Direction.LEFT)
        if action == Action.TURN_RIGHT:
            return Order(tank.id, "turnTo", Direction.RIGHT)
        if action == Action.FIRE_UP:
            return Order(tank.id, "fire", Direction.UP)
        if action == Action.FIRE_DOWN:
            return Order(tank.id, "fire", Direction.DOWN)
        if action == Action.FIRE_LEFT:
            return Order(tank.id, "fire", Direction.LEFT)
        if action == Action.FIRE_RIGHT:
            return Order(tank.id, "fire", Direction.RIGHT)



class RuleFacade:
    mustRule = MustRule()
    avaibleRule = AvaibleRule()

    def __init__(self, context):
        self.context = context

    @staticmethod
    def action(tank, context):
        must = RuleFacade.mustRule.action(tank, context)
        if must != Action.NONE:
            return must
        mays = RuleFacade.avaibleRule.action(tank. context)
        random.choice(mays)


        return Action.MOVE

class MustRule:
    def action(self, tank, context):
        x= tank.pos.x
        y= tank.pos.y

        # check enemy in line
        for enemy in enemyTanks:
            x_e = enemy.pos.x
            y_e = enemy.pos.y
            if x == x_e:
                start, end, isLess = self.compare( y, y_e)
                flag = true
                for i in range(start+1, end):
                    p = context.gamemap[x][i]
                    if p


        if 1>1:
            return Action.NONE
        return Action.MOVE

    def compare(self, a, b):
        if a < b:
            return a, b, True
        else:
            return b, a, False

class AvaibleRule:
    def action(self, tank, context):
        actions = []
        actions.append(Action.MOVE)
        return actions