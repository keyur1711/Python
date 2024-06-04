def arr(lst):
    if not lst: 
        return []
    else:
        return arr(lst[1:]) + [lst[0]]   

lst = [1, 2, 3, 4, 5]
arr = arr(lst)
print("Reversed", arr)
