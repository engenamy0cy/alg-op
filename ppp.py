# def valid_parentherese(text):
#     opening_closing = {")":"(","]":"[","}":"{"}
#     stack = []
#     for char in text:
#         if char in '([{':
#             stack.append(char)
#         elif not stack or stack.pop() != opening_closing[char]:
#             return False
#     return not stack

# print(valid_parentherese("()[]{}"))
# print(valid_parentherese("([)]"))
# print(valid_parentherese("((())"))

# def simplify_path(path):
#     stack = []
#     for part in path.split("/"):
#         if part == "" or part == ".":
#             continue   # пустая и текущая папка ничего не меняют
#         if part == "..":
#             if stack:
#                 stack.pop()  # вышли из последней папки
#         else:
#                 stack.append(part)  # зашли
#     return "/" + "/".join(stack)
# print(simplify_path("a/./b"))

from collections import deque
queue = deque()
queue.append("Анна")
queue.append("Вика")
queue.append("Боря")
first = queue.popleft() #анна
second = queue.popleft()

print(first)
print(second)
print(queue)