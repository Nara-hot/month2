class Hero:
   def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

   def action(self):
       print(f"{self.name} готов к бою!")

Nara = Hero("Nara", 5, 100)
Nara.action()

class Hero:
    def __init__(self, name):
        self.name = name

    def action(self):
        print(f"Герой {self.name} делает ход")

class MageHero(Hero):
    def __init__(self, name, mp):
        super().__init__(name)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")

class WarriorHero(MageHero):
    pass

mage = MageHero("Юна", 100)
warrior = WarriorHero("Нара", 50)

mage.action()
warrior.action()

class BankAccount:
    bank_name = "Iron Bank"

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        return self.__password == password

    @property
    def full_info(self):
        return f"Владелец: {self.hero.name}, Баланс: {self._balance}"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        level = getattr(self.hero, 'level', 1)
        return level * 10
