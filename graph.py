# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:38:37 2017

@author: Shekar
"""

class Graph():
    def __init__(self, nodes=[], edges=[]):
        self.nodes = set(nodes)     #Create a set of nodes. 
                                    #Sets contain unique elements
        self.edges = set(edges)     #Create a set of edges(source, destination)
        self.graph = self.construct_graph()
        
    def construct_graph(self):
        """
        This function creates a graph using a dictionary data structure
        
        @param self.edges: Picks up the edges set from the object
        @return: Returns a dictionary containing the graph structure
        """
        graph = {}
        for source, dest in self.edges:
            if source in graph.keys():
                graph[source].append(dest)
            else:
                graph[source] = [dest]
        return graph
    
    def add_edge(self, source, dest):
        """
        This function adds an edge to the graph if it doesn't exist
        
        @param source: String of the source node
        @param dest: String of the destination node
        @return: Null
        """
        if (source,dest) not in self.edges and (source!=dest):
            self.nodes.add(source)
            self.nodes.add(dest)
            self.edges.add((source, dest))
            if source in self.graph.keys():
                self.graph[source].append(dest)
            else:
                self.graph[source] = [dest]
                
    def has_edge(self, source, dest):
        if (source, dest) in self.edges:
            return True
        else:
            return False
                
    def add_node(self, node):
        """
        This function adds a node to the graph if it doesn't exist
        
        @param node: String of the node to be added
        @return: Null
        """
        if node not in self.nodes:
            self.nodes.add(node)
            self.graph[node] = []
            
    def complete_graph(self):
        """
        Generates a complete graph
        """
        node_list = list(self.nodes)
        for e1 in node_list:
            for e2 in node_list:
                self.add_edge(e1, e2)
    
    def __str__(self):
        """
        Prints the details of the graph
        """
        op = 'Node List: \n'
        op += str(self.nodes)
        op += '\n\nEdge List: \n'
        op += str(self.edges)
        return op