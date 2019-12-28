val1 = ("A" if True else "B")
print(val1)
val2 = ("A" if False else "B")
print(val2)

#########################
# Dictionary操作
#########################
dict = {}
s = "abcabcbb"
for i, e in enumerate(s):
    dict[i] = e
print(dict)
# OUT: {0: 'a', 1: 'b', 2: 'c', 3: 'a', 4: 'b', 5: 'c', 6: 'b', 7: 'b'}


if 1 in dict:  # 預設只能在dict中找key是否存在
    print('Y')
else:
    print('N')

print(dict.keys())
# OUT: dict_keys([0, 1, 2, 3, 4, 5, 6, 7])
print(dict.values())
# OUT: dict_values(['a', 'b', 'c', 'a', 'b', 'c', 'b', 'b'])

if 'a' in dict.values():  # 在values中尋找值是否存在
    print('Y')
else:
    print('N')
# if else可改寫如下
print('Y') if 'a' in dict.values() else print('N')

dict5 = {}
for k,v in dict4.items():
    dict5[v]=k

#########################
# 物件 vs 記憶體位置
#########################

max_so_far = curr_max = start = 0  # 三個變數還有 0 都在同一個記憶體位址
print(id(max_so_far))
print(id(curr_max))
print(id(start))
print(start == curr_max)

start = 1  # start另存到新的記憶體位置
print(curr_max)
print(id(max_so_far))
print(id(curr_max))
print(id(start))
print(start == curr_max)

start = 0
print(curr_max)
print(id(max_so_far))
print(id(curr_max))
print(id(start))
print(start == curr_max)

print(id(0))

#########################
# sorted List
#########################

nums1 = [1, 3]
nums2 = [2]
nums3 = nums1 + nums2
print('nums3', nums3)  # nums3 [1, 3, 2]
num4 = sorted(nums3)
print(num4)


#########################
# define List min function
# Keys are unique within a dictionary while values may not be.
#########################
def minList(a):
    min_so_far = a[0]
    Len = len(a)
    for i in range(1, Len):
        if min_so_far >= a[i]:
            min_so_far = a[i]
    return min_so_far


nums5 = [1, -9, 0, -5.5, 1]
print(minList(nums5))


def sortList(a) -> list:
    sortedList = []
    Len = len(a)
    if Len != 0:
        while True:
            min_so_far = minList(a)  # min element
            sortedList.append(min_so_far)  # add to new list
            idx = a.index(min_so_far)  # find out index of min in original list
            del a[idx]  # delete min in original list
            if len(a) == 0:
                break
    else:
        print('List is empty')
    return sortedList

print(sortList(nums5))

