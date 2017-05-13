#  http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Visitor.html
import random

class Flower(object):
    def accept(self,visitor):
        visitor.visit(self)

    #授粉
    def pollinate(self, pollinator):
        print(self,'pollinated by',pollinator)

    def eat(self, eater):
        print(self, "eaten by ", eater)

    def __str__(self):
        return self.__class__.__name__

#剑兰
class Glaiolus(Flower):
    pass

#
#毛茛属是植物中一个大属，包含有大约400余种，绝大多数为草本植物，有一年生或二年生的；
#花为黄色或白色，少数为橙色甚至红色，花期在春季或夏季；叶基生或互生，单叶分裂或复叶；
#果实为瘦果。许多品种可入药或作为观赏花卉。

#许多品种的毛茛属植物生长在水边，其拉丁语名称意思就是“小青蛙”，言其在水边像青蛙一样。

#几乎所有毛茛属植物都有毒，味苦，但干燥后的植物毒性逐渐消失
class Runuculus(Flower):
    pass

#菊花
class Chrysanthemum(Flower):
    pass

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class Bug(Visitor):
    pass
class Pollinator(Bug):
    pass
#捕食性动物
class Predator(Bug):
    pass


class Bee(Pollinator):
    def visit(self, flower):
        flower.pollinate(self)

class Fly(Pollinator):
    def visit(self, flower):
        flower.pollinate(self)

class Worm(Predator):
    def visit(self,flower):
        flower.eat(self)

def flowerGen(n):
    flwrs = Flower.__subclasses__()
    for i in range(n):
        yield random.choice(flwrs)()


if __name__ == '__main__':
    # import pdb
    # pdb.set_trace()
    bee = Bee()
    fly = Fly()
    worm = Worm()
    for flower in flowerGen(8):
        flower.accept(bee)
        flower.accept(fly)
        flower.accept(worm)
        print('-'*10)