# a = int(input())
# b = int(input())
#
# res = []
#
# for i in range(a,b+1):
#     if i % 2 == 0:
#         res.append(i)
#
# print(*res)

##2
# a = int(input())
# for i in range(1, a+1):
#     if a % i == 0:
#         print(i)
#         break

##3
# a = int(input())
# res = []
# for i in range(1, a+1):
#     if a % i == 0:
#         res.append(i)


# print(*res)
## 4
# a = int(input())
# res = []
#
# for i in range(a):
#     res.append(int(input()))
#
# print(sum(res))

#5

# a = int(input())
# res = []
# ten_system = []
# while a > 0:
#     res.append(a % 10)
#     a //= 10
#
#
# for i in range(len(res)):
#     ten_system.append(res[i] * (2**i))
#
# print(sum(ten_system))


##6
# def power(a, b):
#     return a ** b
#
#
# a = float(input())
# b = float(input())
# print(power(a, b))


##7
# def vote(res):
#
#     if sum(res) >= 2:
#         print(1)
#     else:
#         print(0)
#
#
# res = [bool(int(x)) for x in input().split()]
# vote(res)
# # c = bool(int(input()))
# # b = bool(int(input()))
# # c = bool(int(input()))
# vote(res)
# ## HERE I TRIED UNDERSTAND THE LOGIC
# # print(type(b), a, b)
# # print
# # # vote(a, b, c)
# # res = [a, b, c]
# # print(sum(res))

## 8


# first_dop
# a = [int(x) for x in input().split()]
# N = len(a)
# for i in range(N-1):
#     for j in range(N-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#
# print(a)




