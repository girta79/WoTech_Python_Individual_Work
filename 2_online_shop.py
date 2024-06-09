# INDIVIDUAL WORK
# Develop a simple prototype for an online shop
# 1. Define classes Client, Items, Transaction
# 2. Write the logic so that each client can purchase one or several items in a single transaction
# 3. Make a printout of data with nested loops
# 4. The program should print out:
#  - all clients
#  - all transactions of a client
#  - all items purchased in each transaction of the client

class Client:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Transaction:
    def __init__(self, id, client, items):
        self.id = id
        self.client = client
        self.items = items
        self.total = sum(item.price for item in items)

item1 = Item(1, 'Laptop', 1549.00)
item2 = Item(2, 'Smartphone', 1000.00)
item3 = Item(3, 'Tablet', 650.00)
item4 = Item(4, 'Watch', 500.00)
item5 = Item(5, 'Airpod', 150.00)

client1 = Client(1, 'Jane Juurikas')
client2 = Client(2, 'Anne Liiv')
client3 = Client(3, 'Robert Raud')
client4 = Client(4, 'Siim Sinine')
client5 = Client(5, 'Lauri Hell')

clients = [client1, client2, client3, client4, client5]

transaction1 = Transaction(1, client1, [item1, item3])
transaction2 = Transaction(2, client2, [item2])
transaction3 = Transaction(3, client3, [item5])
transaction4 = Transaction(4, client4, [item3, item4])
transaction5 = Transaction(5, client5, [item4])

client1.add_transaction(transaction1)
client2.add_transaction(transaction2)
client3.add_transaction(transaction3)
client4.add_transaction(transaction4)
client5.add_transaction(transaction5)

print("All clients:")
for client in clients:
    print(f"Client ID: {client.id}, name: {client.name}")
    print("Transactions:")
    for transaction in client.transactions:
        print(f"  Transaction ID: {transaction.id}, total sum: {transaction.total}€")
        print("  Items:")
        for item in transaction.items:
            print(f"    Item ID: {item.id}, {item.name}, price: {item.price}€")
    print()

