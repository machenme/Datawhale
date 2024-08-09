def selection_sort(data):
    compile_count_list = []
    shift_count_list = []
    # pass_num 代表未排序的右边界
    for pass_num in range(len(data) - 1, 0, -1):
        compile_count_list.append(pass_num)
        position_largest = 0
        # 找到左侧未排序里面最大的数
        for i in range(1, pass_num + 1):
            if data[i] > data[position_largest]:
                position_largest = i
        # 把最大的数放到左侧最右边,完成一次选择排序
        data[position_largest], data[i] = data[i], data[position_largest]
        shift_count_list.append(1)

    return (compile_count_list, shift_count_list)


# numbers = [70, 48, 54, 79, 33]
# result = selection_sort(numbers)
# print(result)
"""
# 冒泡排序
# 原始序列
[57, 61, 83, 68, 11, 12]
# 排序过程
1. [57, 61, 68, 11, 12, 83]
2. [57, 61, 11, 12, 68, 83]
3. [57, 11, 12, 61, 68, 83]
4. [11, 12, 57, 61, 68, 83]
"""


# def bubble_sort(data):
#     # 设定左侧边界
#     compile_count_list = []
#     shift_count_list = []
#     for pass_num in range(len(data) - 1, 0, -1):
#         compile_count_list.append(pass_num)
#         shift_time = 0
#         for i in range(0, pass_num):
#             if data[i] > data[i + 1]:
#                 data[i], data[i + 1] = data[i + 1], data[i]
#                 shift_time += 1
#         shift_count_list.append(shift_time)

#     return (compile_count_list, shift_count_list)


# numbers = [92, 33, 63, 6, 66, 77, 74, 51, 30, 86]
# result = bubble_sort(numbers)
# print(result)

"""
# 选择排序
# 原始序列
[54, 36, 60, 97, 82, 63]

# 排序过程

[36, 54, 60, 97, 82, 63]

[36, 54, 60, 97, 82, 63]

[36, 54, 60, 97, 82, 63]

[36, 54, 60, 82, 97, 63]

[36, 54, 60, 82, 97, 63]
"""


def compare(value, item_to_insert, counts_list):
    counts_list[-1] += 1  # Add 1 to number of comparisons
    return value > item_to_insert


def insertion_sort(a_list):
    compile_count_list = []
    shift_count_list = []
    # 第一个数不需要比较,默认就是左侧区域,因此从第二个数开始比较
    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]

        i = index - 1
        compile_count_list.append(0)
        shift_time = 0
        while i >= 0 and compare(a_list[i], item_to_insert, compile_count_list):

            a_list[i + 1] = a_list[i]
            i -= 1
            shift_time += 1
        # compile_count_list.append(compare_time)
        shift_count_list.append(shift_time)

        a_list[i + 1] = item_to_insert
    return (compile_count_list, shift_count_list)


# numbers = [50, 63, 11, 79, 22, 70, 65, 39, 97, 48]
# result = insertion_sort(numbers)
# print(result)

# numbers = [92, 86, 77, 66, 51, 42, 33, 23]
# result = insertion_sort(numbers)
# print(result)


def bubble_sort(data):
    element_num = len(data)
    compile_count_list = []
    shift_count_list = []
    for pass_num in range(len(data) - 1, 0, -1):
        compile_count_list.append(pass_num)
        shift_time = 0
        for i in range(0, pass_num):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                shift_time += 1
        shift_count_list.append(shift_time)

    return (element_num, sum(compile_count_list), sum(shift_count_list))


def bubble_sort_fast(data):
    element_num = len(data)
    compile_count_list = []
    shift_count_list = []
    for pass_num in range(len(data) - 1, 0, -1):
        compile_count_list.append(pass_num)
        shift_time = 0
        for i in range(0, pass_num):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                shift_time += 1
        if shift_time == 0:
            break
        shift_count_list.append(shift_time)

    return (element_num, sum(compile_count_list), sum(shift_count_list))


# d1 = [12, 15, 19, 37, 39]
# result1 = bubble_sort(d1)
# print(
#     "Normal Bubble Sort: Length: {} Comparisons: {} Swaps: {}".format(
#         result1[0], result1[1], result1[2]
#     )
# )
# d2 = [12, 15, 19, 37, 39]
# result2 = bubble_sort_fast(d2)
# print(
#     "Fast Bubble Sort: Length: {} Comparisons: {} Swaps: {}".format(
#         result2[0], result2[1], result2[2]
#     )
# )


"""
线性搜索
"""


def linear_search(numbers, target_number):
    compare_count = 0
    for number in numbers:
        compare_count += 1
        if number == target_number:
            return (True, compare_count)
    return (False, compare_count)


# result = linear_search([54, 26, 93, 17, 77, 20], 32)
# print("Found: {} Comparisons: {}".format(result[0], result[1]))
# print(type(result))


# result = linear_search([93, 54, 78, 18, 61, 13, 36, 42, 16, 60, 58, 92], 61)
# print("Found: {} Comparisons: {}".format(result[0], result[1]))


def linear_search_sorted(numbers, target_number):
    numbers = sorted(numbers)
    compare_count = 0
    for number in numbers:
        compare_count += 1
        if number == target_number:
            return (True, compare_count)
        if number > target_number:
            break
    return (False, compare_count)


# result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 4)
# print(type(result))
# print("Found: {} Equality Comparisons: {}".format(result[0], result[1]))

# result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 6)
# print("Found: {} Equality Comparisons: {}".format(result[0], result[1]))


"""
二分查找

[10, 21, 28, 32, 45, 58, 65, 76, 80, 81, 88, 92] find 32
 0   1   2   3   4   5   6   7   8   9   10  11

第一次mid = (0 + 11) // 2 == 5
判断32 < 58 保留左侧

[10, 21, 28, 32, 45]
 0   1   2   3   4 

第二次mid = (0 + 4) // 2 == 2

判断 28 < 32

[32, 45]
 3   4

第三次mid = (3 + 4) // 2 == 3

32 == 32

完成
"""


def binary_search(names_list, target_name):
    left_index = 0
    right_index = len(names_list) - 1
    mid_index = (left_index + right_index) // 2
    while left_index <= right_index:
        print(f"left: {left_index}, mid: {mid_index}, right: {right_index}")
        if target_name == names_list[mid_index]:
            return True
        elif target_name < names_list[mid_index]:
            right_index = mid_index - 1
            mid_index = (left_index + right_index) // 2
        else:
            left_index = mid_index + 1
            mid_index = (left_index + right_index) // 2
        if left_index > right_index:
            return False


my_list = [
    "Alexandra",
    "Auckland",
    "Blenheim",
    "Chatham Islands",
    "Christchurch",
    "Dunedin",
    "Gisborne",
    "Hamilton",
    "Hokitika",
    "Invercargill",
    "Kaikoura",
    "Kaitaia",
    "Lake Tekapo",
    "Manapouri",
    "Masterton",
    "Milford Sound",
    "Mt Cook",
    "Napier",
    "Nelson",
    "New Plymouth",
    "Palmerston North",
    "Queenstown",
    "Rotorua",
    "Taupo",
    "Tauranga",
    "Timaru",
    "Wanganui",
    "Wellington",
    "Westport",
    "Whangarei",
]
print(binary_search(my_list, "Milford Sound"))
