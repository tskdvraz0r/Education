"""
19.11.2024
"""
import threading as thr


# Получить текущий поток;
current_thread: thr.Thread = thr.current_thread()

# Получить главный поток;
main_thread: thr.Thread = thr.main_thread()

# Проверить, является ли текущий поток главным и вывести свойства главного потока;
if current_thread is main_thread:
    print(f"Главный поток: имя={current_thread.name}, daemon={current_thread.daemon}, id={current_thread.ident}")
else:
    print("Это не главный поток!")