from collections import deque

def smooth(inlist, h):

    """ 
    
    This function performs a basic smoothing

    of inlist and returns the result (outlist).

    Both lists have the same length, N. Each

    item in inlist is assumed to have type

    'float', and 'h' is assumed to be a

    non-negative integer. For each i, outlist[i]

    will be the average of inlist[k] over all k

    that satisfy i-h <= k <= i+h and

    0 <= k <= N-1. 
    
    author: Rida Lefdali
    email: rida_lefdali@outlook.com
    
    """

    N = len(inlist)
    
    outlist = []
    
    if h >= N:
        
        avg = sum(inlist)/N
        return N*[avg]
    
    # we take the first h element in the inlist
    sub_list = inlist[:h+1]
    
    # we use double ended queue as it has operations with complexity O(1)
    dequeue = deque(sub_list)
    
    n_dequeue = len(dequeue) # number of element in the dequeue 
    
    avg = sum(dequeue)/n_dequeue # compute the first element of outlist
    
    outlist.append(avg) # add the first element to outlist

    # for loop to compute the all other elements of outlist
    for i in range(1,N):
        
        n_dequeue = len(dequeue)
        
        l = 0
        
        if i + h < N: 
            
            elt = inlist[i+h]
            dequeue.append(elt)

            if len(dequeue) > 2*h+1:
                l = dequeue.popleft()
            
            avg = (n_dequeue*avg + elt - l)/len(dequeue)
            
            outlist.append(avg)
        
        else:
            
            if i-h > 0:
                l = dequeue.popleft()
            
            avg = (n_dequeue*avg - l)/len(dequeue)
            
            outlist.append(avg)
        
  
    return outlist