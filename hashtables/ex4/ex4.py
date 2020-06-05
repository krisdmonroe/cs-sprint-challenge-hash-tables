def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i in a:
        new = abs(i)
        if new not in cache:
            cache[new] = 1
        else:
            cache[new] += 1
            # print('this is cache', cache)
            # print('this is greater', cache)
        for key, value in cache.items():
            if value == 2:
                if key not in cache:
                    print('this is print', key)
                # print('this is print', key)

        # print('this is value', value)
        # else:
        #     new = abs(i)
        #     print(new)
    # print(a)
    return key


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
