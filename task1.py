"""
HW 25
"""
import random
import time

def create_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_
    """
    random_number = random.randint(1, 100)
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(str(random_number))
    time.sleep(1)
start_time = time.time()
for i in range(1000):
    FILENAME = f"output_{i}.txt"
    create_file(FILENAME)
end_time = time.time()
total_time = end_time - start_time
print(f'Время выполнения для 1000 файлов: {total_time} секунд')
