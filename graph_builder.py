import os 
import itertools 
import pandas as pd 

def generate_node_list(unambiguous_authors, directory):
    author_set = set()
    for author in unambiguous_authors:
        if len(author) > 2:
            author_set.add(author)
    node_list = list(author_set)
    nodes = pd.DataFrame({'Node':node_list})
    file_path = os.path.join(directory, 'nodes.csv')
    nodes.to_csv(file_path, encoding='latin1', index=False)
    return (node_list, nodes) 

def generate_edge_list(node_list, directory, unambiguous_author_lists):
    """
    Generates a set of authors based on how names appear on papers
    Input: List of authors
    Output: List of unique authors based on how they appear
    """
    l1, l2 = [], []
    for unambiguous_author_list in unambiguous_author_lists:
        print(unambiguous_author_list)
        for combination in itertools.combinations(unambiguous_author_list,2):
            print('combination', combination)
            l1.append(combination[0])
            l2.append(combination[1])
    edges = pd.DataFrame({'Source':l1, 'Target': l2})
    file_path = os.path.join(directory, 'edges.csv')
    edges.to_csv(file_path, encoding='latin1', index=False)
    return edges

def run_programme(unambiguous_authors, directory, unambiguous_author_lists):
    (node_list, nodes) = generate_node_list(unambiguous_authors, directory)
    edges = generate_edge_list(node_list, directory, unambiguous_author_lists)
    return (nodes, edges)
