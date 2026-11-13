# print("Enter a number: ")
# n=int(input())
#
# def is_Odd(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_Odd(n))



# def is_leap_year(year):
#     if year % 400==0:
#         return True
#     elif year % 100 ==0:
#         return False
#     elif year % 4==0:
#         return True
#     else:
#         return False
#
# print(is_leap_year(2023))





# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#         print(i, total)
#
# print_triangular_numbers(5)




# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(8))





# def reverse(s):
#     result = ""
#     for char in s:
#         result = char + result
#     return result
#
# print(reverse("Hello World"))
#
#
# def reverse_slice(s):
#     return s[::-1]
# print(reverse_slice("Hello World"))





# def remove_all(sub, s):
#     return s.replace(sub, '')
#
# print(remove_all('an', 'banana'))




# def substitute(message, key):
#     # alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     alphabet = "qtgöwertyuıopğüasdfghjklşizxcç"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "abcçdefgğhıijklmnoöprsştuüvyz"
# print(len(key))
# print(substitute("Üfmmö, Dösme!", key))





def remove_dups(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result

print(remove_dups("hello world"))


