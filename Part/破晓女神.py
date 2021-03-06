from math import *
from PublicReference.base import *


# 武器钝器
class 破晓女神主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '钝器':
            return round(self.CD / self.恢复 * 1.05, 1)


# 天使光翼
class 破晓女神技能0(被动技能):
    名称 = '天使光翼'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 * self.等级, 5)
    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.95

# 天使降临
class 破晓女神技能1(被动技能):
    名称 = '天使降临'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.08 + 0.01 * self.等级, 5)
        else:
            return round(0.98 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.08 + 0.01 * self.等级, 5)
        else:
            return round(0.98 + 0.02 * self.等级, 5)

# 一觉被动
class 破晓女神技能2(被动技能):
    名称 = '荣耀之光'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105+0.015 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

# 二觉被动
class 破晓女神技能3(被动技能):
    名称 = '戒律'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


# 卓越之力
class 破晓女神技能4(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 超卓之心
class 破晓女神技能5(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


# 觉醒之抉择
class 破晓女神技能6(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

# 神光冲击
class 破晓女神技能7(破晓女神主动技能):
    名称 = '神光冲击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1596.7
    成长 = 180.3
    CD = 4
    TP成长 = 0.10
    TP上限 = 5

# 神光连斩
class 破晓女神技能8(破晓女神主动技能):
    名称 = '神光连斩'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2109.7
    成长 = 238.3
    CD = 5
    TP成长 = 0.10
    TP上限 = 5

# 圣盾突击
class 破晓女神技能9(破晓女神主动技能):
    名称 = '圣盾突击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2756.7
    成长 = 311.3
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


# 神光喷涌
class 破晓女神技能10(破晓女神主动技能):
    名称 = '神光喷涌'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4451.9
    成长 = 503.1
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

# 神光盾击
class 破晓女神技能11(破晓女神主动技能):
    名称 = '神光盾击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4908.2
    成长 = 554.8
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

# 烈光
class 破晓女神技能12(破晓女神主动技能):
    名称 = '烈光'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4966.2
    成长 = 560.8
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

# 神光闪耀
class 破晓女神技能13(破晓女神主动技能):
    名称 = '神光闪耀'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7816.3
    成长 = 882.7
    CD = 16
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 2

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.09

# 神光闪影击
class 破晓女神技能14(破晓女神主动技能):
    名称 = '神光闪影击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 10235.5
    成长 = 1155.5
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


# 神罚之锤
class 破晓女神技能15(破晓女神主动技能):
    名称 = '神罚之锤'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 11383.6
    成长 = 1285.4
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27
        elif x == 1:
            self.倍率 *= 1.27 + 0.09


# 神光之跃
class 破晓女神技能16(破晓女神主动技能):
    名称 = '神光之跃'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 19198.4
    成长 = 2167.6
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.08


# 一觉
class 破晓女神技能17(破晓女神主动技能):
    名称 = '信仰聚合神光惩戒'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 46241.6
    成长 = 13959.2
    CD = 152.3


# 圣盾裁决
class 破晓女神技能18(破晓女神主动技能):
    名称 = '圣盾裁决'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 14912.3
    成长 = 1683.7
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.24 + 0.08

# 破晓之光
class 破晓女神技能19(破晓女神主动技能):
    名称 = '破晓之光'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 29092.3
    成长 = 3284.7
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.11
        self.CD *= 0.90

# 神光回旋斩
class 破晓女神技能20(破晓女神主动技能):
    名称 = '神光回旋斩'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 46139.6
    成长 = 5209.4
    CD = 40
    是否有护石 = 1

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
           self.倍率 *= 1.368

# 神圣信约
class 破晓女神技能21(破晓女神主动技能):
    名称 = '神圣信约'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 50250.4
    成长 = 5673.6
    CD = 45
    是否有护石 = 1

    护石选项 = ['圣痕','（蓄力）']
    def 装备护石(self, x):
        if x == 0:
           self.倍率 *= 1.18 + 0.14
        elif x == 1:
           self.倍率 *= 1.32 * (11+0.23)/11

# 二觉
class 破晓女神技能22(破晓女神主动技能):
    名称 = '神圣意志大天使降临'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 106483
    成长 = 32147
    CD = 189

破晓女神技能列表 = []
i = 0
while i >= 0:
    try:
        exec('破晓女神技能列表.append(破晓女神技能' + str(i) + '())')
        i += 1
    except:
        i = -1

破晓女神技能序号 = dict()
for i in range(len(破晓女神技能列表)):
    破晓女神技能序号[破晓女神技能列表[i].名称] = i

破晓女神一觉序号 = 0
破晓女神二觉序号 = 0
破晓女神三觉序号 = 0
for i in 破晓女神技能列表:
    if i.所在等级 == 50:
        破晓女神一觉序号 = 破晓女神技能序号[i.名称]
    if i.所在等级 == 85:
        破晓女神二觉序号 = 破晓女神技能序号[i.名称]
    if i.所在等级 == 100:
        破晓女神三觉序号 = 破晓女神技能序号[i.名称]

破晓女神护石选项 = ['无']
for i in 破晓女神技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        破晓女神护石选项.append(i.名称)

破晓女神符文选项 = ['无']
for i in 破晓女神技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        破晓女神符文选项.append(i.名称)


class 破晓女神角色属性(角色属性):
    实际名称 = '破晓女神'
    角色 = '守护者'
    职业 = '帕拉丁'

    武器选项 = ['钝器']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '板甲'
    防具精通属性 = ['力量']

    主BUFF = 1.89

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(破晓女神技能列表)
        self.技能序号 = deepcopy(破晓女神技能序号)

class 破晓女神(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 破晓女神角色属性()
        self.角色属性A = 破晓女神角色属性()
        self.角色属性B = 破晓女神角色属性()
        self.一觉序号 = 破晓女神一觉序号
        self.二觉序号 = 破晓女神二觉序号
        self.三觉序号 = 破晓女神三觉序号
        self.护石选项 = deepcopy(破晓女神护石选项)
        self.符文选项 = deepcopy(破晓女神符文选项)

