


lists = [[1, 4, 10, 15, 30, 70, 90, 120, 150, 330, 500] , [1, 3, 4], [2, 6], [2, 5, 8], [-17, 10, 12]]

def merge(lists):

    n = len(lists)

    if( n == 1 ):
        return lists[0]
    
    #creates a binary tree as in merge sort
    left = merge(lists[:int(n/2)])
    right= merge(lists[int(n/2):])

    l_index = 0   #keeps track of the last index inserted into the final list
    r_index = 0   #keeps track of the last index inserted into the final list
    res = []

    while (l_index < len(left) and r_index < len(right)): #checks to not go out of bound
        
        if(left[l_index] < right[r_index]):
            res.append(left[l_index])
            l_index += 1
        else:
            res.append(right[r_index])
            r_index += 1

    
    if (l_index < len(left)):        #inserts the residual elements of the list to the final list
        res.extend(left[l_index:])

    if(r_index < len(right)):       #inserts the residual elements of the list to the final list
        res.extend(right[r_index:])

    return res

print(merge(lists))
