import threading
import time

# 定义一个函数，用于线程执行的任务
def print_numbers():
    for i in range(5):
        time.sleep(i)
        print(i)

# 定义另一个函数，用于线程执行的任务
def print_letters():
    for letter in 'ABCDE':
        time.sleep(3)
        print(letter)

# 创建线程对象，target是线程要执行的函数名，args是传递给函数的参数（以元组形式）
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# 启动线程
thread1.start()
thread2.start()

# 等待所有线程完成
thread1.join()
thread2.join()

print("两个线程已完成执行。")