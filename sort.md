## 冒泡排序

遍历便利N个元素,从左到右 依次比较 第一个与第二个,如果左边大于右边,就交换二者,然后第二个与第三个比较,以此类推

在一次循环之后,一定能找到第一个最大的数放在最右边

第二次则是遍历N-1个元素,放到倒数第二个

N个元素一共需要比较 N(N-1)/2 次,因此时间复杂度是`O(n^2)`
```python
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

```

### 快速冒泡

在冒泡排序的基础上,如果某次便利没有任何交换,则证明已经完成排序了,可以结束程序了
```python
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

```

## 选择排序

右端是已排序区域，左端是未排序区域。最开始时，已排序区域为空，未排序区域包含整个列表。

在每一轮中，从未排序区域中选择最大的元素，并将其与未排序区域最右边的元素交换，这样该元素就成为了已排序区域的一部分。这个过程持续进行，将未排序区域的边界每次向左移动一个元素，直到未排序区域的长度为1时结束。

## 插入排序

插入排序将列表分为两个区域：左侧已排序，右侧未排序。在每一步中，插入排序都会获取未排序区域的第一个元素，并将其插入到已排序区域中的正确位置。为了将所有 n 个元素放到正确的位置，外部循环必须执行 n - 1 次。

**步骤概述**：
1. **初始化**：将第一个元素视为已排序区域，剩余元素为未排序区域。
2. **插入操作**：
   - 从未排序区域取出第一个元素。
   - 将其与已排序区域中的元素从右向左比较，找到插入的位置。
   - 将元素插入到找到的位置。
3. **更新区域**：
   - 已排序区域增加一个元素，未排序区域减少一个元素。
4. **重复**：直到未排序区域为空。

---

## 二分查找

先从小到大排列,

寻找到中间的数((left+right)//2),如果目标大于中间的数,从中间数到右区间作为新的区间.如果目标小于中间的数,从左区间到中间的数作为新的区间.重复

二分查找的时间复杂度为`O(logn)`