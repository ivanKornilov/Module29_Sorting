import random


def bubble_sort(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data) - 1):
            count += 1
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return int(count/2)


def test_sorted():
    data = [random.randint(0, 1000) for i in range(100)]
    data_to_sort = data.copy()
    bubble_sort(data_to_sort)
    if data_to_sort == sorted(data, reverse=True):
        print('OK')
    else:
        print('NOT OK')


def make_observations():
    size = 10
    results = []
    for i in range(100):
        data = [random.randint(0, 1000) for i in range(size)]
        results.append((size, bubble_sort(data)))
        size += 10
    return results


def main():
    test_sorted()
    with open('bubble.csv', 'w') as file:
        file.write(f'size, iterations\n')
        for row in make_observations():
            file.write(f'{row[0]}, {row[1]}\n')
    print('Done!')


if __name__ == '__main__':
    main()