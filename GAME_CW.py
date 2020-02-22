#GAME_CW Version 0.1.0

from random import randint
from enum import Enum
from time import sleep
from sys import exit
from os import system
import random

       ###############################################
###### WELCOME TO THE COLD WAR IRON CURTAIN SIMULATION ########
       ###############################################
           


class Job(Enum):
    Kuomintang_Army = 1 #국민당 육군
    Peoples_Liberation_Army = 2 #중국 인민 해방 육군
    United_States_Army = 3 #미합중국 육군
    Soviet_Army = 4 #소비에트 연방 육군


class Player:
    def __init__(self, name, job):
        self.name = name
        if job == Job.Kuomintang_Army:
            self.HP = 3
            self.ATK = 3
            self.DEF = 1
            self.DEX = 2
            self.CRI = 1
        elif job == Job.Peoples_Liberation_Army:
            self.HP = 3
            self.ATK = 3
            self.DEF = 2
            self.DEX = 1
            self.CRI = 1
        elif job == Job.United_States_Army:
            self.HP = 8
            self.ATK = 5
            self.DEF = 3
            self.DEX = 2
            self.CRI = 4 
        elif job == job.Soviet_Army:
            self.HP = 20
            self.ATK = 1
            self.DEF = 2
            self.DEX = 1
            self.CRI = 1

    def __str__(self):
        return "NAME: {}\nHP: {}".format(self.name, self.HP)

    def attack(self, enemy):
        if self.is_dead():
            print("{} 승리!".format(enemy.name))
            exit(1)
        print("{} attack {}".format(self.name, enemy.name))
        lucky1 = randint(1, 10)
        damage = self.ATK
        if lucky1 <= self.CRI:
            print("치명타!")
            damage *= 1.5
        lucky2 = randint(1, 10)
        if lucky2 <= enemy.DEX:
            print("빗나감!")
        else:
            total_damage = damage - enemy.DEF
            enemy.HP -= total_damage
            print()

    def is_dead(self):
        return self.HP <= 0

JJ = Player("장제스", Job.Kuomintang_Army)
MD = Player("모택동", Job.Peoples_Liberation_Army)
HT = Player("해리 트루먼", Job.United_States_Army)
IS = Player("이오시프 스탈린", Job.Soviet_Army)


coin = randint(1, 2)
if coin == 1:
    for i in range(10):
        print("=======================================")
        print("장제스 차례")
        sleep(1)
        JJ.attack(MD)
        sleep(1)
        print("모택동 차례")
        sleep(1)
        MD.attack(JJ)
        sleep(1)
        print()
        print("장제스의 상태:")
        print(JJ)
        print("모택동의 상태:")
        print(MD)
        print("=======================================")
        sleep(2)
else:
    for i in range(10):
        print("=======================================")
        print("모택동 차례")
        sleep(1)
        MD.attack(JJ)
        sleep(1)
        print("장제스 차례")
        sleep(1)
        JJ.attack(MD)
        sleep(1)
        print()
        print("장제스의 상태:")
        print(JJ)
        print("모택동의 상태:")
        print(MD)
        print("=======================================")
        sleep(2)

        
        
coin = randint(3, 4)
if coin == 3:
    for i in range(10):
        print("=======================================")
        print("트루먼의 차례")
        sleep(1)
        HT.attack(IS)
        sleep(1)
        print("스탈린의 차례")
        sleep(1)
        IS.attack(HT)
        sleep(1)
        print()
        print("트루먼의 상태:")
        print(HT)
        print("스탈린의 상태:")
        print(IS)
        print("=======================================")
        sleep(2)
else:
    for i in range(10):
        print("=======================================")
        print("스탈린의 차례")
        sleep(1)
        IS.attack(HT)
        sleep(1)
        print("트루먼의 차례")
        sleep(1)
        HT.attack(IS)
        sleep(1)
        print()
        print("트루먼의 상태:")
        print(HT)
        print("스탈린의 상태:")
        print(IS)
        print("=======================================")
        sleep(2)