#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for x in range(len(items)):
        if x < len(items)-1:
            if items[x+1] < items[x]:
                return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    for x in range(len(items)-1):
        if items[x]>items[x+1]:
            temp = items[x]
            items[x] = items[x+1]
            items[x+1] = temp



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    for x in range(len(items)):
        smallest_index = x
        if x!=len(items)-1:
            for y in range(x+1, len(items)):
                if items[y] < items[smallest_index]:
                    smallest_index = y
            temp = items[x]
            items[x] = items[smallest_index]
            items[smallest_index] = temp

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for x in range(1, len(items)):
        swap = items[x]
        y = x-1
        while items[y] > swap and y>=0:
            items[y+1] = items[y]
            y-=1
        items[y+1] = swap            


# 3, 5, 2