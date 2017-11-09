import networkx as nx

class Navigation():

    def __init__(self):
        # Initiate an DiGraph.
        self.G = nx.DiGraph()


    def add_building(self,building: str,street,node_1,node_1_distance,node_1_direction,node_2,node_2_distance,node_2_direction):

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
        # Create node of building
        building_node = (building,street)
        # Whether direction of node_1 to node_2 is available.
        if self.G.get_edge_data(node_1,node_2)!= None:
            # Whether direction of node_2 to node_1 is available.
            if self.G.get_edge_data(node_2,node_1) != None:
                self.add_edge(building_node,node_1,node_1_distance,node_1_direction,twoway = True)
                self.add_edge(building_node,node_2,node_2_distance,node_2_direction,twoway = True)
            else:
                self.add_edge(node_1,building_node,node_1_distance,node_2_direction, False)
                self.add_edge(building_node,node_2,node_2_distance,node_2_direction, False)
        else:
            if self.G.get_edge_data(node_2,node_1) != None:
                self.add_edge(building_node,node_1,node_1_distance,node_1_direction, False)
                self.add_edge(node_2,building_node,node_2_distance,node_1_direction, False)



    def add_edge(self,node_1,node_2,distance,direction: str,twoway = True):
        """
        Add the street to the DiGraph instance.

        :param node_1:Intersection of the street, informed by two street names.
        :param node_2: The other intersection of the street.
        :param distance: The distance of the street.
        :param direction: The drection from node_1 to node_2.
        :param twoway: Whether the street two-way or one-way.
        """
        # Find the street name from the node_1 and node_2.
        for i in node_1:
            for j in node_2:
                if i == j:
                    street_name = i

        self.G.add_edge(node_1,node_2,weight = distance, direct = direction, street = street_name)
        # add the reverse direction of the street if the street is two way
        if twoway:
            if direction == 'S':
                direction = 'N'
            elif direction == 'N':
                direction = 'S'
            elif direction == 'E':
                direction ='W'
            else:
                direction = 'E'
            self.G.add_edge( node_2, node_1, weight = distance, direct = direction, street = street_name)

#method to find the shortest way
    def find_shortest_way(self):
        pass


#print the result
x = Navigation()
x.add_edge(('E Daniel St', 'S 4th St'), ('E Daniel St', 'S 5th St'), 130, 'E', twoway=True)
x.add_edge(('E Daniel St', 'S 5th St'), ('E Daniel St', 'S 6th St'), 140, 'E')
x.add_edge(('E Daniel St', 'S 6th St'), ('E Daniel St', 'S Wright St'), 130, 'E', False)
x.add_edge(('E Daniel St', 'S 4th St'), ('E Chamlers St', 'S 4th St'), 130, 'S')
x.add_edge(('E Daniel St', 'S 5th St'), ('E Chamlers St', 'S 5th St'), 130, 'S')
x.add_edge(('E Daniel St', 'S 6th St'), ('E Chamlers St', 'S 6th St'), 130, 'S', False)
x.add_edge(('E Daniel St', 'S Wright St'), ('E Chamlers St', 'S Wright St'), 130, 'S')
x.add_edge(('E Chamlers St', 'S 4th St'), ('E Chamlers St', 'S 5th St'), 130, 'E')
x.add_edge(('E Chamlers St', 'S 5th St'), ('E Chamlers St', 'S 6th St'), 140, 'E')
x.add_edge(('E Chamlers St', 'S Wright St'), ('E Chamlers St', 'S 6th St'), 110, 'W', False)
x.add_edge(('E Chamlers St', 'S 4th St'), ('E Armory St', 'S 4th St'), 160, 'S')
x.add_edge(('E Chamlers St', 'S 5th St'), ('University of illinois Armory', 'S 5th St','E Armory St'), 160, 'S')
x.add_edge(('E Chamlers St', 'S 6th St'), ('E Armory St', 'S 6th St'), 160, 'S', False)
x.add_edge(('E Armory St', 'S Wright St'), ('E Chamlers St', 'S Wright St'), 160, 'N', False)

x.add_edge(('E Armory St', 'S 4th St'), ('University of illinois Armory', 'S 5th St','E Armory St'), 130, 'E')
x.add_edge(('University of illinois Armory', 'S 5th St','E Armory St'), ('E Armory St', 'S 6th St'), 140, 'E')
x.add_edge(('E Armory St', 'S 6th St'), ('E Armory St', 'S Wright St'), 130, 'E', False)

