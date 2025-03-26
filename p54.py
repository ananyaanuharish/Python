# Encapsulation
class BankAccount:
    def __init__(self,balance): #variable declared inside constructor
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        self.__balance+=amount
        print(f"Deposited : {amount}, New balance: {self.__balance}")

acc_obj = BankAccount(1000)
acc_obj.set_balance(500)
print(acc_obj.get_balance())