# Network Analysis of Academic Publications

This repository provides Python code for undertaking network analysis of authors on academic publications. The code produces a graph model with authors as nodes and edges as connections between authors which appear on the same paper. The influence of different authors is etimated using centrality measures including degree, eigenvector and betweeness centrality. The resulting graph model can be exported to Gephi where visualisations can be produced like the one below. The outputs of this tool could help to identify influential researchers, perhaps informing funding decisions and helping to reduce conflicts of interest in peer review and funding committee decisions. 

## Prerequisities
Networkx, Python-louvain, Pandas, NumPy, Matplotlib.pyplot

## Directions on use
Save publications in a CSV file. Update main.py file with file_name and directory. Run main.py which will execute code in util.py, graph_builder.py and network_analysis_builder.py. An additional line can be added to export the graph model to Gephi. 

## References
This [article](https://programminghistorian.org/en/lessons/exploring-and-analyzing-network-data-with-python) was useful in developing the network analysis methodology.

## Example output<br>
![Alt text](./network_analysis.png?raw=true "Author Network Analysis")
