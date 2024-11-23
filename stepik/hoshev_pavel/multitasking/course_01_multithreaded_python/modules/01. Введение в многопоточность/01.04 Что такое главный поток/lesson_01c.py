"""
19.11.2024
"""

import threading as thr

# Получить ссылку на главный поток;
main_thread: thr.Thread = thr.main_thread()

# Вывести информацию о главном потоке;
print(
    f"Имя главного потока: {main_thread.name}",
    f"Является ли главный поток демоническим: {main_thread.daemon}",
    sep="\n",
)
