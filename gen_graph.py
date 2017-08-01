# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 10:56:46 2017

@author: shek628
"""

from graph import Graph
import argparse
import random

def generate_graph(num_nodes, num_edges, seed):
    """
    This function generates a random graph
    
    @param num_nodes - Number of nodes to be generated
    @param num_edges - Number of edges
    @param seed - Seed for RNG
    """
    G = Graph()
    for i in range(num_nodes):
        G.add_node(i)
        
    if seed is not None:
        random.seed(seed)
        
    if num_nodes ==1:       #If the num of nodes = 1. Return as is
        return G
    
    max_edges = num_nodes * (num_nodes - 1) #Calc max possible edges
    #If the number of edges requested is more than max_edges. Return a complete graph
    if num_edges > max_edges:
        print("Generating complete graph")
        G.complete_graph()
        return G
    
    edge_count = 0
    while edge_count < num_edges:
        source = random.choice(list(G.nodes))
        dest = random.choice(list(G.nodes))
        if source==dest or G.has_edge(source, dest):
            continue
        else:
            G.add_edge(source, dest)
            edge_count += 1
    return G


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Generates a random directed graph')
    parser.add_argument('-n', dest='nodes', type=int, help='Defines number of nodes (Required)', required=True)
    parser.add_argument('-e', dest='edges', type=int, help='Defines number of edges (Required)', required=True)
    parser.add_argument('-s', dest='seed', type=int, help='Seed for random number generator (default=None)')
    parser.add_argument('-p', dest='plot', type=str, help='Output the graph in a png file. Requires pygraphviz library')
    args = parser.parse_args()

    if (args.nodes is None) or (args.edges is None):
        parser.print_help()
    else:
        G = generate_graph(args.nodes, args.edges, args.seed)
        print(G)
    
    if args.plot is not None:
        try:
            import pygraphviz as pgv
            g = pgv.AGraph()
            for s,d in G.edges:
                g.add_edge(s, d)
            g.draw(args.plot +'.png')
        except ModuleNotFoundError:
            print("\nUnable to import Pygraphviz. Please install using 'pip install pygraphviz'")
            pass
        

    