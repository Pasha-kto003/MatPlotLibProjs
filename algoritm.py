def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print(i)
            return i
    return -1


result = linear_search([1, 2, 3], 2)


#Сложность даного алгоритма будет равна = O(n) где n = x входящее число в массив. В данном случае цикл сработает один раз поэтому n = 1. А значит O(1).