x.add_edge(('E Armory St', 'S 4th St'), ('E Gregory Dr', 'S 4th St'), 140, 'S')
x.add_edge(('E Armory St', 'S 6th St'), ('E Gregory Dr', 'S 6th St'), 140, 'S')

x.add_edge(('E Gregory Dr', 'S 4th St'), ('E Gregory Dr', 'S 6th St'), 270, 'E')

x.add_edge(('E Gregory Dr', 'S 4th St'), ('E Peabody Dr', 'S 4th St'), 300, 'S')
x.add_edge(('E Gregory Dr', 'S 6th St'), ('E Peabody Dr', 'S 6th St'), 300, 'S')
x.add_edge(('E Peabody Dr', 'S 4th St'), ('E Peabody Dr', 'S 6th St'), 270, 'E')

x.add_edge(('W Gregory Dr', 'S 6th St'), ('W Gregory Dr', 'S Goodwin Ave'), 560, 'E')

x.add_edge(('South Goodwin Ave', 'S Goodwin Ave'), ('W Nevada St', 'S Goodwin Ave'), 200, 'N')
x.add_edge(('W Nevada St', 'S Lincoln Ave'), ('W Pennsylvania Ave', 'S Lincoln Ave'), 600, 'S')
x.add_edge(('W Pennsylvania Ave', 'S Lincoln Ave'), ('W Pennsylvania Ave', 'S Dorner Dr'), 220, 'W')
x.add_edge(('W Pennsylvania Ave', 'S Dorner Dr'), ('W Peabody Dr', 'S Dorner Dr'), 100, 'N')
x.add_edge(('W Peabody Dr', 'S Dorner Dr'), ('Allen Hall and Unit One', 'S Dorner Dr','South Goodwin Ave'), 300, 'N')
x.add_edge(('Allen Hall and Unit One', 'S Dorner Dr','South Goodwin Ave'), ('South Goodwin Ave', 'S Goodwin Ave'), 170, 'W')

x.add_edge(('W Peabody Dr', 'S Dorner Dr'), ('W Peabody Dr', 'S Goodwin Ave'), 230, 'W')
x.add_edge(('W Peabody Dr', 'S Goodwin Ave'), ('Funk Agricultural Constitute/Funk ACES', 'S Goodwin Ave'), 100, 'N')

##building:
x.add_building('School of Information Sciences','E Daniel St',('E Daniel St', 'S 5th St'),30,'W',('E Daniel St', 'S 6th St'),110,'E')
x.add_building('English Building','S Wright St',('E Daniel St','S Wright St'),30,'N',('E Chalmers St','S Wright St'),100,'S')
x.add_building('Lincoln Hall','S Wright St',('E Chalmers St','S Wright St'),30,'N',('E Armory Ave','S Wright St'),130,'S')
x.add_building('UI Ice Arena','E Armory Ave',('E Armory Ave','S 4th St'),65,'W',('E Armory Ave','S 5th St'),65,'E')
x.add_building('Carl R. Woese Institute for Genomic Biology','S 6th St',('E Chalmers St','S 6th St'),90,'N',('E Armory Ave','S 6th St'),70,'S')
x.add_building('School of Art+Design','E Peabody Dr',('E Peabody Dr','S 4th St'),130,'W',('E Peabody Dr','S 6th St'),140,'E')
x.add_building('Undergraduate Library','W Gregory Dr',('W Gregory Dr','S 6th St'),280,'W',('South Goodwin Ave','S Goodwin Ave'),280,'E')
x.add_building('University of illinois Extension/Mumford Hall','W Gregory Dr',('W Gregory Dr','S 6th St'),330,'W',('South Goodwin Ave','S Goodwin Ave'),230,'E')
x.add_building('Carl R. Woese Institute for Genomic Biology','W Gregory Dr',('W Gregory Dr','S 6th St'),460,'W',('South Goodwin Ave','S Goodwin Ave'),100,'E')
x.add_building('Freer Hall','W Gregory Dr',('South Goodwin Ave','S Goodwin Ave'),140,'W',('South Goodwin Ave','S Dorner Dr'),30,'E')
x.add_building('Mckinley Health Center','S Lincoln Ave',('W Nevada St','S Lincoln Ave'),400,'N',('W Pennsylvania Ave','S Lincoln Ave'),200,'S')
x.add_building('Foreign Language Building','W Mattews Ave',('W Nevada St','W Mattews Ave'),40,'S',('W Oregon St','W Mattews Ave'),70,'N')
x.add_building('Davenport Hall','W Mattews Ave',('W Oregon St','W Mattews Ave'),25,'S',('W Illinois St','W Mattews Ave'),205,'N')
x.add_building('School of Social Work','W Nevada St',('W Nevada St','S Gregory St'),40,'W',('W Nevada St','S Lincoln Ave'),160,'E')
x.add_building('Spurlock Museum','S Gregory St',('W Oregon St','S Gregory St'),68,'S',('W Illinois St','S Gregory St'),162,'N')
x.add_building('Institute of Government and public Affairs','W Nevada St',('W Nevada St','S Gregory St'),25,'W',('W Nevada St','S Lincoln Ave'),175,'E')
x.add_building('Dance Studio','W Nevada St',('W Nevada St','S Gregory St'),70,'W',('W Nevada St','S Lincoln Ave'),130,'E')
x.add_building('Huff Hall','E Gregory Dr',('E Gregory Dr','S 4th St'),20,'W',('E Gregory Dr','S 6th St'),250,'E')


