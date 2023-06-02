def solve(arr): 
    while True:
        for k, v in enumerate(arr):
            while k != len(arr) -1 :
                k += 1
                if v == arr[k]:
                    arr.remove(v)
                else:
                    continue
        break
    return arr
    
    





print(solve([1,1,2,2,3,4,5,5,4,6]))
