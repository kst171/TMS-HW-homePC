class BankAccount:
    # Конструктор класса
    def __init__(self, account_number, owner_name, balance=0.0):
        self.account_number = account_number  # Номер счета
        self.owner_name = owner_name          # Имя владельца
        self.balance = float(balance)         # Текущий баланс

    # Метод для пополнения счета
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Успешно: Счет {self.account_number} пополнен на +{amount} руб.")
        else:
            print("Ошибка: Сумма пополнения должна быть больше 0.")

    # Метод для снятия денег
    def withdraw(self, amount):
        if amount <= 0:
            print("Ошибка: Сумма снятия должна быть больше 0.")
        elif amount > self.balance:
            print(f"Ошибка: Недостаточно средств на счете {self.account_number}. Баланс: {self.balance} руб.")
        else:
            self.balance -= amount
            print(f"Успешно: Со счета {self.account_number} снято -{amount} руб.")

    # Метод для проверки текущего баланса
    def display_balance(self):
        print(f"Владелец: {self.owner_name} | Счет: {self.account_number} | Баланс: {self.balance} руб.")


# --- Пример использования класса ---

# 1. Создаем новый счет с начальным балансом 1000
account = BankAccount("BY456789", "Иван Иванов", 1000)
account.display_balance()
print("-" * 40)

# 2. Пополняем счет
account.deposit(500)
account.display_balance()
print("-" * 40)

# 3. Пытаемся снять слишком большую сумму (сработает защита)
account.withdraw(2000)
print("-" * 40)

# 4. Снимаем доступную сумму
account.withdraw(350)
account.display_balance()
