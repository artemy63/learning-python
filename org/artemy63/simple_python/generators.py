def my_own_range_generator(start = 0, end = 13, step = 1):
    current_item = start
    while current_item < end:
        yield current_item
        current_item += step


my_own_generator_test_1 = list(my_own_range_generator())
print(my_own_generator_test_1)

my_own_generator_test_2 = list(my_own_range_generator(1, 6))
print(my_own_generator_test_2)

# doesn't work because current_item < end: validation fails
my_own_generator_test_3 = list(my_own_range_generator(6, 1, -1))
print(my_own_generator_test_3)

my_own_generator_test_4 = list(my_own_range_generator(1, 10, 3))
print(my_own_generator_test_4)
