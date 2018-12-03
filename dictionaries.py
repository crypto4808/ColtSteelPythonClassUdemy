# # This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
#
# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }
# # food = 'tea cake'
# # YOUR CODE GOES BELOW:
# if food in bakery_stock:
#     print("{} items left!".format(bakery_stock[food]))
# else:
#     print("We don't make that")




# def calculate(**kwargs):
#     operation_lookup={
#         'sum' : kwargs.get('first',0) + kwargs.get('second',0),
#         'divide': kwargs.get('first',0) + kwargs.get('second',0)
#     }
#     is_float = kwargs.get('make_float', False)

#     operation_value = operation_lookup[kwargs.get('operation',' ')]
#     if is_float:
#         print('Start Function')

#         final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
#     else:
#         final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
#     return final



# print(calculate(make_float=True, operation='divide', first=3.5, second=5))# "The result is 0.7"



def statistics(file_name):
    with open(file_name,'r') as f:
        data = f.readlines()

    return {
        "lines": len(data),
        "words": len(data.split()),
        "characters":
    }



