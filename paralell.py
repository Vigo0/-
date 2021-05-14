import time
from multiprocessing import Pool


def fibonacci_sequence_of(num):
    first_number = 0
    second_number = 1

    num = int(num)
    if num == 0:
        print("Элемент последовательности {} для номера {}".format(num, num))
    elif num == 1:
        print("Элемент последовательности {} для номера {}".format(num, num))
    else:
        for i in range(1, num):
            new_number = first_number + second_number
            first_number = second_number
            second_number = new_number
        print("Элемент последовательности {} для номера {}".format(num, second_number))


if __name__ == '__main__':
    input_number = input("Введите через запятую номера \n Элемент последовательности : ")
    input_values = []
    input_values = input_number.split(",")
    toc = time.time()

    pool = Pool()

    result = pool.map(fibonacci_sequence_of, input_values)
    tic = time.time()

    time_taken = round((tic - toc) * 1000, 1)
    print("Это заняло {} миллисекунд ".format(time_taken))

    pool.close()
    pool.join()
