# Import the external library
from colorama import Fore, Style, init
# Initialize colorama (required for Windows compatibility)
init()

# Эта библиотека нужна для изменения цвета текста и стилизации вывода в терминале.
# Она помогает сделать логи, ошибки или важные уведомления более заметными для пользователя.

# 2. Использовать эту библиотеку в коде
print(Fore.GREEN + "Привет! Этот текст успешно покрашен в зеленый цвет." + Style.RESET_ALL)
print(Fore.RED + "А это сообщение об ошибке красного цвета!" + Style.RESET_ALL)
print(Fore.CYAN + "Задание выполнено успешно." + Style.RESET_ALL)