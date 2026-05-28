nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)
print((lambda x, y: x + y)(5, 3))  # Виведе 8

numbers = [1, 2, 3, 4, 5]
for i in map(lambda x: x ** 2, numbers):
    print(i)
squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)

nums1 = [1, 2, 3, 4]
nums2 = [4, 5, 6, 7]
nums3 = [8, 10, 15, 20]
sum_nums = map(lambda x, y, z: x + y + z, nums1, nums2, nums3)
print(list(sum_nums))

even_nums = filter(lambda x: x % 2 == 0, range(1, 11))
print(list(even_nums))

some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА існує з 1992 року'
new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)
