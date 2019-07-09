'''
2048 核心算法
'''


# 1.定义函数，将列表0元素移至末尾.
# [2,0,2,0]  -->[2,2,0,0]
# [2,0,0,2]   -->[2,2,0,0]
# [2,4,0,2]   -->[2,4,2,0]

def move_zero(list01):
    '''
    将0元素删除，末尾增加
    :param list01:
    :return:
    '''
    for item in range(len(list01) - 1, -1, -1):
        if list01[item] == 0:
            del list01[item]
            list01.append(0)
    return list01


list01 = [2, 0, 2, 2]
move_zero(list01)
print(list01)


# 2.定义函数,合并列表中相同元素
# [2,0,2,0]  -->[4,2,0,0]
# [2,0,0,2]   -->[2,2,0,0]
# [2,4,0,2]   -->[2,4,2,0]

def merge_number(list01):
    #
    move_zero(list01)
    # 如果相邻且相同切掉
    for i in range(len(list01) - 1):
        if list01[i] == list01[i + 1]:
            # 合并
            list01[i] += list01[i + 1]
            del list01[i + 1]
            list01.append(0)
            # del list01[i]
            # del list01[i+1]
            # list01[::-1].append(4)
    # return list01


list01 = [2, 2, 0, 2]
merge_number(list01)
print(list01)

'''3.定义函数，向左移动二维列表
[2,2,0,2]
[0,2,0,4]
[2,0,4,2]
[0,4,2,2]
'''


def left_move(map):
    # 将每行传递（二维列表的每个元素）给合并函数
    for row in map:
        # 传递给merge函数的是二维列表的元素（以为列表对象地址）
        # 函数都是操作对象，无需通过返回值返回结果
        merge_number(row)


double_list = [
    [2, 2, 0, 2],
    [0, 2, 0, 4],
    [2, 0, 4, 2],
    [0, 4, 2, 2],
]
left_move(double_list)
print(double_list)

# 定义函数，向右移动
'''4.定义函数，向左移动二维列表
[2,2,0,2]
[0,2,0,4]
[2,0,4,2]
[0,4,2,2]
'''


def right_move(map):
    for i in range(len(map)):
        list_merge = map[i][::-1]
        merge_number(list_merge)
        map[i][::-1] = list_merge


double_list = [
    [2, 2, 0, 2],
    [0, 2, 0, 4],
    [2, 0, 4, 2],
    [0, 4, 2, 2],
]
merge_number(double_list)
print(double_list)

'''
向上移动（从上到下获取列数据，形成一维列表，交给合并方法，恢复）
向下移动（从下到上获取列数据，形成一维列表，交给合并方法，恢复）
'''
list04 = []

# 作业1:向上移动(核心思想:从上到下获取列数据,形成一维列表,交给合并方法,最后恢复)
def move_up(map):
  # 00  10  20  30
  # 01  11  21  31
  for c in range(4):
    list_merge = []
    for r in range(4):
      list_merge.append(map[r][c])

    merge_number(list_merge)

    for r in range(4):
      map[r][c] = list_merge[r]
# 作业2:向下移动(核心思想:从下到上获取列数据,形成一维列表,交给合并方法,最后恢复)
def move_down(map):
  # 30  20  10  00
  for c in range(4):
    list_merge = []
    for r in range(3, -1, -1):
      list_merge.append(map[r][c])

    merge_number(list_merge)

    # list_merge(从左到右) 赋值给 二维列表(从下到上)
    for r in range(3, -1, -1):  # 3 2 1 0
      map[r][c] = list_merge[3 - r]


move_down(double_list)
print(double_list)