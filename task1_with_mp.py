"""
HW 25
"""
import random
import time
import multiprocessing

def create_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_
    """
    random_number = random.randint(1, 100)
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(str(random_number))
    time.sleep(1)
def create_files_mp(num_files):
    """_summary_

    Args:
        num_files (_type_): _description_
    """
    start_time = time.time()
    processes = []
    for i in range(num_files):
        filename = f"output_{i}.txt"
        process = multiprocessing.Process(target=create_file, args=(filename,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Время выполнения для {num_files} файлов: {total_time} секунд')
def main():
    """_summary_
    """
    create_files_mp(1000)

if __name__ == "__main__":
    main()
