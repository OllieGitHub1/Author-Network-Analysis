%reload_ext autoreload
%autoreload 2
from util import run_programme as run_util
from graph_builder import run_programme as run_graph_builder 
from network_analysis_builder import run_programme as run_network_analysis_builder

directory = 'C:\\Users\WillsO\\OneDrive - Wellcome Cloud\\Python programmes\\Papers to scrape\\'
file_name = 'all references.csv'

(authors, author_lists) = run_util(directory, file_name)
(nodes, edges) = run_graph_builder(authors, directory, author_lists)
network_results = run_network_analysis_builder(directory)


