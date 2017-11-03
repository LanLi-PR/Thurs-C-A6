

class Node(object):
    """
    **meta is for dictionary for every node
    name is key(dict)
    """
    def __init__(self, name, **meta):
        self._name = name
        self.meta = meta

        self.edges = {}
        self._hash = hash(name)

    @property
    def name(self):
        return self._name

    # def add_edge(self, edge: Edge):
    #     """
    #     inherit the Edge
    #     :param edge:
    #     :return:
    #     """
    #     self.edges[edge.to] = edge

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

    def __hash__(self):
        return self._hash


class Edge(object):
    def __init__(self, from_, to, **meta):
        self._from = from_
        self._to = to
        self.meta = meta

        self._hash = hash((self._from, self._to))

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
               and self.from_ == other.from_ \
               and self.to == other.to

    def __hash__(self):
        return self._hash


class Graph:
    def __init__(self, node_cls=Node, edge_cls=Edge):
        self._nodes = {}
        """
        inherit class Node and Edge
        """
        assert issubclass(node_cls, Node)
        assert issubclass(edge_cls, Edge)
        self._node_cls = node_cls
        self._edge_cls = edge_cls

    def node(self, name, **meta):
        """Create node if not exist, update node meta and get node."""
        if name not in self._nodes:
            self._nodes[name] = self._node_cls(name=name, **meta)
        else:
            self._nodes[name].meta.update(**meta)
        return self._nodes[name]

    def edge(self, from_: Node, to: Node, **meta):
        """Create edge if not exist, update edge meta and get edge."""
        assert from_ in self._nodes.values()
        assert to in self._nodes.values()
        if to not in from_.edges:
            from_.edges[to] = self._edge_cls(from_, to, **meta)
        else:
            from_.edges[to].meta.update(**meta)
        return from_.edges[to]

    def edge_n(self, from_name, to_name, **meta):
        """Create edge if not exist, update edge meta and get edge by name."""
        from_ = self.node(from_name)
        to = self.node(to_name)
        return self.edge(from_, to, **meta)

    def edges(self, *nodes, is_bidirectional=False, **meta):
        """Create edges if not exist, update edge metas and get edges."""
        result = []
        for i in range(len(nodes) - 1):
            from_ = nodes[i]
            to = nodes[i + 1]
            result.append(self.edge(from_, to, **meta))
            if is_bidirectional:
                result.append(self.edge(to, from_, **meta))
        return result

    def edges_n(self, *node_names, is_bidirectional=False, **meta):
        """Create edges if not exist, update edge metas and get edges by name.
        """
        nodes = [self.node(node_name) for node_name in node_names]
        return self.edges(*nodes, is_bidirectional, **meta)