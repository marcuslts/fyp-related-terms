# Semantics
from sentence_transformers import SentenceTransformer, util
import numpy as np

# Cosine Similarity
def cosine_similarity_score(input_abstract, links_abstract):
    # Calculate text similarity between abstract of input and links
    model = SentenceTransformer('stsb-roberta-large')
    abstract_similarity = []
    embedding_input = model.encode(input_abstract, convert_to_tensor = True)
    for abstract in links_abstract:
        # Encode abstracts to get embedding
        embedding_link = model.encode(abstract, convert_to_tensor = True)
        # Compute similarity score between abstract of input and that of the links using cosine similarity
        cosine_similarity_score = util.pytorch_cos_sim(embedding_input, embedding_link)
        abstract_similarity.append(cosine_similarity_score.item())
    # Return list of scores
    return abstract_similarity

# Jaccard Similarity
def jaccard_similarity_score(input_abstract, links_abstract):
    # Calculate text similarity between abstract of input and links
    abstract_similarity = []
    # Convert input abstract to set
    input_abs = set(input_abstract)
    for abstract in links_abstract:
        # Convert link abstract to set
        link_abs = set(abstract)
        # Calculate jaccard score which is intersection of set / union of set 
        score = float(len(input_abs.intersection(link_abs)) / len(input_abs.union(link_abs)))
        abstract_similarity.append(score)
    # Return list of scores
    return abstract_similarity

# Get relevant terms based on score
def get_relevant_terms(list_of_similarity_scores, links):
    relevant = []
    # Loop through list to look for scores above 0.5
    for index,score in enumerate(list_of_similarity_scores):
        # If score is more than or equal to 0.5, append to relevant list to be returned
        if score >= 0.5:
            relevant.append(links[index])
    return relevant

# Calculate accuracy score based on lists
def accuracy_score(input_list, conceptnet_list):
    input_list = [x.lower() for x in input_list]
    conceptnet_list = [x.lower() for x in conceptnet_list]
    return sum (1 for x, y in zip(input_list, conceptnet_list) if x == y) / float(len(conceptnet_list))