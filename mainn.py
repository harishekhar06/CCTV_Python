# for i in range(4):
#     for j in range(4-i):
#         print("#", end="")
#     print()
# nums = [12,18,34,32,44]
# for num in nums:
#     if num % 5 == 0:
#         print(num)
# else:
#     print("Not found")

# num = 3
# for i in range(2,num):
#     if num % i ==0:
#         print("Prime number")
#         break
# else:
#     print("Not a prime number")
# from array import  *
# valus = array('i', [5,-8,7,9,60])
#
# for e in valus:
#     print(e)
# def freq_words():
#     inp = input("Enter the string: ")
#     li = inp.split()
#     d = {}
#
#     for i in li:
#         if i not in d.keys():
#             d[i] = 0
#         d[i] = d[i] + 1
#     print(d)
# freq_words()
def missing():
    a = [1, 2, 4, 5, 6, 7]
    n = a[-1]
    sum_1 = 0
    total = n*(n+1)//2
    res = total-sum_1
    print(res)

missing()