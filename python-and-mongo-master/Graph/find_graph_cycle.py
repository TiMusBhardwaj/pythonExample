
#######       IGNORE             ##########
####NOT WORKING AS EXPECTED  #############

class Solution:

    def course_schedule(self, n, edges):


        # key vertex: value -> all connected vertices
        map_graph = {}

        for edge in edges:
            edge_0_connections = map_graph.get(edge[0])
            if edge_0_connections is None:
                edge_0_connections = [edge[1]]
            else:
                edge_0_connections.append(edge[1])
            map_graph[edge[0]] = edge_0_connections



            if len(map_graph ) > n:
                return False

        map_visited = {}
        #check for cycle
        arr = [next(iter(map_graph))]
        while len(arr) > 0:

            vertex = arr.pop(0)
            if not vertex:
                continue
            if map_visited.get(vertex) is not None and map_visited[vertex]:
                return False
            map_visited[vertex] = True
            arr = arr + [] if map_graph.get(vertex) is None else map_graph.get(vertex)
        return True




if __name__ == '__main__':
    print(Solution().course_schedule(4, [[1, 0], [1, 2], [3, 1], [2, 3]]))