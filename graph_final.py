import networkx as nx




class Navigation:

    def __init__(self):
        # Create an instance of networkx DiGraph class as the class Navigation attribute
        self.G = nx.DiGraph()
        # Create a dictionary to store the building nodes.
        self.Building2Node={}

    def add_building(self, building, street,node_1,node_1_distance,node_1_direction,node_2,node_2_distance,node_2_direction):

        """
        Add the building to the map, and add the edge between the buildings and intersections automatically.
        :param building: Building Name of the building.
        :param street: Street name of the Street.
        :param node_1: One of the two intersections of the street.
        :param node_1_distance: The distance from building to node_1.
        :param node_1_direction: The direction from building to node_1
        :param node_2: The other intersection of the street.
        :param node_2_distance: The distance from building to node_2.
        :param node_2_direction: The direction from building to node_2
        """
        # Create building node by building name and street name.
        building_node=(building,street)
        # Store every building nodes to the dictionary.
        self.Building2Node[building]=building_node
        # Whether there is access from node_1 to node_2.
        from2ToExist = self.G.get_edge_data(node_1, node_2) != None
        to2FromExist = self.G.get_edge_data(node_2, node_1) != None

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
        Add the street between two intersection.
        :type street_name: str
        :param from_: start node, A tuple made of two streets.
        :param to: end node
        :param distance: the weight for every edge
        :param orientation: set the default one orientation
        :param twoway: default one-way
        :return: 
        """

        # Find out the street name by searching two nodes.
        for i in from_:
            for j in to:
                if i == j:
                    edge_name = i


        self.G.add_edge(from_, to, weight=distance, orientation=orientation, edge_name=edge_name)

        # If the street is two-direction, we create the other direction automatically.
        if twoway:
            oppose = {
                'N': 'S',
                'S': 'N',
                'E': 'W',
                'W': 'E',
            }
            # Use different meta
            self.G.add_edge(
                to,from_, weight=distance,orientation=oppose[orientation], edge_name=edge_name
            )

    def shorestPath(self,source,dest):
        """
        Find the shortest path between two building.
        :param source: the input start map code
        :param dest: the input destination map code
        :return: the minimum path 
        """
        # Find the real building node stored in the map using building name.
        src = self.Building2Node[source]
        dst = self.Building2Node[dest]
        # Use the inside method to find out the path.
        path2Node= nx.algorithms.shortest_paths.weighted.dijkstra_path(self.G,src,dst,weight='weight')
        street=[]
        orientation=[]
        # Store the shortest path with two lists
        street.append(self.G.get_edge_data(path2Node[0],path2Node[1])['edge_name'])
        orientation.append(self.G.get_edge_data(path2Node[0], path2Node[1])['orientation'])
        print("Starting on ", path2Node[0][1], "turn ", orientation[0])
        # Explain and print out the path.
        for i in range(1,len(path2Node)-1):
            orientation.append(self.G.get_edge_data(path2Node[i],path2Node[i+1])['orientation'])
            street.append(self.G.get_edge_data(path2Node[i],path2Node[i+1])['edge_name'])
            if street[i]!=street[i-1]:
                print("At",street[i],"turn ",orientation[i])
        print("Processed until you arrive at ",dst[0])


def main():
    """
    constrct an instance
    """
    school_map = Navigation()


    # Store every street to the map
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

    school_map.add_edge(('E Chamlers St', 'S 4th St'), ('E Armory Ave', 'S 4th St'), 160, 'S', twoway=True)
    school_map.add_edge(('E Chamlers St', 'S 5th St'), ('S 5th St', 'E Armory Ave'), 160, 'S', twoway=True)
    school_map.add_edge(('E Chamlers St', 'S 6th St'), ('E Armory Ave', 'S 6th St'), 160, 'S')
    school_map.add_edge(('E Armory Ave', 'S Wright St'), ('E Chamlers St','S Wright St'), 160, 'N')

    school_map.add_edge(('E Armory Ave', 'S 4th St'), ('E Armory Ave', 'S 5th St'), 130, 'E', twoway=True)
    school_map.add_edge(('E Armory Ave', 'S 5th St'), ('E Armory Ave', 'S 6th St'), 140, 'E', twoway=True)
    school_map.add_edge(('E Armory Ave', 'S 6th St'), ('E Armory Ave', 'S Wright St'), 130, 'E')

    school_map.add_edge(('E Armory Ave', 'S 4th St'), ('E Gregory Dr', 'S 4th St'), 140, 'S', twoway=True)
    school_map.add_edge(('E Armory Ave', 'S 6th St'), ('E Gregory Dr', 'S 6th St'), 140, 'S', twoway=True)

    school_map.add_edge(('W Nevada St', 'S Mathews Ave'), ('W Nevada St', 'S Goodwin Ave'), 140, 'E')
    school_map.add_edge(('W Nevada St', 'S Goodwin Ave'), ('W Nevada St', 'S Gregory St'), 200, 'E', twoway=True)
    school_map.add_edge(('W Nevada St', 'S Gregory St'), ('W Nevada St', 'S Lincoln Ave'), 200, 'E', twoway=True)

    school_map.add_edge(('W Oregon St', 'S Goodwin Ave'), ('W Oregon St', 'S Mathews Ave'), 140, 'W')
    school_map.add_edge(('W Oregon St', 'S Goodwin Ave'), ('W Oregon St', 'S Gregory St'), 200, 'E', twoway=True)
    school_map.add_edge(('W Oregon St', 'S Gregory St'), ('W Oregon St', 'S Lincoln Ave'), 200, 'E', twoway=True)

    school_map.add_edge(('W Illinois St', 'S Mathews Ave'), ('W Illinois St', 'S Goodwin Ave'), 200, 'E', twoway=True)
    school_map.add_edge(('W Illinois St', 'S Goodwin Ave'), ('W Illinois St', 'S Gregory St'), 200, 'E', twoway=True)
    school_map.add_edge(('W Illinois St', 'S Gregory St'), ('W Illinois St', 'S Lincoln Ave'), 200, 'E', twoway=True)

    school_map.add_edge(('W Illinois St', 'S Mathews Ave'), ('W Oregon St', 'S Mathews Ave'), 200, 'S')
    school_map.add_edge(('W Oregon St', 'S Mathews Ave'), ('W Nevada St', 'S Mathews Ave'), 110, 'S')

    school_map.add_edge(('W Oregon St', 'S Goodwin Ave'), ('W Nevada St', 'S Goodwin Ave'), 110, 'S', twoway=True)
    school_map.add_edge(('W Illinois St', 'S Goodwin Ave'), ('W Oregon St', 'S Goodwin Ave'), 230, 'S', twoway=True)

    school_map.add_edge(('W Nevada St', 'S Gregory St'), ('W Oregon St', 'S Gregory St'), 110, 'N', twoway=True)
    school_map.add_edge(('W Oregon St', 'S Gregory St'), ('W Illinois St', 'S Gregory St'), 230, 'N', twoway=True)

    school_map.add_edge(('W Nevada St', 'S Lincoln Ave'), ('W Oregon St', 'S Lincoln Ave'), 110, 'N', twoway=True)
    school_map.add_edge(('W Oregon St', 'S Lincoln Ave'), ('W Illinois St', 'S Lincoln Ave'), 230, 'N', twoway=True)

    school_map.add_edge(('E Gregory Dr', 'S 4th St'), ('E Gregory Dr', 'S 6th St'), 280, 'E', twoway=True)
    school_map.add_edge(('E Gregory Dr', 'S 4th St'), ('E Peabody Dr', 'S 4th St'), 300, 'S', twoway=True)
    school_map.add_edge(('E Gregory Dr', 'S 6th St'), ('E Peabody Dr', 'S 6th St'), 300, 'S', twoway=True)
    school_map.add_edge(('E Peabody Dr', 'S 4th St'), ('E Peabody Dr', 'S 6th St'), 280, 'E', twoway=True)

    school_map.add_edge(('E Gregory Dr', 'S 6th St'), ('E Gregory Dr', 'W Gregory Dr'), 130, 'E', twoway=True)
    school_map.add_edge(('E Gregory Dr', 'W Gregory Dr'), ('W Gregory Dr', 'S Goodwin Ave'), 400, 'E', twoway=True)

    school_map.add_edge(('W Gregory Dr', 'S Goodwin Ave'), ('W Nevada St', 'S Goodwin Ave'), 200, 'N', twoway=True)
    school_map.add_edge(('W Nevada St', 'S Lincoln Ave'), ('W Pennsylvania Ave', 'S Lincoln Ave'), 600, 'S', twoway=True)
    school_map.add_edge(('W Pennsylvania Ave', 'S Lincoln Ave'), ('W Pennsylvania Ave', 'S Dorner Dr'), 220, 'W', twoway=True)
    school_map.add_edge(('W Pennsylvania Ave', 'S Dorner Dr'), ('W Peabody Dr', 'S Dorner Dr'), 100, 'N', twoway=True)
    school_map.add_edge(('W Peabody Dr', 'S Dorner Dr'), ( 'W Gregory Dr','S Dorner Dr'), 300,
               'N', twoway=True)
    school_map.add_edge(('W Gregory Dr','S Dorner Dr'), ('W Gregory Dr', 'S Goodwin Ave'),170, 'W', twoway=True)

    school_map.add_edge(('W Peabody Dr', 'S Dorner Dr'), ('W Peabody Dr', 'South Goodwin Ave'), 230, 'W', twoway=True)



    ##building:
    school_map.add_building('ischool','E Daniel St',('E Daniel St', 'S 5th St'),30,'W',('E Daniel St', 'S 6th St'),110,'E')
    school_map.add_building('English Building', 'S Wright St',('E Chamlers St', 'S Wright St'), 100, 'S',('E Daniel St', 'S Wright St'), 30, 'N')
    school_map.add_building('Lincoln Hall', 'S Wright St', ('E Armory Ave', 'S Wright St'), 130, 'S',('E Chamlers St', 'S Wright St'), 30, 'N')
    school_map.add_building('UI Ice Arena', 'E Armory Ave', ('E Armory Ave', 'S 4th St'), 65, 'W', ('E Armory Ave', 'S 5th St'),
                   65, 'E')
    school_map.add_building('Carl R. Woese Institute for Genomic Biology', 'S 6th St', ('E Chalmers St', 'S 6th St'), 90, 'N',
                   ('E Armory Ave', 'S 6th St'), 70, 'S')
    school_map.add_building('School of Art+Design', 'E Peabody Dr', ('E Peabody Dr', 'S 4th St'), 130, 'W',
                   ('E Peabody Dr', 'S 6th St'), 140, 'E')
    school_map.add_building('Undergraduate Library', 'W Gregory Dr', ('E Gregory Dr', 'W Gregory Dr'), 100, 'W',
                   ('W Gregory Dr', 'S Goodwin Ave'), 300, 'E')
    school_map.add_building('University of illinois Extension/Mumford Hall','W Gregory Dr', ('E Gregory Dr', 'W Gregory Dr'), 200,
                   'W', ('W Gregory Dr', 'S Goodwin Ave'), 200, 'E')
    school_map.add_building('Carl R. Woese Institute for Genomic Biology', 'W Gregory Dr', ('E Gregory Dr', 'W Gregory Dr'), 300,
                   'W', ('W Gregory Dr', 'S Goodwin Ave'), 100, 'E')
    school_map.add_building('Freer Hall', 'W Gregory Dr', ('W Gregory Dr', 'S Goodwin Ave'), 140, 'W',
                   ('W Gregory Dr', 'S Dorner Dr'), 30, 'E')
    school_map.add_building('Mckinley Health Center', 'S Lincoln Ave', ('W Nevada St', 'S Lincoln Ave'), 400, 'N',
                   ('W Pennsylvania Ave', 'S Lincoln Ave'), 200, 'S')
    school_map.add_building('Foreign Languages Building', 'S Mathews Ave', ('W Nevada St', 'S Mathews Ave'), 40, 'S',
                   ('W Oregon St', 'S Mathews Ave'), 70, 'N')
    school_map.add_building('Davenport Hall', 'S Mathews Ave', ('W Oregon St', 'S Mathews Ave'), 25, 'S',
                   ('W Illinois St', 'S Mathews Ave'), 205, 'N')
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
    school_map.add_building('University of illinois Armory', 'E Armory Ave',('E Armory Ave', 'S 4th St'),125,'W',('E Armory Ave', 'S 5th St'),5,'E')
    school_map.add_building('Allen Hall and Unit One','W Gregory Dr',('W Gregory Dr', 'S Dorner Dr'),5,'E',('W Gregory Dr', 'S Goodwin Ave'),165,'W')
    school_map.add_building('Office of the Registrar', 'S Gregory St', ('W Oregon St', 'S Gregory St'), 170, 'S',('W Illinois St', 'S Gregory St'), 50, 'N')

    response = True
    while response:
            #input the map_code and put the parameter into the function
            building_code = {50: 'Allen Hall and Unit One',
                             195: 'Carl R. Woese Institute for Genomic Biology',
                             39: 'Dance Studio',
                             151: 'Davenport Hall',
                             718: 'English Building',
                             162: 'Foreign Languages Building',
                             52: 'Freer Hall',
                             #631: 'Funk Agricultural Constitute/Funk ACES',
                             584: 'Huff Hall',
                             36: 'Institute of Government and public Affairs',
                             456: 'Lincoln Hall',
                             26: 'Mckinley Health Center',
                             590: 'School of Art+Design',
                             37: 'School of Social Work',
                             65: 'Spurlock Museum',
                             525: 'UI Ice Arena',
                             522: 'Undergraduate Library',
                             526: 'University of illinois Armory',
                             710: 'University of illinois Extension/Mumford Hall',
                             493: 'ischool',
                             612:'Office of the Registrar'}

            # print out the building information.
            for i in building_code:
                print(i, building_code[i])

            # Filter two zip codes.
            str,stp = input(" Enter starting and ending mail codes: ").split()
            str = int(str)
            stp = int(stp)
            # Find and print out the shortest path.
            print("Showing the shortest route from", building_code[str], "to", building_code[stp])
            school_map.shorestPath(building_code[str],building_code[stp])
            response = False
            response = input("Continue or Quit? Enter Y if continue and N to quit")
            if response == 'Y':
                response = True
            else:
                response = False

    print('Finish!')

if __name__=='__main__':
        main()
