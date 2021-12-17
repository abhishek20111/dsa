class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end) # it have to add new elments
            else:
                self.graph_dict[start] = [end] # if tere is none in that work of dictionary then add the value you are checking
        print("Graph dict",self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shorttest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shorttest_path is None or len(sp) < len(shorttest_path):
                        shorttest_path = sp

        return shorttest_path



if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_path = Graph(routes)

    start = "Mumbai"
    end = "Toronto"

    print(f"shortest path between {start} and {end}:",route_path.get_shortest_path(start, end))
    print(f"All paths between: {start} and {end}: ", route_path.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_path.get_shortest_path(start, end))

    start = "Dubai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ", route_path.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_path.get_shortest_path(start, end))

    # d = {
    #     "Mumbai":["Paris","Dubai"],
    #     "Paris":["Dubai","New York"]
    # }
    # routes = [
    #     ("Mumbai", "Paris"),
    #     ("Mumbai", "Dubai"),
    #     ("Paris", "Dubai"),
    #     ("Paris", "New York"),
    #     ("Dubai", "New York"),
    #     ("New York", "Toronto"),
    # ]
