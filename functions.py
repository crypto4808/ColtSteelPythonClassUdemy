# from random import randint
#
#
# def flip_coin(attempts):
#     num = 0
#     while num<attempts:
#         num +=1
#         rand_flip = randint(0,1)
#         # print(rand_flip)
#         if rand_flip ==0:
#             print(f"ATTEMPT#{num} =HEADS")
#         else:
#             print(f"ATTEMPT#{num} =TAILS")
#
# flip_coin(10)


def count_sevens(*args):
    return args.count(7)

result1 = count_sevens(1,4,7)
print(f"Number of 7s is {result1}")
nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
result2 = count_sevens(*nums)

print(f"Number of 7s is {result2}")
