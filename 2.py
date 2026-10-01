# numbers = [1,2,2,2,2,4,6] 
# target = 2
# def first_sort(array,target):
#     array.sort()
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         middle = (left + right) // 2
#         # if array[middle] == target:
#         #     right = middle + 1
#         if array[middle] < target:
#             left = middle + 1
#         else:
#             right = middle
#     return left
# res_task = first_sort(numbers, target)
# print(res_task)

# numbers = [30,20,10,40] 
# target = 45
# def second_task(array,target):
#     array.sort()
#     left = 0
#     right = len(array) 
#     while left < right:
#         middle = (left + right) // 2
#         if array[middle] < target:
#             left = middle + 1
#         else:
#             right = middle
#     return left
# res_task = second_task(numbers, target)
# print(res_task)

# numbers = [1,2,4,7,11]
# target = 11
# def sorted_to_eleven(array,target):
#     array.sort()
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         middle = array[left] + array[right]
#         if middle == target:
#             return [left, right]

#         if middle < target:
#             left +=1
#         else:
#             right -=1
#     return left
# res_task = sorted_to_eleven(numbers, target)
# print(res_task)   

# numbers = [1,4,8,3,7,11,25,40] 
# target = 7
# def binary_sorted(array, target):
#     array.sort()
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         middle = (left + right) // 2
#         if array[middle] == target:
#             return middle
#         if array[middle] < target:
#             left = middle + 1
#         else:
#             right = middle
#     return left
# res_task = binary_sorted(numbers, target)
# print(res_task)

# text = "геййег"
# textp = "шалаш"
# taxtw = "хакер в реКАх"
# def palindrom(text):
#     text = text.lower().replace(" ","")
#     left = 0
#     right = len(text) -1
#     while left < right:
#         if text[left] != text[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# print(palindrom(text))
# print(palindrom(textp))
# print(palindrom(taxtw))
