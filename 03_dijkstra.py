# Dijkstra Algorithm - Shortest Path
# Only to Positive
from collections import defaultdict
import heapq

# min Heap


class MinHeap:

    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def get_length(self):
        return len(self._queue)

# graph


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertexes = {}

    def addEdge(self, src, dest, cost):
        self.graph[src].append((dest, cost))
        self.vertexes[src] = src
        self.vertexes[dest] = dest

    def dijkstra(self, src, dest):

        # get the number of vertexes
        number_vertexes = len(self.vertexes)

        # estimate the lower cost
        p = [None for i in range(number_vertexes)]

        # the source is 0
        p[src] = 0

        # building the min heap (priority queue)
        min_heap = MinHeap()

        # insert the source in min heap
        min_heap.insert(src, 0)

        # while the heap lenght is upper than 0
        while min_heap.get_length() > 0:

            # remove of min heap
            u = min_heap.remove()

            # running the edge of "u"
            for edge in self.graph[u]:

                # get the edge and cost
                v, cost = edge

                # relaxation condition
                if p[v] is None or p[v] > p[u] + cost:

                    # update the cost estimative
                    p[v] = p[u] + cost

                    # insert on min heap
                    min_heap.insert(v, p[v])

        # return the lower path cost
        return p[dest]

g = Graph()

g.addEdge(0, 1, 1)
g.addEdge(0, 3, 3)
g.addEdge(0, 4, 10)
g.addEdge(1, 2, 5)
g.addEdge(2, 4, 1)
g.addEdge(3, 2, 2)
g.addEdge(3, 4, 6)

print(g.dijkstra(0, 4))
