# Cycle Graph Example

class CycleGraph:

    def __init__(self, V):
        self.V = V
        self.adjacency_matrix = [[] for i in range(V)]

    def add_edge(self, orgin, destiny):
        self.adjacency_matrix[orgin].append(destiny)

    def dfs(self, v):
        stack = []
        stackRecord = [False for i in range(self.V)]
        visited = [False for i in range(self.V)]

        while True:
            find_neighbor = False

            if not visited[v]:
                stack.append(v)
                visited[v] = stackRecord[v] = True

            for adj in self.adjacency_matrix[v]:

                # The neighbor is on stackRecord, then exists an cycle
                if stackRecord[adj]:
                    return True
                # Not in the stackRecord and not in visited, you found it
                elif not visited[adj]:
                    find_neighbor = True
                    break

            if not find_neighbor:
                # get out of stack
                stackRecord[stack[-1]] = False
                # remove the stack last element
                stack.pop()
                if len(stack) == 0:
                    break
                v = stack[-1]
            else:
                v = adj

        return False

    def have_cycle(self):
        for i in range(self.V):
            if self.dfs(i):
                return True

        return False


# Cycle Graph example
cg = CycleGraph(3)
cg.add_edge(0, 1)
cg.add_edge(1, 2)
cg.add_edge(2, 0)

print(cg.have_cycle())

# Cycle Graph example
cg = CycleGraph(3)
cg.add_edge(0, 1)
cg.add_edge(1, 2)
cg.add_edge(2, 1)

print(cg.have_cycle())

# Not Cycle Graph example
cg = CycleGraph(4)
cg.add_edge(0, 1)
cg.add_edge(1, 2)
cg.add_edge(2, 3)

print(cg.have_cycle())
