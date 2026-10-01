import random
import time 

window_length = 5
numbers = [random.randint(1, 15) for _ in range(10000000)]

print(f"создан массив из {len(numbers)} элементов")

start_time = time.time()

max_sum_window = 0
best_window = []

# for i in range(len(numbers) - window_length + 1):
#     current_window = numbers[i : i + window_length]
#     current_sum = sum(current_window)
for i in range(len(numbers) - window_length + 1):
    current_sum = 0
    for j in range(window_length):
        current_sum += numbers[i + j]

    if current_sum > max_sum_window:
        max_sum_window = current_sum
        best_window = numbers[i : i + window_length]

end_time = time.time()
time_window = end_time - start_time
print(best_window)
print(max_sum_window)
print(time_window)




# def max_sum_window(array,window_length):
#     current_sum = sum(array[:window_length])
#     best_sum = current_sum
#     for right in range(window_length,len(array)):
#         left_leaving = right - window_length
#         current_sum += array[right] - array[left_leaving]
#         best_sum = max(best_sum,current_sum)
#     return best_sum
# start_time = time.time()
# result = max_sum_window(numbers, window_length)
# end_time = time.time()
# time_window = end_time - start_time
# print(f"максимальная сумма окна длины:{window_length}")
# print(f"{time_window} сек")