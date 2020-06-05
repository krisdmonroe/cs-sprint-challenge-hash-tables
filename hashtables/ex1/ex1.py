def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    # x = weights
    # for i in range(len(weights)):
    #     for ii in range(len(weights) -1):
    #         if (x[i] + x[ii+1]) == limit:
    #                 return (ii+1 , i)
    # (key,value)
    # (weights, index)
        # print(i)
    for i in range(len(weights)):
        # print(i, end = " ")
        # print(weights[i])
        # print(i)
        x = limit - weights[i]
        # x is limit minus weight now were looking for that value in the cache
        if x in cache:
            if cache[x] < i:
                return [i, cache[x]]
            else:    
                return [cache[x], i]
            # print(cache)
        # otherwise add it to the cache
        else:
            # weights[i] is value and i is index
            cache[weights[i]] = i
        
        # print(limit - weights[i]) 
    return None 

# if __name__ == "__main__":
#     weights_3 = [4, 6, 10, 15, 16]
#     print(get_indices_of_item_weights(weights_3, 5, 21))