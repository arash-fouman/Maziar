import math
a = [10, 5, 6, 2, 1, 9, 7, 8, 4]

a = [1 , 2, 4, 5, 6, 7, 8, 9, 10]

def binary_search(a, x, begin, end):
    
    n = math.floor((end - begin)/2)
    
    if (begin == end):
        if( a[begin] == x):
            return begin
        else:
            return -1                           # if the element was not found in the array

                
    if( begin - end )%2:                        #check if the array length is even
        
        if ( a[n] >= x ):
            return binary_search (a , x, begin, begin+n)
        else:
            return binary_search (a , x,  begin+n+1 , end)

    else:
        if( a[n] == x):                     #check the middle element
            return n

        elif ( a[n] > x ):
            return binary_search (a , x, begin, begin+n)
        else:
            return binary_search (a , x,  begin+n+1 , end)


i = binary_search(a, 4, 0, len(a)-1)

print(i)
