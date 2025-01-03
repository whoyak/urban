import multiprocessing
import time


def read_info(name):
    all_data = []
    for file_name in name:
        while True:
            with open(file_name, 'r') as file:
                line = file.readline()
                all_data.append(line)
                if not line:
                    break


if __name__ == "__main__":
    filenames = ["file 1.txt","file 2.txt","file 3.txt","file 4.txt"]
    start = time.time()
    read_info(filenames)
    end = time.time()
    print(f'Линейное выполнение: {end - start} секунд')

    start = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, [filenames for _ in filenames])
    end = time.time()
    print(f'Многопроцессное выполнение: {end - start} секунд')
