"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
          # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  # TODO
        else:
            raise IndexError('That vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[starting_vertex]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting vertex id 
        q = Queue()
        q.enqueue(starting_vertex)
        # create an empty Set to store visitied vertices
        visitied = set()
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first vertex 
            v = q.dequeue()
            # if that vertex has not been visited
            if v not in visitied:
                # mark it as visited
                print(v)
                visitied.add(v)
                # add all of it's neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
         # create an empty stack and push the starting vertex id 
        s = Stack()
        s.push(starting_vertex)
        # create an empty Set to store visitied vertices
        visitied = set()
        # while the stack is not empty...
        while s.size() > 0:
            # pop the first vertex 
            v = s.pop()
            # if that vertex has not been visited
            if v not in visitied:
                # mark it as visited
                print(v)
                visitied.add(v)
                # add all of it's neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print('dft_recursive',starting_vertex)

        for item in self.vertices[starting_vertex]:
            if item not in visited:
                self.dft_recursive(item,visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
        # Create an empty queue and enqueue a path to the starting vertex id
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a set to store visitied vertices
        visited = set()
        # while the queue is not empty:
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # grab the last vertex from the path
            v = path[-1]
            # if that vertex has not been visited:
            if v not in visited:
                # check if it's the target:
                if v == destination_vertex:
                    # if so return path
                    return path
                # mark it as visited
                visited.add(v)
                # then add a path to it's neighbors to check the back of the queue
                for item in self.vertices[v]:
                    # copy the path 
                    copied_path = list(path)
                    # append the neighbor to the back
                    copied_path.append(item)
                    # enqueue the copied path 
                    q.enqueue(copied_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push a path to the starting vertex id
        s = Stack()
        s.push([starting_vertex])
        # Create a set to store visitied vertices
        visited = set()
        # while the queue is not empty:
        while s.size() > 0:
            # pop the first path
            path = s.pop()
            # grab the last vertex from the path
            v = path[-1]
            # if that vertex has not been visited:
            if v not in visited:
                # check if it's the target:
                if v == destination_vertex:
                    # if so return path
                    return path
                # mark it as visited
                visited.add(v)
                # then add a path to it's neighbors to check the back of the queue
                for item in self.vertices[v]:
                    # copy the path 
                    copied_path = list(path)
                    # append the neighbor to the back
                    copied_path.append(item)
                    # push the copied path 
                    s.push(copied_path)

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
