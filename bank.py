import random

def find_account():
    branch_code = input('Branch code: ')
    number_account = input('Number account: ')
    for account in accounts_list:
        if account.branch_code == branch_code and account.number_account == number_account:
            return account


class Address(object):

    def __init__(self, street, number, city, country):
        self.street = street
        self.number = number
        self.city = city
        self.country = country


class Account(object):

    def __init__(self, branch_code, number_account, amount, person):
        self.branch_code = branch_code
        self.number_account = number_account
        self.amount = float(amount)
        self.person = person.name

    def show_balance(self):
        print('balance: ', self.amount, '$', sep='')

    def cash_out(self, cash_value):
        self.amount -= cash_value
        print('Balance: ', self.amount)

    def cash_deposit(self, deposit_value):
        self.amount += deposit_value

    def transfer_cash(self, transfer_value, account):
        account.amount += transfer_value
        self.amount -= transfer_value
        print(account.amount, self.amount)


class Person(object):

    def __init__(self, name):
        self.name = name


nivea = Person('Nivea')
daniel = Person('Daniel')
nivea_account = Account('17', '15', 3000, nivea)
daniel_account = Account('123', '35', 4000, daniel)
accounts_list = [nivea_account, daniel_account]
option = None
while True:
    x = input(('Olá, digite 1 para entrar em sua conta, ou digite 2 para abrir uma conta: '))
    if x == '1':
        account = find_account()
        if account is None:
            print('Essa conta não existe')
            exit()
        print('bem vindo,', account.person)
        while True:
            print('1- Show balance\n2- Cash ou\n3- Deposit\n4- Transfer cash\n5- Log out\n6- Close')
            option = input('Escolha uma das opções acima: ')
            if option == '1':
                account.show_balance()
            if option == '2':
                cash_value = float(input('Valor para saque: '))
                account.cash_out(cash_value)
            if option == '3':
                deposit_value = float(input('Valor para depósito: '))
                account.cash_deposit(deposit_value)
            if option == '4':
                transfer_value = float(input('Valor para transferência: '))
                if transfer_value < account.amount and transfer_value > 0:
                    print('Conta para receber: ')
                    y = find_account()
                    if y is None:
                        print('Essa conta não existe')
                        break
                    account.transfer_cash(transfer_value, y)
                else:
                    print('saldo inválido para transação')
            if option == '5':
                break
            if option == '6':
                exit()
    if x == '2':
         new_name = Person(input('Nome: '))
         inicial_amount = input('Inicial amount: ')
         new_account = Account(str(random.randint(0,100)), str(random.randint(0,100)), inicial_amount, new_name)
         accounts_list.append(new_account)
         print('New branch code: ', new_account.branch_code, '\nNew number account: ', new_account.number_account)








