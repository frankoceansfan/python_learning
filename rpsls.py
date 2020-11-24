#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：林兴望
日期：2020/11/22
"""

import random

#规则是：剪刀裁剪纸；纸包裹石头；石头砸碎剪刀；石头砸死蜥蜴；蜥蜴毒死史波克；
#        史波克打碎剪刀；剪刀腰斩蜥蜴；蜥蜴吃掉布；纸反驳史波克；史波克蒸发石头
#0-rock 石头
#1-Spock 史波克
#2-paper 布
#3-lizard 蜥蜴
#4-scissors 剪刀

def name_to_number(name):   #将游戏对象对应到不同的整数
    if name=="石头":
        return 0
    elif name=="史波克":
        return 1
    elif name=="布":
        return 2
    elif name=="蜥蜴":
        return 3
    elif name=="剪刀":
        return 4
    else: return "Error: No Correct Name"

def number_to_name(num):   #将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    if num==0:
        return "石头"
    elif num==1:
        return "史波克"
    elif num==2:
        return "布"
    elif num==3:
        return "蜥蜴"
    elif num==4:
        return "剪刀"
    else: return "Error: No Correct Name"

def rpsls(player_choice):
    print("您的选择为："+str(player_choice))
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print("计算机的选择为："+str(comp_choice))
    difference=(comp_number-player_number)%5
    if difference==1 or difference==2:
        print("计算机赢了")
    elif difference==3 or difference==4:
        print("您赢了")
    elif difference==0:
        print("您和计算机出的一样呢")
    else: print("错误")

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)