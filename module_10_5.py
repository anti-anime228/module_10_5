import multiprocessing
import datetime

# file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
file_list = [f'./file {number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []
    try:
        with open(name, 'r') as file:
            while True:
                line = file.readline()
                if line == '\n':
                    break
                elif not line:
                    break
                else:
                    all_data.append(line)
    except:
        print("Что-то пошло не так... Ошибка произошла.")
    finally:
        pass
    return all_data

# if __name__ == "__main__":
#     with multiprocessing.Pool(processes=4) as pool:
#         start = datetime.datetime.now()
#         pool.map(read_info, file_list)
#     end = datetime.datetime.now()
#     print(end - start)


# for filename in file_list:
#     start = datetime.datetime.now()
#     read_info(filename)
#     end = datetime.datetime.now()
#     res = end - start
#     print(f'Время выполнения для {filename}: {res}')
