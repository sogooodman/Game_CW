from random import randint
from enum import Enum
from time import sleep
from sys import exit

i = 0
class Player:
    def __init__(self,name):
        self.name = name
        self.HP = 10
        self.CRI = 0
        self.ATK = 0
        self.DEF = 0
    def __str__(self):
        pass

    def attack(self, enemy):

        if self.ATK <= 0:
            print("주포가 너무나 약해 적에게 아무 피해를 주지 못했습니다!")
        else:
            chance = randint(1,10)
            if chance <= self.CRI:
                print("전차의 엔진룸에 직격했습니다!")
                self.special_attack(enemy)
            else:
                if self.ATK > 0:
                    print("{}이(가) {}을(를) 공격!".format(self.name, enemy.name))
                chance2 = randint(1,10)
                if chance2 <= enemy.DEX:
                    print("슬랫아머를 장착합니다.")
                    enemy.special_defense(self)
                else:
                    damage = self.ATK - enemy.DEF
                    if damage < 0:
                        damage = 0
                        print("흠집도 안났습니다!")
                    enemy.HP -= damage

    def special_attack(self, enemy):
        pass

    def special_defense(self, enemy):
        pass

    def is_dead(self):
        return self.HP <= 0

class Tiger(Player):
    def __init__(self,name):
        self.name = name
        self.HP = 10
        self.ATK = 6
        self.DEF = 3
        self.DEX = 4
        self.CRI = 3

    def __str__(self):
        return("NAME : {}. JOB: Tiger\nHP : {}"
.format(self.name, self.HP))
    def special_attack(self , enemy):
       self.DEX += 1
       print("""
       {}가 회피기동 공격을 시작합니다. {}의 회피력을 1증가시키고 주포를 발사합니다.
       {}의 현재 회피력 : {}
       """.format(self.name,self.name, self.name, self.DEX))
       damage = self.ATK - enemy.DEF
       if damage < 0:
             damage = 0
       enemy.HP -= damage
    def special_defense(self, enemy):
        print("""
        {}가 슬랫아머를 장착합니다. 공격을 무시하며, {}의 방어력이 1만큼 상승합니다.
        {}의 현재 방어력 :{}
        """.format(self.name,self.name, self.name,self.DEF))

class FT17(Player):
    def __init__(self,name):
        self.name = name
        self.HP = 3
        self.DEX = 8
        self.ATK = 1
        self.DEF = 2
        self.CRI = 4
        self.SAVEATK = 0
    
    def __str__(self):
        return("NAME : {}. JOB: FT17\nHP : {}"
.format(self.name, self.HP))
    def special_attack(self, enemy):
        self.ATK = self.SAVEATK
        self.ATK *=3
        self.attack(enemy)
        self.ATK = self.ATK/3
        print("""
            {}는 철갑탄을 장전합니다. 대인 공격으로는 부적합하지만 대전차 공격으로는 좋습니다. 
            """.format(self.name))

    
    def special_defense(self, enemy):
        print("""
        {}가 회피했습니다. 너무 날래고 게다가 작기까지 한데, 이걸 어떻게 맞춥니까.
        """.format(self.name))

class M4(Player):
    def __init__(self,name):
        self.name = name
        self.HP = 10
        self.ATK = 5
        self.DEF = 4
        self.CRI = 3
        self.DEX = 4
        self.SAVEATK = 0
        self.SAVEDEF = 0

    def __str__(self):
        return("NAME : {}. JOB: M4\nHP : {}"
.format(self.name, self.HP))
    def special_attack(self,enemy):
        self.ATK = self.SAVEATK
        self.ATK *=2
        self.attack(enemy)
        self.ATK = self.ATK/2
        self.DEX += 1
        print("""
            {}는 칼리오페 다연장 로켓을 장착해 발사합니다. 건물의 파괴용으로 쓰이지만 대전차용으로도 나쁘지 않습니다. 덤으로 로켓을 날리니 가벼워져 {}의 회피가 1만큼 상승합니다.
            """.format(self.name,self.name))


    def special_defense(self,enemy):
            print("""
            {}는 포방패를 들어 올렸습니다. 이제 기관총 사수는 보호받을수 있습니다. 방어력 1이 올라갑니다.
            """.format(self.name))
            self.DEF += 1

class T_34(Player):
    def __init__(self,name):
        self.name = name
        self.HP =  12
        self.ATK = 4
        self.DEF = 2
        self.CRI = 4
        self.DEX = 3
    def __str__(self):
        return("NAME : {}. JOB: T-34\nHP : {}"
.format(self.name, self.HP))
    def special_attack(self,enemy):
        print("""
        다른 전차를 하나 더 데려옵니다. 두번 공격합니다.
        """)
        sleep(2)
        self.attack(enemy)
        sleep(2)
        self.attack(enemy)
        sleep(2)

    def special_defense(self,enemy):
        damage = enemy.ATK - self.DEF
        if damage < 0:
            damage = 0
        self.HP -= damage
        self.ATK += damage
        print("""
        6월의 복수! {}의 체력이 소모된 만큼 포탄을 더 쌔게 날립니다. 
        """.format(enemy.name))
        #독소전쟁은 6월 22일에 발발한다.

class K2(Player):
    def __init__(self,name):
        self.name = name
        self.HP =  20
        self.ATK = 8
        self.FixedATK = 5
        self.DEF = 10
        self.CRI = 10
        self.DEX = 10
        self.SAVEATK = 0
    def __str__(self):
        return("NAME : {}. JOB: K2\nHP : {}"
.format(self.name, self.HP))
    def special_attack(self,enemy):
        print("""
        K2는 '날탄' 유식하게 영어로 말하자면 'Armor Piercing Fin-Stabilized Discarding Sabot'를 발사합니다. 이것보다 빠른건 주말뿐입니다.
        """)
        self.ATK = self.SAVEATK
        self.ATK *=5
        self.attack(enemy)
        self.ATK = self.ATK/5

    def special_defense(self,enemy):
        self.SAVEATK = self.ATK
        self.SAVEDEF = self.DEF
        self.ATK = 0
        self.DEF = 999
        print("""
        {}의 장갑은 너무나 강력하여 그 어느 전차도 관통하거나 흠집조차도 못 냅니다. 
        """.format(self.name))


def turn(p1,p2):
    print("==================================")
    print("{}의 차례.".format(p1.name))
    sleep(1)
    p1.attack(p2)
    print("현재 상태")
    print()
    print(p1)
    print()
    print(p2)
    print("==================================")
    ###########################################################
    if p2.is_dead():
        print("{}은 사망하셨습니다.".format(p2.name))
        print("{}의 승리!".format(p1.name))
        exit(1)
    ###########################################################
    input()
    print("==================================")
    print("{}의 차례.".format(p2.name))
    sleep(1)
    p2.attack(p1)
    print("현재 상태")
    print()
    print(p1)
    print()
    print(p2)
    print("==================================")
    ###########################################################
    if p1.is_dead():
        print("{}은 사망하셨습니다.".format(p1.name))
        print("{}의 승리!".format(p2.name))
        exit(1)
    input()
p1 = T_34("이오시프 스탈린")
p2 = M4("프랭클린 루즈벨트")

coin = randint(1,2)
if coin == 1:
    pass
else:
    (p1,p2) = (p2,p1)

print("게임을 시작합니다.")
n = True
while n:
    turn(p1,p2)
    if p1.is_dead() or p2.is_dead == True:
        n = False