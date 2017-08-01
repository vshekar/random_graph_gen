random_graph_gen

#Synopsis
Short script to generate a random directed graph

#Details
Generates a random graph based on command line options
Graph object is implemented in graph.py
Command line script is gen_graph.py

#Usage
```
python gen_graph.py [-h] [-n NODES] [-e EDGES] [-s SEED] [-p PLOT]

optional arguments:
  -h, --help  show this help message and exit
  -n NODES    Defines number of nodes (Required)
  -e EDGES    Defines number of edges (Required)
  -s SEED     Seed for random number generator (default=None)
  -p PLOT     Output the graph in a png file. Requires pygraphviz library
```