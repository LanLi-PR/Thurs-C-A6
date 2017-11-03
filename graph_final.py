import networkx as nx
"""
using networkx.DiGraph() class to create an attribute for class Navigation
and overload the method for this class (different parameters)
"""


class Navigation:
    def __init__(self):
        self.G = nx.DiGraph()

    def add_inter(self, intersection: list):
        """

        :param intersection: street intersection
        :return: 
        """
        self.G.add_node(intersection)

    def add_building(self, building, street,node_1,node_1_distance,node_1_direction,node_2,node_2_distance,node_2_direction):

        """
        Add the building to the map, and add the edge between the buildings and intersections automatically.
        :param building: Building Name of the building.
        :param street: Street name of the Street.
        :param node_1: One of the two intersections of the street.
        :param node_1_distance: The distance from building to node_1.
        :param node_1_direction: The drection from building to node_1
        :param node_2: The other intersection of the street.
        :param node_2_distance: The distance from building to node_2.
        :param node_2_direction: The drection from building to node_2
        """
        building_node = (building, street)
        from2ToExist = self.G.get_edge_data(node_1, node_2) != None
        to2FromExist = self.G.get_edge_data(node_2, node_1) != None
        """
        assigning to a reference in case of recursively calculate 
        make an edition here 
        """
        if from2ToExist:
            if to2FromExist:
                # from -> to | to -> from, two way "true"
                #  node1_->building->node2_ || node2_->building->node1_
                self.add_edge(building_node, node_1, node_1_distance, node_1_direction, True)
                self.add_edge(building_node, node_2, node_2_distance, node_2_direction, True)
            else:
                # from-> to, one way----node1_->building->node2_
                self.add_edge(node_1, building_node, node_2_distance, node_2_direction, False)
                self.add_edge(building_node, node_2, node_2_distance, node_2_direction, False)
        else:
            if to2FromExist:
                # to -> from,one way
                self.add_edge(building_node, node_1, node_1_distance, node_1_direction, False)
                self.add_edge(node_2, building_node, node_2_distance, node_2_direction, False)

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
        node=(from_,to)
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
                *reversed(node), weight=distance,orientation=oppose[orientation], edge_name=edge_name
            )

    def shorestPath(self,source,dest):
        """
        
        :param source: the input start map code
        :param dest: the input destination map code
        :return: the minimum path 
        """
        src = source
        dst = dest
        return nx.algorithms.shortest_paths.weighted.dijkstra_path(self.G,src,dst,weight='weight')


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
    school_map.add_edge(('E Daniel St', 'S 5th St'), ('E Daniel St', 'S 6th St'), 140, 'E', twoway=True)
    school_map.add_edge(('E Daniel St', 'S 6th St'), ('E Daniel St', 'S Wright St'), 130, 'E')
    school_map.add_edge(('E Daniel St', 'S 4th St'), ('E Chamlers St', 'S 4th St'), 130, 'S', twoway=True)
    school_map.add_edge(('E Daniel St', 'S 5th St'), ('E Chamlers St', 'S 5th St'), 130, 'S', twoway=True)
    school_map.add_edge(('E Daniel St', 'S 6th St'), ('E Chamlers St', 'S 6th St'), 130, 'S')
    school_map.add_edge(('E Daniel St', 'S Wright St'), ('E Chamlers St', 'S Wright St'), 130, 'S', twoway=True)
    school_map.add_edge(('E Chamlers St', 'S 4th St'), ('E Chamlers St', 'S 5th St'), 130, 'E', twoway=True)
    school_map.add_edge(('E Chamlers St', 'S 5th St'), ('E Chamlers St', 'S 6th St'), 140, 'E', twoway=True)
    school_map.add_edge(('E Chamlers St', 'S Wright St'), ('E Chamlers St', 'S 6th St'), 110, 'W')
    school_map.add_edge(('E Chamlers St', 'S 4th St'), ('E Armory St', 'S 4th St'), 160, 'S', twoway=True)
    school_map.add_edge(('E Chamlers St', 'S 5th St'), ('University of illinois Armory', 'S 5th St', 'E Armory St'), 160, 'S', twoway=True)
    school_map.add_edge(('E Chamlers St', 'S 6th St'), ('E Armory St', 'S 6th St'), 160, 'S')
    school_map.add_edge(('E Armory St', 'S Wright St'), ('E Chamlers St', 'S Wright St'), 160, 'N')

    school_map.add_edge(('E Armory St', 'S 4th St'), ('University of illinois Armory', 'S 5th St', 'E Armory St'), 130, 'E', twoway=True)
    school_map.add_edge(('University of illinois Armory', 'S 5th St', 'E Armory St'), ('E Armory St', 'S 6th St'), 140, 'E', twoway=True)
    school_map.add_edge(('E Armory St', 'S 6th St'), ('E Armory St', 'S Wright St'), 130, 'E')

    school_map.add_edge(('E Armory St', 'S 4th St'), ('E Gregory Dr', 'S 4th St'), 140, 'S', twoway=True)
    school_map.add_edge(('E Armory St', 'S 6th St'), ('E Gregory Dr', 'S 6th St'), 140, 'S', twoway=True)

    school_map.add_edge(('E Gregory Dr', 'S 4th St'), ('E Gregory Dr', 'S 6th St'), 270, 'E', twoway=True)

    school_map.add_edge(('E Gregory Dr', 'S 4th St'), ('E Peabody Dr', 'S 4th St'), 300, 'S', twoway=True)
    school_map.add_edge(('E Gregory Dr', 'S 6th St'), ('E Peabody Dr', 'S 6th St'), 300, 'S', twoway=True)
    school_map.add_edge(('E Peabody Dr', 'S 4th St'), ('E Peabody Dr', 'S 6th St'), 270, 'E', twoway=True)

    school_map.add_edge(('W Gregory Dr', 'S 6th St'), ('W Gregory Dr', 'S Goodwin Ave'), 560, 'E', twoway=True)

    school_map.add_edge(('South Goodwin Ave', 'S Goodwin Ave'), ('W Nevada St', 'S Goodwin Ave'), 200, 'N', twoway=True)
    school_map.add_edge(('W Nevada St', 'S Lincoln Ave'), ('W Pennsylvania Ave', 'S Lincoln Ave'), 600, 'S', twoway=True)
    school_map.add_edge(('W Pennsylvania Ave', 'S Lincoln Ave'), ('W Pennsylvania Ave', 'S Dorner Dr'), 220, 'W', twoway=True)
    school_map.add_edge(('W Pennsylvania Ave', 'S Dorner Dr'), ('W Peabody Dr', 'S Dorner Dr'), 100, 'N', twoway=True)
    school_map.add_edge(('W Peabody Dr', 'S Dorner Dr'), ('Allen Hall and Unit One', 'S Dorner Dr', 'South Goodwin Ave'), 300,
               'N', twoway=True)
    school_map.add_edge(('Allen Hall and Unit One', 'S Dorner Dr', 'South Goodwin Ave'), ('South Goodwin Ave', 'S Goodwin Ave'),
               170, 'W', twoway=True)

    school_map.add_edge(('W Peabody Dr', 'S Dorner Dr'), ('W Peabody Dr', 'S Goodwin Ave'), 230, 'W', twoway=True)
    school_map.add_edge(('W Peabody Dr', 'S Goodwin Ave'), ('Funk Agricultural Constitute/Funk ACES', 'S Goodwin Ave'), 100, 'N', twoway=True)

    ##building:
    school_map.add_building('School of Information Sciences', 'E Daniel St', ('E Daniel St', 'S 5th St'), 30, 'W',
                   ('E Daniel St', 'S 6th St'), 110, 'E')
    school_map.add_building('English Building', 'S Wright St', ('E Daniel St', 'S Wright St'), 30, 'N',
                   ('E Chalmers St', 'S Wright St'), 100, 'S')
    school_map.add_building('Lincoln Hall', 'S Wright St', ('E Chalmers St', 'S Wright St'), 30, 'N',
                   ('E Armory Ave', 'S Wright St'), 130, 'S')
    school_map.add_building('UI Ice Arena', 'E Armory Ave', ('E Armory Ave', 'S 4th St'), 65, 'W', ('E Armory Ave', 'S 5th St'),
                   65, 'E')
    school_map.add_building('Carl R. Woese Institute for Genomic Biology', 'S 6th St', ('E Chalmers St', 'S 6th St'), 90, 'N',
                   ('E Armory Ave', 'S 6th St'), 70, 'S')
    school_map.add_building('School of Art+Design', 'E Peabody Dr', ('E Peabody Dr', 'S 4th St'), 130, 'W',
                   ('E Peabody Dr', 'S 6th St'), 140, 'E')
    school_map.add_building('Undergraduate Library', 'W Gregory Dr', ('W Gregory Dr', 'S 6th St'), 280, 'W',
                   ('South Goodwin Ave', 'S Goodwin Ave'), 280, 'E')
    school_map.add_building('University of illinois Eschool_maptension/Mumford Hall', 'W Gregory Dr', ('W Gregory Dr', 'S 6th St'), 330,
                   'W', ('South Goodwin Ave', 'S Goodwin Ave'), 230, 'E')
    school_map.add_building('Carl R. Woese Institute for Genomic Biology', 'W Gregory Dr', ('W Gregory Dr', 'S 6th St'), 460,
                   'W', ('South Goodwin Ave', 'S Goodwin Ave'), 100, 'E')
    school_map.add_building('Freer Hall', 'W Gregory Dr', ('South Goodwin Ave', 'S Goodwin Ave'), 140, 'W',
                   ('South Goodwin Ave', 'S Dorner Dr'), 30, 'E')
    school_map.add_building('Mckinley Health Center', 'S Lincoln Ave', ('W Nevada St', 'S Lincoln Ave'), 400, 'N',
                   ('W Pennsylvania Ave', 'S Lincoln Ave'), 200, 'S')
    school_map.add_building('Foreign Language Building', 'W Mattews Ave', ('W Nevada St', 'W Mattews Ave'), 40, 'S',
                   ('W Oregon St', 'W Mattews Ave'), 70, 'N')
    school_map.add_building('Davenport Hall', 'W Mattews Ave', ('W Oregon St', 'W Mattews Ave'), 25, 'S',
                   ('W Illinois St', 'W Mattews Ave'), 205, 'N')
    school_map.add_building('School of Social Work', 'W Nevada St', ('W Nevada St', 'S Gregory St'), 40, 'W',
                   ('W Nevada St', 'S Lincoln Ave'), 160, 'E')
    school_map.add_building('Spurlock Museum', 'S Gregory St', ('W Oregon St', 'S Gregory St'), 68, 'S',
                   ('W Illinois St', 'S Gregory St'), 162, 'N')
    school_map.add_building('Institute of Government and public Affairs', 'W Nevada St', ('W Nevada St', 'S Gregory St'), 25,
                   'W', ('W Nevada St', 'S Lincoln Ave'), 175, 'E')
    school_map.add_building('Dance Studio', 'W Nevada St', ('W Nevada St', 'S Gregory St'), 70, 'W',
                   ('W Nevada St', 'S Lincoln Ave'), 130, 'E')
    school_map.add_building('Huff Hall', 'E Gregory Dr', ('E Gregory Dr', 'S 4th St'), 20, 'W', ('E Gregory Dr', 'S 6th St'),
                   250, 'E')

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

    school_map.add_edge(('W Nevada St', 'S Lincoln Ave'), ('W Oregon St', 'S Lincoln Ave'), 110, 'N')
    school_map.add_edge(('W Oregon St', 'S Lincoln Ave'), ('W Illinois St', 'S Lincoln Ave'), 230, 'N')

    # add_building(self,building: str,street,node_1,node_1_distance,node_1_direction,node_2,node_2_direction,node_2_distance):


    # 'E Daniel St'
    # 'S 4th St'
    # 'S 5th St'
    # 'S 6th St'
    # 'S Wright St'
    # 'E Chamler St'
    # 'E Armory St'
    # 'E Gregory'

    # def add_building(self, building: str, street, node_1, node_1_distance, node_1_direction, node_2, node_2_distance,node_2_direction):
    school_map.add_building('School of Information Sciences', 'E Daniel St', ('E Daniel St', 'S 5th St'), 30, 'W',
                   ('E Daniel St', 'S 6th St'), 110, 'E')
    print(school_map.G['E Daniel St', 'S 5th St']['School of Information Sciences', 'E Daniel St'])
    print(school_map.G['School of Information Sciences', 'E Daniel St']['E Daniel St', 'S 5th St'])
    print(school_map.G['School of Information Sciences', 'E Daniel St']['E Daniel St', 'S 6th St'])
    print(school_map.G['E Daniel St', 'S 6th St']['School of Information Sciences', 'E Daniel St'])

    print(list(school_map.G.nodes()))
    print(list(school_map.G.edges()))

    school_map.shorestPath()

if __name__=='__main__':
    main()