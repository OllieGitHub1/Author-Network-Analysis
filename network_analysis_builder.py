import os 
import csv
import pandas as pd
import networkx as nx
from operator import itemgetter
import matplotlib.pyplot as plt

def load_file(directory):
    
    file_path_1 = os.path.join(directory, 'nodes.csv')
    file_path_2 = os.path.join(directory, 'edges.csv')
    
    with open(file_path_1, 'r') as nodecsv: # Open the file                       
        nodereader = csv.reader(nodecsv) # Read the csv  
        nodes = [n for n in nodereader][1:]                     
        node_names = [n[0] for n in nodes] # Get a list of only the node names                                       

    with open(file_path_2, 'r') as edgecsv: # Open the file
        edgereader = csv.reader(edgecsv) # Read the csv     
        edges = [tuple(e) for e in edgereader][1:] # Retrieve the dat
    return (nodes, edges, node_names)

def build_graph(nodes, edges, node_names):
    G = nx.Graph() # Initialize a Graph object                                                        
    G.add_nodes_from(node_names) # Add nodes to the Graph                             
    G.add_edges_from(edges) # Add edges to the Graph  
    return G

def calculate_centrality_measures(G):
    degree_dict = dict(G.degree(G.nodes()))
    betweenness_dict = nx.betweenness_centrality(G) # Run betweenness centrality
    eigenvector_dict = nx.eigenvector_centrality(G)
    nx.set_node_attributes(G, degree_dict, 'degree')
    nx.set_node_attributes(G, betweenness_dict, 'betweenness')
    nx.set_node_attributes(G, eigenvector_dict, 'eigenvector')
    return (degree_dict, betweenness_dict, eigenvector_dict)

def build_data_frames(degree_dict, betweeness_dict, eigenvector_dict):

    dicts = [degree_dict, betweeness_dict, eigenvector_dict]

    super_dict = {}
    for d in dicts:
        for k, v in d.items():  # d.items() in Python 3+
            super_dict.setdefault(k, []).append(v)

    df = pd.DataFrame.from_items(super_dict.items(), orient='index', columns=['Degree','Eigenvector','Betweeness'])
    return df

def run_programme(directory):
    (nodes, edges, node_names) = load_file(directory)
    G = build_graph(nodes, edges, node_names)
    (degree_dict, betweenness_dict, eigenvector_dict) = calculate_centrality_measures(G)
    df = build_data_frames(degree_dict, betweenness_dict, eigenvector_dict)
    return df
 
    
