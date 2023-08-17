#  1 ans
def calculate_average():
    average = lambda list1: sum(list1) // len(list1)
    return average


average = calculate_average()
number_list = [2, 4, 6, 8, 10]
print(average(number_list))
#
# 2 ans
def even_numbers(numbers):
    for x in numbers:
        if x % 2 == 0:
            yield x


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_no = even_numbers(numbers)
print(next(even_no))
print(next(even_no))
print(next(even_no))
print(next(even_no))
print(next(even_no))

#   3 ANS
def print_student_details(student_name, additional_details):
    print(student_name, additional_details)


student_data_dict = {"age": 18, "grade": 12, "school": "vps"}
print(print_student_details('abhishek', additional_details=student_data_dict))


print('------------------------------------------------------------')


# 4 ans
def sum_arugments():
    sum = lambda x, y: x + y
    return sum


sums = sum_arugments()
print(sums(50, 60))

# 5 ans
def is_primeno(numbers):
    int(numbers)
    for x in range(2, 11):
        if numbers % x == 0:
            print('it is not prime no')
    else:
        print(' it is a prime')


checking_prime = is_primeno(11)
print(checking_prime)
#
#
# # 6 ans
def reverse_string(string):
    str(string)
    reversing = string[-1::-1]
    return reversing


reversing_string = reverse_string('abhishek')
print(reversing_string)

#
# # # 8 ans
# def fabonacci(c):
#     while c in range(0,):
#         a = 0
#         b = 1
#         c = a + b
#         yield c
#
# abhi = fabonacci(1)
# print(next(abhi))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# 9 ans
def concatenate_strings(firstname, lastname, a, b, c, ):
    return firstname + lastname + a + b + c


joiningstings = concatenate_strings('abhi', 'shek', 'is', 'my', 'name', )
print(joiningstings)


# 10 ans
def find_max_value(list1):
    list1.sort()
    return list1[-1], 'is the maximum value'


list1 = [3000, 100, 200, 300, 400, 2000, 1000]
maximum_value = find_max_value(list1)
print(maximum_value)

# 11 ans
def calculate_sum(nums):
    return sum(nums)


numbers = 1, 2, 3, 4, 5, 6, 7
print(calculate_sum(numbers))
