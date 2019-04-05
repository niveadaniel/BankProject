import random
import sqlite3

conn = sqlite3.connect('banktables.db')
c = conn.cursor()

def find_account():
    branch_code = input('Branch code: ')
    number_account = input('Number account: ')
    for account in accounts_list:
        if account.branch_code == branch_code and account.number_account == number_account:
            return account


class Address(object):

    def __init__(self, user_id, street, number, city, country, id = None):
        self.id = int(id)
        self.street = street
        self.number = number
        self.city = city
        self.country = country
        self.user_id = int(user_id)

    @staticmethod
    def create_table():
        c.execute('''create table if not exists address (
                        id integer primary key autoincrement not null,
                        user_id integer not null,
                        street text not null,
                        number integer not null,
                        city text not null,
                        country text not null,
                        foreign key (person_id) references person(id)''')
        conn.commit()

    def save(self):
        if self.id != None:
            c.execute(''' update address set 
                        street=?, number=?, city=?, country=? where
                        id=? ''', (self.street, self.number, self.city, self.country, self.id))
            conn.commit()
        else:
            c.execute('''insert into address (user_id, street, number, city, country) values
                            (?, ?, ?, ?, ?)''', (self.user_id, self.street, self.number, self.city, self.country,))
            self.id = c.lastrowid
            conn.commit()

    @staticmethod
    def find(id):
        c.execute("select * from person where id = '%s'" % id)
        r = c.fetchone()
        person = Person(id=r.id, name=r.name, age=r.age)
        return person

class Account(object):

    def __init__(self, user_id, branch_code, number_account, amount, id = None):
        self.id = id
        self.branch_code = branch_code
        self.number_account = number_account
        self.amount = float(amount)
        self.user_id = int(user_id)

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

    @staticmethod
    def create_table():
        c.execute('''create table if not exists accounts ( 
                        id integer primary key autoincrement not null,
                        user_id integer not null, branch_code integer not null,
                        number_account integer not null, amount numeric not null, 
                        foreign key (person_id) references person(id))''')
        conn.commit()

    def save(self):
        if self.id != None:
            c.execute('''update accounts set 
                        branch_code=?, number_account=?, amount=? where 
                        id=? ''', (self.branch_code, self.number_account, self.amount, self.id))
            conn.commit()
        else:
            c.execute('''insert into accounts (user_id, branch_code, number_account, amount) values 
                            (?, ?, ?, ?)''',(self.user_id, self.branch_code, self.number_account, self.amount))
            self.id = c.lastrowid
            conn.commit()

    @staticmethod
    def find(id):
        c.execute("select * from person where id = '%s'" % id)
        r = c.fetchone()
        person = Person(id=r.id, name=r.name, age=r.age)
        return person


class Person(object):

    def __init__(self, name, age, id = None):
        self.id = id
        self.age = int(age)
        self.name = name

    @staticmethod
    def create_table():
        c.execute('''create table if not exists person (
                        id integer primary key autoincrement not null,
                        name text not null,
                        age integer not null)''')
        conn.commit()

    def save(self):
        if self.id != None:
            c.execute('''update person set 
                            name=?, age=? where 
                            id=? ''', (self.name, self.age, self.id))
        else:
            conn.commit()
            c.execute('insert into person (name, age) values (?, ?)', (self.name, self.age))
            self.id = c.lastrowid
            conn.commit()

Person.create_table()
Account.create_table()
#nivea = Person('Nivea', 21)
#nivea.save()
#daniel = Person('Daniel', 38)
#daniel.save()
#nivea_account = Account(1, '17', '15', 3000)
#nivea_account.save()
#daniel_account = Account(2, '34', '12', 5700)
#daniel_account.save()
c.execute('select * from person')
rows = c.fetchall()
print(rows)
#accounts_list = [nivea_account, daniel_account]
option = None
while True:
    account_found = False
    x = input(('Olá, digite 1 para entrar em sua conta, ou digite 2 para abrir uma conta: '))
    if x == '1':
        account = find_account()
        if account is None:
            print('Essa conta não existe')
        else:
            account_found = True
            print('bem vindo,', account.person)
        while account_found == True:
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
         new_person = Person(name=input('Nome: '), age=input('Idade: '))
         new_person.save()
         new_account = Account(user_id=new_person.id, branch_code=str(random.randint(0,100)),
                               number_account=str(random.randint(0,100)), amount=input('Inicial amount: '))
         new_account.save()
         #accounts_list.append(new_account)
         print('New branch code: ', new_account.branch_code, '\nNew number account: ', new_account.number_account)








