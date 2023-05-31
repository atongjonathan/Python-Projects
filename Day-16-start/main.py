from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Celebrity", ["Selena Gomez", "Ariana Grande", "Hailey Baldwin"])
table.add_column("Followers", ["417", "380", "10"])
table.align = 'l'

table.add_row(['Cristiano Ronaldo', '500'])
print(table)