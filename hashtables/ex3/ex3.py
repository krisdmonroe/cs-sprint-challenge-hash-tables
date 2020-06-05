def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    # first idea
    # for loop somehow
    print(arrays)
    for i in arrays:
        
        
    return cache


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
