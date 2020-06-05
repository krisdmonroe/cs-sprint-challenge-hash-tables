# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    # for f in files:
    #     # print(f)
    #     if f in cache:
    #         cache[f] += 1
    #     else:
    #         cache[f] = 1
    #     for i in queries:
    #         print(i)
    #         if i in cache:
    #             result.append(i)
    # return result
    files[files.find('/'):]
    print(files)
        # for q in queries:
        #     print(q)

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
