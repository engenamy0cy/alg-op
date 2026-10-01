import random
import time 

window_length = 5
numbers = [random.randint(1, 15) for _ in range(10000)]

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
        best_window = i

end_time = time.time()
time_window = end_time - start_time
print(f"best window: {best_window}")
print(f"max summ: {max_sum_window}")
print(f"time used: {time_window} s.")