x.add_edge(('W Nevada St','W Mattews Ave'),('W Nevada St','S Goodwin Ave'),140,'E')
x.add_edge(('W Nevada St','S Goodwin Ave'),('W Nevada St','S Gregory St'),200,'E')
x.add_edge(('W Nevada St','S Gregory St'),('W Nevada St','S Lincoln Ave'),200,'E')

x.add_edge(('W Oregon St','S Goodwin Ave'),('W Oregon St','W Mattews Ave'),140,'W')
x.add_edge(('W Oregon St','S Goodwin Ave'),('W Oregon St','S Gregory St'),200,'E')
x.add_edge(('W Oregon St','S Gregory St'),('W Oregon St','S Lincoln Ave'),200,'E')

x.add_edge(('W Illinois St','W Mattews Ave'),('W Illinois St','S Goodwin Ave'),140,'E')
x.add_edge(('W Illinois St','S Goodwin Ave'),('W Illinois St','S Gregory St'),200,'E')
x.add_edge(('W Illinois St','S Gregory St'),('W Illinois St','S Lincoln Ave'),200,'E')

x.add_edge(('W Nevada St','W Mattews Ave'),('W Oregon St','W Mattews Ave'),110,'S')
x.add_edge(('W Oregon St','W Mattews Ave'),('W Illinois St','W Mattews Ave'),230,'S')

x.add_edge(('W Oregon St','S Goodwin Ave'),('W Nevada St','S Goodwin Ave'),110,'N')
x.add_edge(('W Illinois St','S Goodwin Ave'),('W Oregon St','S Goodwin Ave'),230,'N')

x.add_edge(('W Nevada St','S Gregory St'),('W Oregon St','S Gregory St'),110,'N')
x.add_edge(('W Oregon St','S Gregory St'),('W Illinois St','S Gregory St'),230,'N')

x.add_edge(('W Nevada St','S Lincoln Ave'),('W Oregon St','S Lincoln Ave'),110,'N')
x.add_edge(('W Oregon St','S Lincoln Ave'),('W Illinois St','S Lincoln Ave'),230,'N')

#add_building(self,building: str,street,node_1,node_1_distance,node_1_direction,node_2,node_2_direction,node_2_distance):


#'E Daniel St'
#'S 4th St'
#'S 5th St'
#'S 6th St'
#'S Wright St'
#'E Chamler St'
#'E Armory St'
#'E Gregory'

#def add_building(self, building: str, street, node_1, node_1_distance, node_1_direction, node_2, node_2_distance,node_2_direction):
x.add_building('School of Information Sciences','E Daniel St',('E Daniel St', 'S 5th St'),30,'W',('E Daniel St', 'S 6th St'),110,'E')
print(x.G['E Daniel St', 'S 5th St']['School of Information Sciences','E Daniel St'])
print(x.G['School of Information Sciences','E Daniel St']['E Daniel St', 'S 5th St'])
print(x.G['School of Information Sciences','E Daniel St']['E Daniel St', 'S 6th St'])
print(x.G['E Daniel St', 'S 6th St']['School of Information Sciences','E Daniel St'])

print(list(x.G.nodes()))
print(list(x.G.edges()))



