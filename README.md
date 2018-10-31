# Author-Network-Analysis

### Description

##### This repository provides Python code for undertaking network analyis of authors from publications. The code produces a graph model for which nodes show authors and edges show connections for coauthors which appear on the same paper. The code calculates key centrality measures including degree, eigenvector and betweeness centrality. The resulting graph model can be exported to Gephi where visualisations  the one below was produced for researchers in the field of infectious disease epidemiology. The code is useful for identifying key researchers within a field and connections between communtiies. It could also be used by research funding organisations to inform decision making: for example, the identification of peer reviewers and members for review committees. The following article was useful in developing this approach: https://programminghistorian.org/en/lessons/exploring-and-analyzing-network-data-with-python 

### Pre-requisities

##### - Networkx
##### - Python-louvain == 0.5
##### - Pandas
##### - NumPy
##### - Matplotlib.pyplot

### Directions on use

#####Save list of publications in a CSV file. Update main.py file with file_name and directory. Run main.py which will execute code in util.py, graph_builder.py and network_analysis_builder.py. An additional line can be added to export the graph model to Gephi. 

### Example output

![Alt text](./network_analysis.png?raw=true "Author Network Analysis")
