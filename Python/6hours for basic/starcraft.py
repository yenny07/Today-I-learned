# 마린 : 공격 유닛
name = "마린"
hp = 40
dagage = 5
print("{0}유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, dagage))

# 탱크

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, hp))

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(name))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, locaion):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, locaion, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)


marine1= AttackUnit("마린1", 40, 5)
marine2 = AttackUnit("마린2", 40, 5)
tank1 = AttackUnit("탱크1", 150, 35)

wraith1 = AttackUnit("레이스", 80, 5)
wraith2 = AttackUnit("레이스", 80, 5)
wraith2.clocking = True # Unit 클래스에 없는 변수를 외부에서 이렇게 추가 가능

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

vulture = AttackUnit("벌쳐", 80, 10, 20)

battlecruiser = FlyableAttackUnit("배틀크루저")