import networkx as nx

class Navigation():

    def __init__(self):
        self.G = nx.DiGraph()


    def add_building(self,building: str,street,node_1,node_1_distance,node_1_direction,node_2,node_2_distance,node_2_direction):
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
            if direction == 'South':
                direction = 'North'
            elif direction == 'North':
                direction = 'Sounth'
            elif direction == 'East':
                direction ='West'
            else:
                direction = 'East'
            self.G.add_edge( node_2, node_1, weight = distance, direct = direction, street = street_name)
#method to find the shortest way

    def find_shortest_way(self):
        pass


#print the result
x = Navigation()
x.add_edge(('E Daniel St', 'S 4th St'), ('E Daniel St', 'S 5th St'), 130, 'East', twoway=True)
x.add_edge(('E Daniel St', 'S 5th St'), ('E Daniel St', 'S 6th St'), 140, 'East')
x.add_edge(('E Daniel St', 'S 6th St'), ('E Daniel St', 'S Wright St'), 130, 'East', False)
x.add_edge(('E Daniel St', 'S 4th St'), ('E Chamlers St', 'S 4th St'), 130, 'South')
x.add_edge(('E Daniel St', 'S 5th St'), ('E Chamlers St', 'S 5th St'), 130, 'South')
x.add_edge(('E Daniel St', 'S 6th St'), ('E Chamlers St', 'S 6th St'), 130, 'South', False)
x.add_edge(('E Daniel St', 'S Wright St'), ('E Chamlers St', 'S Wright St'), 130, 'South')
x.add_edge(('E Chamlers St', 'S 4th St'), ('E Chamlers St', 'S 5th St'), 130, 'East')
x.add_edge(('E Chamlers St', 'S 5th St'), ('E Chamlers St', 'S 6th St'), 140, 'East')
x.add_edge(('E Chamlers St', 'S Wright St'), ('E Chamlers St', 'S 6th St'), 110, 'West', False)
x.add_edge(('E Chamlers St', 'S 4th St'), ('E Armory St', 'S 4th St'), 160, 'South')
x.add_edge(('E Chamlers St', 'S 5th St'), ('E Armory St', 'S 5th St'), 160, 'South')
x.add_edge(('E Chamlers St', 'S 6th St'), ('E Armory St', 'S 6th St'), 160, 'South', False)
x.add_edge(('E Armory St', 'S Wright St'), ('E Chamlers St', 'S Wright St'), 160, 'North', False)

x.add_edge(('E Armory St', 'S 4th St'), ('E Armory St', 'S 5th St'), 130, 'East')
x.add_edge(('E Armory St', 'S 5th St'), ('E Armory St', 'S 6th St'), 140, 'East')
x.add_edge(('E Armory St', 'S 6th St'), ('E Armory St', 'S Wright St'), 130, 'East', False)

x.add_edge(('E Armory St', 'S 4th St'), ('E Gregory Dr', 'S 4th St'), 140, 'South')
x.add_edge(('E Armory St', 'S 6th St'), ('E Gregory Dr', 'S 6th St'), 140, 'South')

x.add_edge(('E Gregory Dr', 'S 4th St'), ('E Gregory Dr', 'S 6th St'), 270, 'East')


#'E Daniel St'
#'S 4th St'
#'S 5th St'
#'S 6th St'
#'S Wright St'
#'E Chamler St'
#'E Armory St'
#'E Gregory'

#def add_building(self, building: str, street, node_1, node_1_distance, node_1_direction, node_2, node_2_distance,node_2_direction):
x.add_building('School of Information Sciences','E Daniel St',('E Daniel St', 'S 5th St'),30,'West',('E Daniel St', 'S 6th St'),110,'East')
print(x.G['E Daniel St', 'S 5th St']['School of Information Sciences','E Daniel St'])
print(x.G['School of Information Sciences','E Daniel St']['E Daniel St', 'S 5th St'])
print(x.G['School of Information Sciences','E Daniel St']['E Daniel St', 'S 6th St'])
print(x.G['E Daniel St', 'S 6th St']['School of Information Sciences','E Daniel St'])

print(list(x.G.nodes()))
print(list(x.G.edges()))



