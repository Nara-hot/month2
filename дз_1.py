class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")
    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health +=1

Nakcy = Hero("Nakcy", 100, 150, 50)
Aragon = Hero("Aragon", 100, 100, 20)

Nakcy.greet()
Nakcy.attack()
Nakcy.rest()

Aragon.greet()
