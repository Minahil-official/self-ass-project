def remove_element(lst):
    min_len = 3
    while len(lst) >= min_len:
        last_ele = lst.pop()
        print(last_ele)
    
remove_element([1,2,3,4,5,6,7])
