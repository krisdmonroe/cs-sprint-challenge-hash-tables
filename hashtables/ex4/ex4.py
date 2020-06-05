import time
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    key = []
    # for i in a:
    #     if i >= 0:
    #         if i in cache:
    #             cache[i] += 1
    #         else:
    #             cache[i] = 1   
    #         # print(i)
    #     elif i < 0:    
    #         negative = abs(i)
    #         if negative in cache:  
    #             # print(cache)
    #             # print('this is neg', negative)
    #             # print('this is neg', negative)
    #             key.append(negative)
    # for i in a:
    #     if i != 0:
    #         if i in cache:
    #             cache[i] += 1
    #         else:
    #             cache[i] = 1
    #             # print(key)
    #         if i < 0:
    #             # print(-i)
    #             if -i in cache:
    #                 key.append(-i)

    for i in a:
        if i != 0:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
                # reverse possitve to negative and negative to possitve
                reverse = -i
                # if the reverse is in the list
                if reverse in cache:
                    # if reverse is greater we know its positive
                    if reverse > i:
                        print(reverse, i)
                        key.append(reverse)
                    else:
                        # reverse is less then i we want to only return positive numbers
                        # append the positive number
                        # print(i, reverse)
                        key.append(i)
    return key
    # going to try to append negatives first------
    # cache = {}
    # key = []
    # for i in a:
    #     if i < 0:
    #         negative = abs(i)
    #         print(i)
    #         cache[negative] = 1
    #         print(cache)
    #     else:
    #         if i in cache:
    #             key.append(i)
    # return key

# if __name__ == "__main__":
    # print(has_negatives([-1,-2,1,2,3,4,-4]))
    # print(has_negatives([1,-1,2,3,-4,-3,4,-5,6,7]))
    # print(has_negatives([1,2,3])
    # 1,-1,2,3,-4,-3,4,-5,6,7 = cache
    # i is 1
    # the reverse is -1
    # cache is 1
    # is reverse which is -1 in cache no so continue
    # now cache has 1,-1
    # reverse of -1 is 1 
    # is 1 > -1 yes so append to list
    # list is now 1


