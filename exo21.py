def length(lst):
    return len(lst)

def mean(lst):
    return sum(lst) / len(lst) if lst else 0

def range_of_list(lst):
    return max(lst) - min(lst) if lst else 0


numbers = [1, 2, 3, 4, 5]
print("Length:", length(numbers))
print("Mean:", mean(numbers))
print("Range:", range_of_list(numbers))