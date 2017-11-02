import networkx as nx

class Navigation():

    def __init__(self):
        self.G = nx.DiGraph()


    def add_building(self,building: str,street,node_1,node_1_distance,node_1_direction,node_2,node_2_distance,node_2_direction, On_inter = False):
        # two way
        building_node = (building,street)
        if self.G.get_edge_data(node_1,node_2)!= None:
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
        # single way


    def add_edge(self,node_1,node_2,distance,direction: str,twoway = True):
        for i in node_1:
            for j in node_2:
                if i == j:
                    street_name = i

        self.G.add_edge(node_1,node_2,weight = distance, direct = direction, street = street_name)

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
x.add_edge(('W Peabody Dr', 'S Dorner Dr'), ('University of illinois Armory', 'S 5th St','E Armory St'), 300, 'N')
x.add_edge(('University of illinois Armory', 'S 5th St','E Armory St'), ('South Goodwin Ave', 'S Goodwin Ave'), 170, 'W')

x.add_edge(('W Peabody Dr', 'S Dorner Dr'), ('W Peabody Dr', 'S Goodwin Ave'), 230, 'W')
x.add_edge(('W Peabody Dr', 'S Goodwin Dr'), ('Funk Agricultural Constitute/Funk ACES', 'S Goodwin Ave'), 100, 'N')

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


#'E Daniel St'
#'S 4th St'
#'S 5th St'
#'S 6th St'
#'S Wright St'
#'E Chamler St'
#'E Armory St'
#'E Gregory'
ischool
University of illinois Armory
School of Art+Design
Huff Hall
English Building
Lincoln Hall
Davenport Hall
Foreign Languages Building
Undergraduate Library
University of illinois Extension/Mumford Hall
Funk Agricultural Constitute/Funk ACES
Freer Hall
School of Social Work
Dance Studio
Institute of Government and public Affairs
Allen Hall and Unit One
Mckinley Health Center
UI Ice Arena
Carl R. Woese Institute for Genomic Biology
Spurlock Museum

#def add_building(self, building: str, street, node_1, node_1_distance, node_1_direction, node_2, node_2_distance,node_2_direction):
x.add_building('School of Information Sciences','E Daniel St',('E Daniel St', 'S 5th St'),30,'W',('E Daniel St', 'S 6th St'),110,'E')
print(x.G['E Daniel St', 'S 5th St']['School of Information Sciences','E Daniel St'])
print(x.G['School of Information Sciences','E Daniel St']['E Daniel St', 'S 5th St'])
print(x.G['School of Information Sciences','E Daniel St']['E Daniel St', 'S 6th St'])
print(x.G['E Daniel St', 'S 6th St']['School of Information Sciences','E Daniel St'])

print(list(x.G.nodes()))
print(list(x.G.edges()))



