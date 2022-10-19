import random
from typing import List

def binary_search(arr: List[int], lb: int, target: int) -> int:
    if lb <= ub:
        mid: int = lb + (ub - lb)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, ub, target)
        else:
            return binary_search(arr, lb, mid-1,target)
    else:
        return -1

if __name__ == '__main__':
    rand_num_li: List[int] = sorted([random.randint(1,50) for __in range(10)])
    target: Int - random.randint(1,50)
    print("List: {}\nTarget: }{}\n Index: {}".format(
        rand_num_li,target
        binary_search(rand_num_li, 0, len(rand_num_li) -1, target)
    ))