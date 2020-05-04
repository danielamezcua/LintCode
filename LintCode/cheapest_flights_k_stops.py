from collections import deque,defaultdict
class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice(self, n, flights, src, dst, K):
        q = deque()
        flights_graph = defaultdict(lambda: defaultdict(int))
        cheapest = -1

        if src == dst:
            return 0


        for flight in flights:
            flights_graph[flight[0]][flight[1]] = flight[2]
        

        visited = set()
        visited.add(src)
        first = (src, visited, K,0)
        q.append(first)

        while q:
            element = q.popleft()
            source = element[0]
            vis = element[1]
            stops_left = element[2]
            price_so_far = element[3]
            vis.add(source)

            #check if we have arrived to the destination
            if source == dst:
                if cheapest == -1 or price_so_far < cheapest:
                    cheapest = price_so_far
            #check if we can continue to add stops and if it makes senes to keep adding stops in this route
            elif stops_left >= 0 and (cheapest == -1 or price_so_far < cheapest):
                #get next stops from this source and add them to the queue
                stops = flights_graph[source]
                for stop in stops.keys():
                    if stop not in vis:
                        q.append((stop, vis.copy(), stops_left-1, price_so_far+ stops[stop]))

        return cheapest 