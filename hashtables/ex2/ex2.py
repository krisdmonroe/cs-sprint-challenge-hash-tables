#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    route = []
    # Your code here
    for i in tickets:
        cache[i.source] = i.destination
        # print(cache[i.source])
        # if cache[i.source] == 'NONE':
        #     current = cache[i.source]
        #     route.append(cache[i.source])
        #     print(i.destination)
        #     if i.destination == 'NONE':
        #         return
    # get a starting ticket
    # find the value for the initial value NONE which would be lax
    route.append(cache["NONE"])
    # print(cache["NONE"])
    # then continue through the list
    # this will set cur to lax
    cur = cache["NONE"]
    # print(cur)
    # will stop when it finds the end
    while cur != "NONE":
        # we initiat with none but we get lax
        # so we then will get SFO if we pass in lax
        # that will continue untill we have nothing left
        # cur = LAX
        route.append(cache[cur])
        # will set cur to next item
        # cur = cache["LAX"]
        cur = cache[cur]
        # this will not be SFO
        # which will be pass back in route.append(cache["SFO"])
        # print(cur)
    return route

if __name__ == "__main__":
    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")
    tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

    print(reconstruct_trip(tickets, 10))
