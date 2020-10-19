from PublicReference.base import *

class 真·战斗法师主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '矛':
            return round(self.CD / self.恢复 * 1.05, 1)
        if 武器类型 == '棍棒':
            return round(self.CD / self.恢复 * 0.95, 1)

class 真·战斗法师技能0(被动技能):
    名称 = '尼巫的战斗术'
    所在等级=15
    等级上限=11
    基础等级=1
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级,3)

class 真·战斗法师技能1(被动技能):
    名称 = '炫纹'
    所在等级=15
    等级上限=60
    基础等级=46  
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.20+0.00*self.等级,3)
    
class 真·战斗法师技能2(被动技能):
    名称='矛精通'
    所在等级=20
    等级上限=30
    基础等级=20  
    def 加成倍率(self, 武器类型):
        if self.等级==0 or 武器类型 != '矛':
            return 1.0  
        if self.等级<=20:
            return round(1.00+0.01*self.等级,3) 
        if self.等级>20:
            return round(0.80+0.02*self.等级,3)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 真·战斗法师技能3(被动技能):
    名称='棍棒精通'
    所在等级=20
    等级上限=30
    基础等级=20  
    def 加成倍率(self, 武器类型):
        if self.等级==0 or 武器类型 != '棍棒':
            return 1.0  
        if self.等级<=20:
            return round(1.00+0.01*self.等级,3) 
        if self.等级>20:
            return round(0.80+0.02*self.等级,3)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)
    
class 真·战斗法师技能4(真·战斗法师主动技能):
    名称 = '炫纹发射'
    备注 = '(个数,TP为强化炫纹)'
    是否主动 = 0
    所在等级=15
    等级上限=60
    基础等级=46
    基础=326.00/1.118*1.1
    成长=37.00/1.118*1.1
    CD=0.25
    TP成长=0.10
    TP上限 = 1
    
class 真·战斗法师技能5(真·战斗法师主动技能):
    名称='碎霸'
    所在等级=30
    等级上限=60
    基础等级=38
    基础=3637.4186/1.118*1.1
    成长=419.5813/1.118*1.1
    CD=8
    TP成长=0.10
    TP上限 = 5
    额外倍率 = 0
    触发概率 = 0
    def 等效百分比(self, 武器类型):
        return (1 + self.额外倍率 * self.触发概率) * super().等效百分比(武器类型)
    
class 真·战斗法师技能6(真·战斗法师主动技能):
    名称='流星闪影击'
    所在等级=35
    等级上限=60
    基础等级=36  
    基础=7762.4285/1.118*1.186
    成长=876.5714/1.118*1.186
    CD=20
    TP成长=0.10
    TP上限 = 5
    演出时间 = 0.6
   
class 真·战斗法师技能7(真·战斗法师主动技能):
    名称='炫纹强压'
    所在等级=35
    等级上限=60
    基础等级=36  
    基础=8777
    成长=991
    CD=17
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.4
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.242
            self.CD *=0.92

        elif x == 1:
            self.倍率*=1.334
            self.CD *=0.92
        

class 真·战斗法师技能8(真·战斗法师主动技能):
    名称='强袭流星打'
    所在等级=40
    等级上限=60
    基础等级=33  
    基础=8884.8461/1.118*1.186
    成长=1025.1538/1.118*1.186
    CD=25
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.5
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.1865
            

        elif x == 1:
            self.倍率*=1.281
            
        
class 真·战斗法师技能9(真·战斗法师主动技能):
    名称='煌龙偃月'
    所在等级=45
    等级上限=60
    基础等级=31  
    基础 = 3542.2972/1.118*1.186
    成长 = 408.7027/1.118*1.186
    攻击次数 = 1.0
    基础2 = 1181.7837/1.118*1.186
    成长2 = 136.2162/1.118*1.186
    攻击次数2 = 7.0
    基础3 = 5056.6216/1.118*1.186
    成长3 = 584.3783/1.118*1.186
    攻击次数3 = 1.0
    CD=45
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.24
            

        elif x == 1:
            self.倍率*=1.318
            
        
class 真·战斗法师技能10(真·战斗法师主动技能):
    名称='煌龙乱舞'
    所在等级=45
    等级上限=60
    基础等级=31  
    基础 = 1205.7027/1.118*1.186
    成长 = 136.2972/1.118*1.186
    攻击次数 = 5.0
    基础2 = 9052.8918/1.118*1.186
    成长2 = 1022.1081/1.118*1.186
    攻击次数2 = 1.0
    CD=45
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.2552
            

        elif x == 1:
            self.倍率*=1.3272
            

class 真·战斗法师技能11(被动技能):
    名称='斗神意志'
    所在等级=48
    等级上限=40
    基础等级=20
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.05+0.02*self.等级,3)

