import networkx as nx

class Navigation:
    def __init__(self):
        self.G = nx.DiGraph()

    def add_inter(self, intersection: list):
        """

        :param intersection: street intersection
        :return: 
        """
        self.G.add_node(intersection)

    def add_building(self, building: str, street, from_, from_distance, from_direction, to, to_direction, to_distance):
        # two way
        building_node = (building, street)
        from2ToExist = self.G.get_edge_data(from_, to) != None
        to2FromExist = self.G.get_edge_data(to, from_) != None
        if from2ToExist:
            if to2FromExist:
                # from -> to | to -> from
                self.add_edge(building_node, from_, from_distance, from_direction, True)
                self.add_edge(building_node, to, to_distance, to_direction, True)
            else:
                # from-> to
                self.add_edge(from_, building_node, from_distance, to_direction, False)
                self.add_edge(building_node, to, to_distance, to_direction, False)
        else:
            if to2FromExist:
                # to -> from
                self.add_edge(building_node, from_, from_distance, from_direction, False)
                self.add_edge(to, building_node, to_distance, from_direction, False)
                # single way

    def add_edge(self, from_, to, distance, orientation='S', twoway=False):
        """
        make an edition here, the default twoway- should be set as false to kep this graph diagraph
        :type street_name: str
        :param from_: start node
        :param to: end node
        :param distance: the weight for every edge
        :param orientation: set the default one orientation
        :param twoway: default one-way
        :return: 
        """
        for i in from_:
            for j in to:
                if i == j:
                    edge_name = i

        self.G.add_edge(from_, to, weight=distance, orientation=orientation, edge_name=edge_name)
        """
        simplify the twoway parameter
        """
        if twoway:
            oppose = {
                'N': 'S',
                'S': 'N',
                'E': 'W',
                'W': 'E',
            }
            # Use different meta
            self.G.add_edge(
                *reversed(from_,to), weight=distance,orientation=oppose[orientation], edge_name=edge_name
            )

        # if twoway:
        #     if direction == 'S':
        #         direction = 'N'
        #     elif direction == 'N':
        #         direction = 'S'
        #     elif direction == 'E':
        #         direction = 'W'
        #     else:
        #         direction = 'E'
        #     self.G.add_edge(to, from_, weight=distance, direct=direction, street=street_name)

    def shorestPath(self,source,dest):
        src = source
        dst = dest
        return nx.algorithms.shortest_paths.weighted.dijkstra_path(G,src,dst,weight='weight')

