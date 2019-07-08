sales_file = open('D:\Work\Crypto\data\chicken.txt' , 'r')

day = 0
amount = 0
total = 0

for sale in sales_file:
    data = sale.strip().split(': ')
    amount = int(data[1])

    total = total + amount
    day = day + 1
sales_file.close()

print(total/ day)