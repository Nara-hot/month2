keywords = """False               class               from                or None                continue            global              pass True                def                 if                  raise and                 del                 import              return as                  elif                in                  try assert              else                is                  while async               except              lambda              with await               finally             nonlocal            yield break               for                 not""".split()

# Словарь для хранения результатов: {слово: оценка}
results = {}

for keyword in keywords:
    answer = input(f'' "{keyword}"? (да/нет): ').lower().strip()
    # Если ответ "да" — 1 (пройдено), иначе 0 (не пройдено)
    results[keyword] = 1 if answer == 'да' else 0

# 1) Общее количество слов
total_words = len(keywords)

# 2) Количество пройденных и не пройденных слов
passed_count = sum(results.values())
not_passed_count = total_words - passed_count

# 3) Сортировка словаря по значению (от 0 к 1)
# Сначала выведутся те, что "не знаю" (0), затем "знаю" (1)
sorted_results = sorted(results.items(), key=lambda item: item[1])

# 4) Процентное соотношение
passed_percent = (passed_count / total_words) * 100
not_passed_percent = (not_passed_count / total_words) * 100

# Вывод результатов
print("\n--- Отчет по домашнему заданию №8 ---")
print(f"1) Общее количество слов: {total_words}")
print(f"2) Пройдено: {passed_count}, Не пройдено: {not_passed_count}")

print("3) Список слов по мере освоения:")
for word, score in sorted_results:
    status = "Освоено" if score == 1 else "Нужно выучить"
    print(f"   - {word}: {status}")

print(f"4) Процентное соотношение: Пройдено {passed_percent:.1f}% / Не пройдено {not_passed_percent:.1f}%")