class 真·战斗法师技能12(真·战斗法师主动技能):
    名称='星纹陨爆'
    所在等级=50
    等级上限=40
    基础等级=12  
    基础=40144.7058/1.118*1.186
    成长=12119.2941/1.118*1.186
    CD=145.0
    演出时间 = 2

class 真·战斗法师技能13(真·战斗法师主动技能):
    名称 = '变身贝亚娜'
    备注 = '(一轮)'
    所在等级=50
    等级上限=1
    基础等级=1  
    基础 = 294.9333
    成长 = 90.0667
    攻击次数 = 4.0
    基础2 = 735.6
    成长2 = 225.4
    攻击次数2 = 1.0
    CD=1

class 真·战斗法师技能14(真·战斗法师主动技能):
    名称='变身贝亚娜苍天击'
    所在等级=50
    等级上限=1
    基础等级=1  
    基础=1107.4/1.236*1.186
    成长=338.6/1.236*1.186
    CD=1   

class 真·战斗法师技能15(真·战斗法师主动技能):
    名称='变身贝亚娜天地碎霸'
    所在等级=50
    等级上限=1
    基础等级=1 
    基础 = 509.5333/1.14*1.186
    成长 = 187.4667/1.14*1.186
    攻击次数 = 1.0
    基础2 = 2245.2667/1.14*1.186
    成长2 = 806.7333/1.14*1.186
    攻击次数2 = 1.0
    CD=7

class 真·战斗法师技能16(真·战斗法师主动技能):
    名称='闪击碎霸'
    所在等级=60
    等级上限=40
    基础等级=23  
    基础=14049.625/1.118*1.186
    成长=1586.375/1.118*1.186
    CD=30
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.9
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.15
            self.CD *=0.90

        elif x == 1:
            self.倍率*=1.24
            self.CD *=0.90

class 真·战斗法师技能17(真·战斗法师主动技能):
    名称='流星雷连击'
    所在等级=70
    等级上限=40
    基础等级=18  
    基础=23187.8889/1.118*1.186
    成长=2616.1111/1.118*1.186
    CD=50
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.10

        elif x == 1:
            self.倍率*=1.19
       

class 真·战斗法师技能18(被动技能):
    名称='战灵潜能'
    所在等级=75
    等级上限=40
    基础等级=11
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.22+0.02*self.等级,3)

class 真·战斗法师技能19(真·战斗法师主动技能):
    名称='炫纹簇'
    所在等级=75
    等级上限=40
    基础等级=16
    基础 = 4935.8125/1.118*1.185
    成长 = 557.1875/1.118*1.185
    攻击次数 = 7.0
    CD=45
    演出时间 = 1.3
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率*=1.3142857       
class 真·战斗法师技能20(真·战斗法师主动技能):
    名称='使徒之舞'
    所在等级=80
    等级上限=40
    基础等级=13  
    基础 = 1449.333/1.118*1.185
    成长 = 163.6923/1.118*1.185
    攻击次数 = 3.0
    基础2 = 2900.769/1.118*1.185
    成长2 = 327.2307/1.118*1.185
    攻击次数2 = 1.0
    基础3 = 29006.3076/1.118*1.185
    成长3 = 3272.6923/1.118*1.185
    攻击次数3 = 1.0
    CD=40
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率*=1.36801    

class 真·战斗法师技能21(真·战斗法师主动技能):
    名称='使徒化身'
    所在等级=85
    等级上限=40
    基础等级=5  
    基础 = 39871.1428/1.118*1.185
    成长 = 12035.8571/1.118*1.185
    攻击次数 = 1.0
    基础2 = 26580.1428/1.118*1.185
    成长2 = 8023.8571/1.118*1.185
    攻击次数2 = 1.0
    CD=180
    
class 真·战斗法师技能22(真·战斗法师主动技能):
    名称='原初之光'
    所在等级=95
    等级上限=60
    基础等级=6  
    基础 = 90673.8
    成长 = 10237.2
    CD=58
    

class 真·战斗法师技能23(被动技能):
    名称='调律'
    所在等级=95
    等级上限=40
    基础等级=4
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级,3)

class 真·战斗法师技能24(真·战斗法师主动技能):
    名称='星河绝灭斩'
    所在等级=100
    等级上限=40
    基础等级=2  
    基础 = 9665*4 + 7733*5 + 38660 + 25772 + 7733*15
    成长 = 2917*4 + 2333*5 + 11669 + 7780 + 2333*15
    CD=290
    演出时间 = 5
    def 加成倍率(self, 武器类型):
        return 0.0

