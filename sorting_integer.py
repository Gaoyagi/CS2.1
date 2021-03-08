#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    largest = numbers[0]
    smallest = numbers[0]
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    #sort = []
    i = 0
    while smallest <= largest:
        if smallest in counts:
            for _ in range(counts[smallest]):
                # sort.append(smallest)
                numbers[i] = smallest
                i+=1
        smallest+=1
        
   
        

def insertion_sort(numbers):
    swapped = True
    while swapped:
        swapped =  False
        for x in range(1, len(numbers)):
            if numbers[x-1] > numbers[x]:
                temp = numbers[x-1]
                numbers[x-1] = numbers[x]
                numbers[x] = temp
                swapped = True

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    maximum = max(numbers, default=0) + 1
    buckets = [] 
    for _ in range(num_buckets):
        buckets.append([])

    for num in numbers:
        index = num * num_buckets // maximum
        buckets[index].append(num)

    index = 0
    for bucket in buckets:
        insertion_sort(bucket)
        for item in bucket:
            numbers[index] = item
            index += 1
    
   




temp = [2, 18, 17, 16, 20, 2]
#bucket_sort(temp)
counting_sort(temp)
print(temp)
