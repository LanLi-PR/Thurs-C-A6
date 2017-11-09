"""
a python class

"""


class Edge(object):
    edges = []

    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to

    def add_edge(self,from_,to,bidirectional=True):
        edge=Edge(from_,to)


        pass



class Nodes(object):
    """
    class for the nodes in the graph
    """
    def __init__(self,nodes=[]):
        self.nodes=nodes

    def add_node(self, node):
        nodes = []
        nodes.append(node)


class Graph(Edge,Nodes):
    """
    construct the shortest-path
    
    """
    pass
