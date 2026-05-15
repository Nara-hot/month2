# Словарь курсов валют относительно сома
rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):

        return self.amount * rates[self.currency]

    def __add__(self, other):

        if isinstance(other, Money):
            total_in_kgs = self.convert_to_kgs() + other.convert_to_kgs()
            return Money(total_in_kgs, "KGS")
        return NotImplemented

    def __sub__(self, other):

        if isinstance(other, Money):
            total_in_kgs = self.convert_to_kgs() - other.convert_to_kgs()
            return Money(total_in_kgs, "KGS")
        return NotImplemented

    def __mul__(self, number):

        if isinstance(number, (int, float)):
            return Money(self.amount * number, self.currency)
        return NotImplemented

    def __truediv__(self, number):

        if isinstance(number, (int, float)):
            if number == 0:
                raise ZeroDivisionError("Нельзя делить деньги на ноль!")
            return Money(self.amount / number, self.currency)
        return NotImplemented

    def __str__(self):

        return f"{self.amount} {self.currency}"

money1 = Money(100, "USD")   # Это 8900 сомов
money2 = Money(5000, "KGS")  # Это 5000 сомов

result_add = money1 + money2
print(f"Результат сложения: {result_add}") # Ожидаем 13900 KGS

result_sub = money1 - money2
print(f"Результат вычитания: {result_sub}") # Ожидаем 3900 KGS

result_mul = money1 * 3
print(f"Результат умножения: {result_mul}") # Ожидаем 300 USD

result_div = money2 / 2
print(f"Результат деления: {result_div}")   # Ожидаем 2500.0 KGS
