import time

sizes=[1000,10000,100000,1000000]

for size in sizes:
    numbers_list=list(range(size))
    numbers_set=set(numbers_list)

    target =size-1

    start = time.perf_counter()
    target in numbers_list
    end = time.perf_counter()
    list_time = end - start

    start = time.perf_counter()
    target in numbers_set
    end = time.perf_counter()
    set_time = end - start

    print("Size:", size)
    print("List lookup:", list_time)
    print("Set lookup:", set_time)
    print()