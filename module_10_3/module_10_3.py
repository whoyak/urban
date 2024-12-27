import random
import threading
import time

class Bank:
    def __init__(self,balance:int,transactions:int):
        self.balance = balance
        self.lock = threading.Lock()
        self.transactions= transactions
    def deposit(self):
        while self.transactions>0:
            with self.lock:
                r = random.randint(50,500)
                self.balance+= r
                print(f'Пополнение: {r}. Баланс: {self.balance}')
                time.sleep(0.001)
                self.transactions -= 1

    def take(self):
        while self.transactions > 0:
            with self.lock:
                r = random.randint(50, 500)
                print(f'Запрос на {r}')
                if r <=self.balance:
                    self.balance -= r
                    print(f'Снятие: {r}. Баланс: {self.balance}')
                elif r>self.balance:
                    print(f'Запрос отклонен, недостаточно средств')
                self.transactions -= 1
            time.sleep(0.001)


bk = Bank(balance=1000,transactions=100)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
