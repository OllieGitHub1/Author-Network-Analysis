import os
import pandas as pd

def message(x = ''):
    
    while x not in ['Y', 'y', 'N', 'n']:
        x = input("Would you like to run analysis for first and last author only (Y/N): ")
    if x in ['N', 'n']:
        print("Analysis will run for all authors for papers in the datatset")
    return x 
    
def load_file(directory, file_name):
    """
    Load file into python notebook
    Input: Directory where file is stored and file name. Assumed file is in CSV format.
    Output: A dataframe containing publications
    """
    file_path = os.path.join(directory, file_name)
    publications = pd.read_csv(file_path, encoding ='latin1')
    
    return publications

def generate_data_structures(publications, x):
    """
    Sets up data structures used by programme
    Input: CSV file of publications with PMIDs, authors and RCRs 
    Output: Lists of authors and RCRs  
    """
    authors, number_authors, l = [], [], []
    author_lists = publications['Authors'].str.split(", ") #produces list of authors for each paper
    RCRs = publications['RCR'] #produce list of RCRs for each paper
    RCR_list = [[RCR] for RCR in RCRs] # produce nested list of RCRs 
    
    ###Branch if code is run for first and last authors
    
    cleaned_author_lists = []
    
    if x in ['Y', 'y']:
        for author_list in author_lists:
            temp = []
            if len(author_list) > 1:
                authors.append(author_list[0])
                authors.append(author_list[-1])
                temp.append(author_list[0])
                temp.append(author_list[-1])
                number_authors.append(2)
            else:
                authors.append(author_list[0])
                temp.append(author_list[0])
                number_authors.append(1)    
            cleaned_author_lists.append(temp)
        author_lists = cleaned_author_lists
        for i in range(len(RCR_list)): 
            l.append(RCR_list[i]*number_authors[i]) #create list of no. authors per paper * RCR for the paper
            author_RCRs = [RCR for RCRs in l for RCR in RCRs] # flatten list of lists
            
        return (authors, author_RCRs, author_lists)
    
    ###Branch if code is run for all authors 
    
    else: 
        authors = [authors for author_list in author_lists for authors in author_list] #produces list of indivudal authors
        author_lists = publications['Authors'].str.split(", ") #produces list of authors for each paper
        for author_list in author_lists: #produce list of number of authors on each paper 
            number_authors.append(len(author_list))
   
        for i in range(len(RCR_list)): 
            l.append(RCR_list[i]*number_authors[i]) #create list of no. authors per paper * RCR for the paper
            author_RCRs = [RCR for RCRs in l for RCR in RCRs] # flatten list of lists
        
        return (authors, author_RCRs, author_lists)
    
def run_programme(directory, file_name):
    
    x = message()
    publications = load_file(directory, file_name)
    (authors, author_RCRs, author_lists) = generate_data_structures(publications, x)
    return (authors, author_RCRs, author_lists)
             
