import random


class Creature:
    def __init__(self, name, max_health, attack, defence, damage):
        self.name = name
        self.max_health = max_health
        self.attack = attack
        self.defence = defence
        self.damage = damage

        self.health = max_health

    def is_alive(self):
        return self.health > 0
    
    def hit(self, enemy):
        damage_modifier = self.attack - enemy.defence + 1
        if damage_modifier <0:
            damage_modifier = 1
        
        for i in range (damage_modifier):
            if random.randint (1, 6) >=5:
                damage = random.randint(self.damage[0], self.damage[1])
                enemy.health = max (0, enemy.health - damage)
                return


class Player(Creature):
    def __init__(self, name, max_health, attack, defence, damage):
        super().__init__(name, max_health, attack, defence, damage)

        self.health_bottles = 4

    def heal(self):
        if self.health_bottles > 0:
            self.health = self.health + int(0.3*self.max_health)
            if self.health > self.max_health:
                self.health = self.max_health
            self.health_bottles = self.health_bottles - 1


class Monster(Creature):
    def __init__(self, name, max_health, attack, defence, damage):
        super().__init__(name, max_health, attack, defence, damage)


if __name__ == "__main__":
    hero = Player('Anna', 100, 20, 20, (3,12))
    monster = Monster('Shrek', 100, 20, 20, (3,10))


    while True:
        #Hero turn
        if hero.health < hero.max_health/2:
            hero.heal()
            print (f"{hero.name} is healed. {hero.health_bottles} bottles have left.")

        hero.hit (monster)
        print(f"{hero.name} hits {monster.name}. {monster.name} health is {monster.health}")
        if not monster.is_alive():
            print(f"{hero.name} is a winner" )
            break
        #Monster turn
        monster.hit (hero)
        print(f"{monster.name} hits {hero.name}. {hero.name} health is {hero.health}" )
        if not hero.is_alive():
            print(f"{monster.name} is a winner" )
            break

    
    




