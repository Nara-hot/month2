import random
class Hero:
    def __init__(self,name,level,health,strength):
        self.name = name
        self. level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"приветб я {self.name}, мой уровень {self.level}")
    def attack(self):
        print(f"{self.name} наносить удар!")
        self.strength -=1
    def rest(self):
        print(f"{self.name} Одыхает...")
        self.health +=10


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina
    def attack(self):
        print(f"{self.name} атакует мечом!")

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        print(f"{self.name} кастует заклинание!")

class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        print(f"{self.name} атакует из-под тишка!")

warrior = Warrior("Арагорн", 10, 150, 20, 100)
mage = Mage("Гэндальф", 12, 80, 5, 200)
assassin = Assassin("Эцио", 11, 100, 15, 50)

heroes_dict = {
    "Warrior": warrior,
    "Mage": mage,
    "Assassin": assassin
}

def play_game():
    print("Выберите героя: Warrior / Mage / Assassin")
    user_choice = input("Ваш выбор: ").capitalize()

    if user_choice not in heroes_dict:
        print("Неверный выбор! Попробуйте снова.")
        return

    player = heroes_dict[user_choice]

    ai_choice_name = random.choice(list(heroes_dict.keys()))
    opponent = heroes_dict[ai_choice_name]

    print(f"\nВы выбрали: {user_choice}")
    player.attack()
    print(f"Противник: {ai_choice_name}")
    opponent.attack()
    print("-" * 20)

    if user_choice == ai_choice_name:
        print("Ничья!")
    elif (user_choice == "Warrior" and ai_choice_name == "Assassin") or \
            (user_choice == "Assassin" and ai_choice_name == "Mage") or \
            (user_choice == "Mage" and ai_choice_name == "Warrior"):
        print(f"{user_choice} победил!")
    else:
        print(f"{ai_choice_name} победил!")


if __name__ == "__main__":
    play_game()