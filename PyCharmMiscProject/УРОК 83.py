keywords = """False class from or
None continue global pass
True def if raise
and del import return
as elif in try
assert else is while
async except lambda with
await finally nonlocal yield
break for not""".split()

stats = {}

for keyword in keywords:
    answer = input(f'Do you know keyword "{keyword}"? (yes/no): ').lower().strip()
    if answer == 'yes' or answer == 'да':
        stats[keyword] = 1
    else:
        stats[keyword] = 0

total_words = len(keywords)
print(f"\n1) Общее количество слов: {total_words}")

passed_count = sum(stats.values())
failed_count = total_words - passed_count
print(f"2) Пройдено: {passed_count}, Не пройдено: {failed_count}")

sorted_stats = sorted(stats.items(), key=lambda item: item[1])
print("3) Список слов (0 - не знаю, 1 - знаю):")
for word, score in sorted_stats:
    print(f"   {word}: {score}")

passed_percentage = (passed_count / total_words) * 100
failed_percentage = (failed_count / total_words) * 100
print(f"4) Процент пройденного: {passed_percentage:.2f}%")
print(f"   Процент не пройденного: {failed_percentage:.2f}%")