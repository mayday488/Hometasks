#Upper case function:
def str_up (str_1):
    str_1 = str_1.upper()
    return str_1

#Lower case function:
def lower_case (str_2):
    return str_2.lower()

List_upper = ["lorem","ipsum","dolor","sit","amet","consectetur","adipiscing","elit"]
List_lower = ["LOREM","IPSUM","DOLOR","SIT","AMET","CONSECTETUR","ADIPISCING","ELIT"]

new_list_upper = list(map(str_up,List_upper))
print (new_list_upper)
new_list_lower = list(map(lower_case,List_lower))
print (new_list_lower)