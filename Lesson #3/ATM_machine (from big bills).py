b = [1000,500,200,100,50,20,10,5]
n = int(input('Amount of money: '))
operation_results = []
if n < 0:
    print ("Invalid value: the amount must be positive")
elif n <= 5:
    print ("Invalid value: the sum must be at least 5")
else:
    pass

while n >= 5:
    for i in b:
        if n // i:
            print(n // i, ' x ', i)
            n %= i
    
print('Unfortunately, this sum cannot be withdrawn: ' , n)