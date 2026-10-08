import heapq
from collections import Counter
from collections import defaultdict
import re

def get_words(text):
    words = re.findall(r"[А-Яа-яЁё]+", text.lower())
    return [word for word in words if len(word) > 3]

def top_k(words, k):
    freq = Counter(words)

    heap = []

    for word, count in freq.items():
        heapq.heappush(heap, (count, word))

        if len(heap) > k:
            heapq.heappop(heap)

    return sorted(heap, reverse=True)

def read_book(filename):
    with open("desyat-negrityat.txt", "r", encoding="utf-8") as file:
        text = file.read()

    return get_words(text)

def find_and_print_anagrams(text):
    words = re.findall(r"[А-Яа-яЁё]+", text.lower())
    anagram_dict = defaultdict(set)
    for word in words:
        if len(word) > 1:
            key = "".join(sorted(word))
            anagram_dict[key].add(word)
    found = False
    for group in anagram_dict.values():
        if len(group) > 1:
            print(group)
            found = True
            
with open("desyat-negrityat.txt", "r", encoding="utf-8") as file:
    text = file.read()
    find_and_print_anagrams(text)

def show_top(book_name, words, k):
    print("\n", book_name)

    top = top_k(words, k)

    for count, word in top:
        print(word, "-", count)

    return set(word for count, word in top)

# book1 = read_book("desyat-negrityat.txt")
# book2 = read_book("smert-na-nile.txt")
# book3 = read_book("ubiystvo-v-vostochnom-ekspresse.txt")

# top1 = show_top("Десять негритят", book1, 10)
# top2 = show_top("Смерть на Ниле", book2, 10)
# top3 = show_top("Убийство в Восточном экспрессе", book3, 10)

# print("\nОбщие слова:")

# print("Десять негритят + Смерть на Ниле:",
#       top1 & top2)

# print("Десять негритят + Восточный экспресс:",
#       top1 & top3)

# print("Смерть на Ниле + Восточный экспресс:",
#       top2 & top3)

# print("Во всех трех книгах:",
#       top1 & top2 & top3)