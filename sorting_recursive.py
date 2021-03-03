#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    sorted = []
    x = 0
    y = 0
    while x < len(items1) or y < len(items2):

        #items are both in bounds
        if x < len(items1) and y < len(items2):
            if items1[x] < items2[y]:
                sorted.append(items1[x])
                x += 1
            else:
                sorted.append(items2[y])
                y += 1
        else:
            #i is only one with elements remaining
            if x < len(items1):
                sorted.extend(items1[x:])
            #j is ony one with elements remaining
            else:
                sorted.extend(items2[y:])

            break

    return sorted

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    mid = len(items) // 2

    #base case
    if len(items) > 1:

        #divide lists
        items1 = items[:mid]
        items2 = items[mid:]

        #recursivley call merge sort
        merge_sort(items1)
        merge_sort(items2)

        #merge lists back together
        items[:] = merge(items1, items2)
    



def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # # TODO: Move pivot item into final position [p] and return index p
    pivot = low
    left = low+1
    right = high
    while left<=right:
        while left<=right and items[left] <= items[pivot]: 
            left+=1
        while left<=right and items[right] >= items[pivot]:
            right-=1
        if left<=right:
            temp = items[left]
            items[left] = items[right]
            items[right] = temp

    temp = items[pivot]
    items[pivot] = items[right]
    items[right] = temp
    return right

    



def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

    #check for default values
    if low == None and high == None:
        low = 0
        high = len(items) - 1

    #Base case, current list size is too small
    if low < high:
        pivot = partition(items, low, high)     #partition list
        quick_sort(items, low, pivot-1)           #sort left sublist
        quick_sort(items, pivot+1, high)        #sort right sublist  

         
    
    