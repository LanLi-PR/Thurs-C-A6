import csv

from graph import Graph


class SchoolMap(Graph):
    def add_street(
            self, *nodes,
            is_bidirectional=False, orientation='S', street_name='Street'
    ):
        orientation = orientation.upper()
        """
        update the edges().meta in Graph.edges()
        in map, we cannot just define bidirectional here; we need to update the parameter
        """
        self.edges(*nodes, orientation=orientation, street_name=street_name)
        if is_bidirectional:
            oppose = {
                'N': 'S',
                'S': 'N',
                'E': 'W',
                'W': 'E',
            }
            # Use different meta
            self.edges(
                *reversed(nodes), orientation=oppose[orientation], street_name=street_name
            )

    def add_street_n(
            self, *node_names,
            is_bidirectional=False, orientation='S', street_name='Street'
    ):
        nodes = [self.node(node_name) for node_name in node_names]
        self.add_street(*nodes, is_bidirectional, orientation, street_name)

    def dijkstra(self, *nodes, *edges, *distance, initial):
        """
        :param nodes: 
        :param edges: 
        :param distance: adjacent edges' distance
        :param initial: 
        :return: 
        """
        visited = {initial: 0}
        path = {}

        nodes = set(nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in edges[min_node]:
                try:
                    weight = current_weight + distance[(min_node, edge)]
                except:
                    continue
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node
        return visited, path


def read_data(path):
    """
    read the map data 
    :param path 
    :return: map data structure 

    """
    node_data = []
    with open(path) as f:
        # skip the headers
        reader=csv.DictReader(f,delimiter=',')
        for row in reader:
            node={
                'name': row['name'].strip(),
                'latitude':row['latitude'].strip(),
                'longitude':row['longitude'].strip()
                }
            node_data.append(node)
        print(node_data)
    f.close()
    return node_data


def main():
    nodes=read_data('map_tempo1.csv')
    school_map = SchoolMap()
    for node in nodes:
        school_map.node(**node)
    school_map.add_street_n(
        'a','b','c','d',
        is_bidirectional=True, orientation='E', street_name='E.Daniel'
    )
    school_map.add_street_n(
        'e','f','g',
        is_bidirectional=True, orientation='E', street_name='E.Chalmers'
    )
    school_map.add_street_n(
        'h','i','j',
        is_bidirectional=True, orientation='E', street_name='E.Armory'
    )
    # ...
    school_map.add_street_n(
        'a','e','h',
        is_bidirectional=True, orientation='S', street_name='4th'
    )
    school_map.add_street_n(
        'b','f','j',
        is_bidirectional=True, orientation='S', street_name='5th'
    )
    school_map.add_street_n(
        'd','g',
        is_bidirectional=True, orientation='S', street_name='6th'
    )
    while True:
        # get user input
        raw_input=input(from_,to).strip()
        from_ = school_map.node(raw_input[0])
        to = school_map.node(raw_input[1])
        # set the edge distance

        # path_edges = school_map.path(from_, to) # Do it yourself
        # output


if __name__ == '__main__':
    main()
