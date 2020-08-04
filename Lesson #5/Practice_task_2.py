#Function that multiplies only natural numbers:
def multiply (a):
   if a == 2 or a == 3 or a == 5:
       return a*a
   elif a%2 and a%3 and a%5:
       return a*a
   else:
       return a
   
list_of_numbers = (range(1,10+1))

new_list_of_numbers = list(map(multiply,list_of_numbers))
print (new_list_of_numbers)