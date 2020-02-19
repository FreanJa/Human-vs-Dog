#! python3
#可以键入 人类 生命值 和 攻击
#        狗 生命值 和 攻击
#设定 人类 为无差别 群体攻击
#     狗 为随机 单体攻击
#有 0.1 暴击率 暴击则攻击力*3

class char:
    def __init__(self,n):
        self.name = n

    def attack(self,enemy):
        enemy.blood -= self.damage

class person(char):                     #定义人类
    def __init__(self,n,b,d):
        super().__init__(n)
        self.blood = b                  #血量为自定义
        self.damage = d                 #人类默认攻击力为5 (人攻击方式为群体攻击
    def attack(self,enemy):
        super().attack(enemy)


class dog(char):                        #定义狗类
    def __init__(self,n,b,d):
        super().__init__(n)
        self.blood = b
        self.damage = d                #狗默认攻击力为10 (狗攻击方式为单体攻击
    def attack(self,enemy):
        super().attack(enemy)

def rnd():                              #定义随机函数 随机抽取本轮该狗的攻击对象
    r = int(random.random()*2)
    if r == 0 :
        if p1.blood > 0 :
            return 'p1'
        elif p2.blood > 0:
            return 'p2'
    else: 
        if p2.blood > 0 :
            return 'p2'
        elif p1.blood > 0:
            return 'p1'
    return 'win'

def cs():                               #暴击 暴击率0.1 攻击力*3
    r = int(random.random()*10)
    if r == 8:
        return 3
    return 1

import random
print('*******************')
print('*** 人 狗 大 战 ***')
print('* Humans vs. Dogs *')
print('*******************')
time = int(input('轮数:'))
pb = int(input('人类血量:'))
pd = int(input('人类攻击:'))
db= int(input('狗血量:'))
dd= int(input('狗攻击:'))
p1 = person('p1',pb,pd)
p2 = person('p2',pb,pd)
d1 = dog('d1',db,dd)
d2 = dog('d2',db,dd)
d3 = dog('d3',db,dd)
for i in range(time):
    print('*******第%s轮*******'%(i+1))
    if p1.blood > 0:                #因为狗的攻击对象随机 所以p1和p2是否存活需要分步考虑
        if d1.blood > 0:            #因为人是群体攻击 所以只需判断一只狗的血量即可
            s = cs()
            if s != 1:
                p1 = person('p1',pb,pd*s)
            p1.attack(d1)
            p1.attack(d2)
            p1.attack(d3)
        else:
            print('person win!')
            break
    if p2.blood > 0:
        if d1.blood > 0:
            s = cs()
            if s != 1:
                p2 = person('p2',pb,pd*s)
            p1.attack(d1)
            p1.attack(d2)
            p1.attack(d3)
        else:
            print('person win!')
            break

    if d1.blood > 0:
        t = rnd()
        s = cs()
        if s != 1:
            d1 = person('d1',db,dd*s)
        if t == 'win':
            print('dog win!')
            break
        elif t == 'p1':
            d1.attack(p1)
        else:
            d1.attack(p2)

        t = rnd()
        s = cs()
        if s != 1:
            d2 = person('d2',db,dd*s)
        if t == 'win':
            print('dog win!')
            break
        elif t == 'p1':
            d2.attack(p1)
        else:
            d2.attack(p2)

        t = rnd()
        s = cs()
        if s != 1:
            d3 = person('d3',db,dd*s)
        if t == 'win':
            print('dog win!')
            break
        elif t == 'p1':
            d3.attack(p1)
        else:
            d3.attack(p2)
    print('当前状态:')
    print(' person:')
    print('  %s:%d %s:%d'%(p1.name,p1.blood,p2.name,p2.blood))
    print(' dog:')
    print('  %s:%d %s:%d %s:%d'%(d1.name,d1.blood,d2.name,d2.blood,d3.name,d3.blood))
    if d1.blood <= 0:
        print('********************')
        print('person win!')
        break
print('*******************')