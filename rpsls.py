#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020/11/22
"""

import random

#�����ǣ������ü�ֽ��ֽ����ʯͷ��ʯͷ���������ʯͷ�������棻���涾��ʷ���ˣ�
#        ʷ���˴��������������ն���棻����Ե�����ֽ����ʷ���ˣ�ʷ��������ʯͷ
#0-rock ʯͷ
#1-Spock ʷ����
#2-paper ��
#3-lizard ����
#4-scissors ����

def name_to_number(name):   #����Ϸ�����Ӧ����ͬ������
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="��":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else: return "Error: No Correct Name"

def number_to_name(num):   #������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    if num==0:
        return "ʯͷ"
    elif num==1:
        return "ʷ����"
    elif num==2:
        return "��"
    elif num==3:
        return "����"
    elif num==4:
        return "����"
    else: return "Error: No Correct Name"

def rpsls(player_choice):
    print("����ѡ��Ϊ��"+str(player_choice))
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print("�������ѡ��Ϊ��"+str(comp_choice))
    difference=(comp_number-player_number)%5
    if difference==1 or difference==2:
        print("�����Ӯ��")
    elif difference==3 or difference==4:
        print("��Ӯ��")
    elif difference==0:
        print("���ͼ��������һ����")
    else: print("����")

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)