def main():
    """
    constrct an instance
    :return: 
    """
    school_map = Navigation()

    # 'E Daniel St'
    # 'S 4th St'
    # 'S 5th St'
    # 'S 6th St'
    # 'S Wright St'
    # 'E Chamler St'
    # 'E Armory St'
    # 'E Gregory'
    school_map.add_edge(('E Daniel St', 'S 4th St'), ('E Daniel St', 'S 5th St'), 130, 'E', twoway=True)
    school_map.add_edge(('E Daniel St', 'S 5th St'), ('E Daniel St', 'S 6th St'), 140, 'E')
    school_map.add_edge(('E Daniel St', 'S 6th St'), ('E Daniel St', 'S Wright St'), 130, 'E', False)
    school_map.add_edge(('E Daniel St', 'S 4th St'), ('E Chamlers St', 'S 4th St'), 130, 'S')
    school_map.add_edge(('E Daniel St', 'S 5th St'), ('E Chamlers St', 'S 5th St'), 130, 'S')
    school_map.add_edge(('E Daniel St', 'S 6th St'), ('E Chamlers St', 'S 6th St'), 130, 'S', False)
    school_map.add_edge(('E Daniel St', 'S Wright St'), ('E Chamlers St', 'S Wright St'), 130, 'S')
    school_map.add_edge(('E Chamlers St', 'S 4th St'), ('E Chamlers St', 'S 5th St'), 130, 'E')
    school_map.add_edge(('E Chamlers St', 'S 5th St'), ('E Chamlers St', 'S 6th St'), 140, 'E')
    school_map.add_edge(('E Chamlers St', 'S Wright St'), ('E Chamlers St', 'S 6th St'), 110, 'W', False)
    school_map.add_edge(('E Chamlers St', 'S 4th St'), ('E Armory St', 'S 4th St'), 160, 'S')
    school_map.add_edge(('E Chamlers St', 'S 5th St'), ('E Armory St', 'S 5th St'), 160, 'S')
    school_map.add_edge(('E Chamlers St', 'S 6th St'), ('E Armory St', 'S 6th St'), 160, 'S', False)
    school_map.add_edge(('E Armory St', 'S Wright St'), ('E Chamlers St', 'S Wright St'), 160, 'N', False)

    school_map.add_edge(('E Armory St', 'S 4th St'), ('E Armory St', 'S 5th St'), 130, 'E')
    school_map.add_edge(('E Armory St', 'S 5th St'), ('E Armory St', 'S 6th St'), 140, 'E')
    school_map.add_edge(('E Armory St', 'S 6th St'), ('E Armory St', 'S Wright St'), 130, 'E', False)

    school_map.add_edge(('E Armory St', 'S 4th St'), ('E Gregory Dr', 'S 4th St'), 140, 'S')
    school_map.add_edge(('E Armory St', 'S 6th St'), ('E Gregory Dr', 'S 6th St'), 140, 'S')

    school_map.add_edge(('E Gregory Dr', 'S 4th St'), ('E Gregory Dr', 'S 6th St'), 270, 'E')

    school_map.add_edge(('W Nevada St', 'W Mattews Ave'), ('W Nevada St', 'S Goodwin Ave'), 140, 'E')
    school_map.add_edge(('W Nevada St', 'S Goodwin Ave'), ('W Nevada St', 'S Gregory St'), 200, 'E')
    school_map.add_edge(('W Nevada St', 'S Gregory St'), ('W Nevada St', 'S Lincoln Ave'), 200, 'E')

    school_map.add_edge(('W Oregon St', 'S Goodwin Ave'), ('W Oregon St', 'W Mattews Ave'), 140, 'W')
    school_map.add_edge(('W Oregon St', 'S Goodwin Ave'), ('W Oregon St', 'S Gregory St'), 200, 'E')
    school_map.add_edge(('W Oregon St', 'S Gregory St'), ('W Oregon St', 'S Lincoln Ave'), 200, 'E')

    school_map.add_edge(('W Illinois St', 'W Mattews Ave'), ('W Illinois St', 'S Goodwin Ave'), 140, 'E')
    school_map.add_edge(('W Illinois St', 'S Goodwin Ave'), ('W Illinois St', 'S Gregory St'), 200, 'E')
    school_map.add_edge(('W Illinois St', 'S Gregory St'), ('W Illinois St', 'S Lincoln Ave'), 200, 'E')

    school_map.add_edge(('W Nevada St', 'W Mattews Ave'), ('W Oregon St', 'W Mattews Ave'), 110, 'S')
    school_map.add_edge(('W Oregon St', 'W Mattews Ave'), ('W Illinois St', 'W Mattews Ave'), 230, 'S')

    school_map.add_edge(('W Oregon St', 'S Goodwin Ave'), ('W Nevada St', 'S Goodwin Ave'), 110, 'N')
    school_map.add_edge(('W Illinois St', 'S Goodwin Ave'), ('W Oregon St', 'S Goodwin Ave'), 230, 'N')

    school_map.add_edge(('W Nevada St', 'S Gregory St'), ('W Oregon St', 'S Gregory St'), 110, 'N')
    school_map.add_edge(('W Oregon St', 'S Gregory St'), ('W Illinois St', 'S Gregory St'), 230, 'N')

    school_map.add_edge((('W Nevada St', 'S Lincoln Ave'), ('W Oregon St', 'S Lincoln Ave'), 110, 'N'))
    school_map.add_edge((('W Oregon St', 'S Lincoln Ave'), ('W Illinois St', 'S Lincoln Ave'), 230, 'N'))

    # add_building(self,building: str,street,from_,from_distance,from_direction,to,to_direction,to_distance):
    school_map.add_building('Foreign Language Building', 'W Mattews Ave', ('W Nevada St', 'W Mattews Ave'), 40, 'S',
                   ('W Oregon St', 'W Mattews Ave'), 70, 'N')
    school_map.add_building('Davenport Hall', 'W Mattews Ave', ('W Oregon St', 'W Mattews Ave'), 25, 'S',
                   ('W Illinois St', 'W Mattews Ave'), 205, 'N')
    school_map.add_building('School of Social Work', 'W Nevada St', ('W Nevada St', 'S Gregory St'), 40, 'W',
                   ('W Nevada St', 'S Lincoln Ave'), 160, 'E')
    school_map.add_building('Spurlock Museum', 'S Gregory St', ('W Oregon St', 'W Mattews Ave'), 68, 'S',
                   ('W Illinois St', 'W Mattews Ave', 162, 'N'))
    school_map.add_building('School of Social Work', 'W Nevada St', ('W Nevada St', 'S Gregory St'), 25, 'W',
                   ('W Nevada St', 'S Lincoln Ave'), 175, 'E')
    school_map.add_building('School of Social Work', 'W Nevada St', ('W Nevada St', 'S Gregory St'), 70, 'W',
                   ('W Nevada St', 'S Lincoln Ave'), 130, 'E')

    print(list(school_map.G.nodes()))
    print(list(school_map.G.edges()))
    school_map.shorestPath()