class 真·战斗法师技能25(真·战斗法师主动技能):
    名称='基本攻击'
    备注 = '(一轮,TP为基础精通)'
    所在等级=1
    等级上限=1
    基础等级=1  
    基础 = 225.2*2.662/1.115*1.1
    基础2 = 1.16 * 225.2*2.662/1.115*1.1
    基础3 = 1.8 * 225.2*2.662/1.115*1.1
    CD=1
    TP成长=0.10
    TP上限 = 3

class 真·战斗法师技能26(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['基本攻击']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

真·战斗法师技能列表 = []
i = 0
while i >= 0:
    try:
        exec('真·战斗法师技能列表.append(真·战斗法师技能'+str(i)+'())')
        i += 1
    except:
        i = -1

真·战斗法师技能序号 = dict()
for i in range(len(真·战斗法师技能列表)):
    真·战斗法师技能序号[真·战斗法师技能列表[i].名称] = i

真·战斗法师一觉序号 = 12
真·战斗法师二觉序号 = 0
真·战斗法师三觉序号 = 0
for i in 真·战斗法师技能列表:
    if i.所在等级 == 85:
        真·战斗法师二觉序号 = 真·战斗法师技能序号[i.名称]
    if i.所在等级 == 100:
        真·战斗法师三觉序号 = 真·战斗法师技能序号[i.名称]

真·战斗法师护石选项 = ['无']
for i in 真·战斗法师技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        真·战斗法师护石选项.append(i.名称)

真·战斗法师符文选项 = ['无']
for i in 真·战斗法师技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        真·战斗法师符文选项.append(i.名称)

class 真·战斗法师角色属性(角色属性):

    实际名称 = '真·战斗法师'
    角色 = '魔法师(女)'
    职业 = '战斗法师'

    武器选项 = ['矛', '棍棒']
    
    伤害类型选择 = ['物理百分比', '魔法百分比']
    
    伤害类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量', '智力']

    主BUFF = 1.790

    远古记忆 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(真·战斗法师技能列表)
        self.技能序号= deepcopy(真·战斗法师技能序号)

    def 被动倍率计算(self):
        if self.武器类型 == '矛':
            self.技能栏[self.技能序号['棍棒精通']].关联技能 = ['无']
        elif self.武器类型 == '棍棒':
            self.技能栏[self.技能序号['矛精通']].关联技能 = ['无']
        for i in [13, 14, 15]:
            self.技能栏[i].等级 = self.技能栏[12].等级
        super().被动倍率计算()

    def 站街力量(self):
        return int(max(self.力量,self.智力))

    def 站街智力(self):
        return self.站街力量()

    def 面板力量(self):
        return max(super().面板力量(), super().面板智力())
      
    def 面板智力(self):
        return self.面板力量()

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间) / i.等效CD(self.武器类型) + 1 + i.基础释放次数))
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        if '闪击碎霸' in [self.护石第一栏, self.护石第二栏, self.护石第三栏]:
            技能释放次数[self.技能序号['碎霸']] += 技能释放次数[self.技能序号['闪击碎霸']]
            
        return 技能释放次数

    def 武器基础(self):
        temp = 装备列表[装备序号[self.装备栏[11]]]

        self.力量 += temp.力量
        self.智力 += temp.智力
        self.物理攻击力 += temp.物理攻击力
        self.魔法攻击力 += temp.物理攻击力
        self.独立攻击力 += temp.独立攻击力

        if temp.所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(temp.等级,temp.品质,self.强化等级[11],self.武器类型,'物理')
            self.魔法攻击力 += 武器计算(temp.等级,temp.品质,self.强化等级[11],self.武器类型,'物理')
            self.独立攻击力 += 锻造计算(temp.等级,temp.品质,self.武器锻造等级)

class 真·战斗法师(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 真·战斗法师角色属性()
        self.角色属性A = 真·战斗法师角色属性()
        self.角色属性B = 真·战斗法师角色属性()
        self.一觉序号 = 真·战斗法师一觉序号
        self.二觉序号 = 真·战斗法师二觉序号
        self.三觉序号 = 真·战斗法师三觉序号
        self.护石选项 = deepcopy(真·战斗法师护石选项)
        self.符文选项 = deepcopy(真·战斗法师符文选项)

    def 界面(self):
        super().界面()
        self.碎霸概率=MyQComboBox(self.main_frame2)
        self.碎霸概率.resize(130,20)
        self.碎霸概率.move(320,450)
        for i in range(11):
            self.碎霸概率.addItem('歼灵灭魂矛：' + str(i * 10) + '%')
        self.碎霸概率.setCurrentIndex(1)

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        属性.技能栏[属性.技能序号['碎霸']].触发概率 = round(self.碎霸概率.currentIndex() / 10, 2)

