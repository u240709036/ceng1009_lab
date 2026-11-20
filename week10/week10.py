# myList = [76, 92.3, "hello", True, 4, 76]
#
# print(myList)
# myList.append(76)
# myList.append("apple")
#
# print(myList)
# myList.insert(3, "cat")
# print(myList)
#
# myList.insert(0, 99)
# print(myList)
#
# print(myList.index("hello"))
#
# print(myList.count(76))
#
# myList.remove(76)
# print(myList)
#
# myList.pop(myList.index(True))
# print(myList)



#
# def sum_of_squares(numbers):
#     sum = 0
#
#     for number in numbers:
#         sum += number **2
#     return sum
#
# myList =[2,3,4]
# print(sum_of_squares(myList))
#




# def sum_evens(num_list):
#     sum = 0
#     for num in num_list:
#         if num % 2 == 0:
#             sum += num
#     return sum
#
# print(sum_evens([1,2,3,4,5,6,7,8,9,10]))




# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#
#     return counter
#
# print(count_five_letter(['hello', 'world', 'world', 'world', 'world', 'ali']))




# def sum_until_even(num_list):
#     total = 0
#     for num in num_list:
#         if num % 2 == 0:
#             break
#         total += num
#     return total
# print(sum_until_even([1, 3, 5, 6, 7]))




# def count_words(words):
#     count = 0
#     for word in words:
#         count +=1
#         if word =='sam':
#             break
#     return count
#
# print(count_words(['samed','mehmet','ahmed','ali',"micheal","sam", "süleyman"]))




# def replace(s, old, new):
#     pieces = s.split(old)
#     print(pieces)
#     print(new.join(pieces))
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual == expected:
#         print("PASSED")
#     else:
#         print("FAILED")
#
# test(replace('Mississippi', "i", "I"), 'MIssIssIppI')





def highNumber(num_List):
    max_val= num_List[0]
    for num in num_List:
        if num > max_val:
            max_val = num

    return max_val
myList = [1,-2,3,4,-5,12,7,16,16,15]
print(highNumber(myList))







