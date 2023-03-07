# SPARQL 
import importlib
from query import *
from similarities import *
from conceptnet import *

# Get input
input = input("Query: ")
query = Query(input)

# Get abstract of input
input_abstract = query.get_abstract()
print(input_abstract)

# Get links of input
input_links = query.get_links()
print(input_links)

# Get abstract of links
links_abstract = []
for link in input_links:
    # Set link as input for Query to get abstract
    links_abstract.append(Query(link).get_abstract())
print(links_abstract)

# Calculate cosine score per term based on abstract
cosine_score_list = cosine_similarity_score(input_abstract, links_abstract)
print(cosine_score_list)

# Calculate jaccard score per term based on abstract
jaccard_score_list = jaccard_similarity_score(input_abstract, links_abstract)
print(jaccard_score_list)

# Get relevant terms based on score for both cosine and jaccard lists
cosine_terms = get_relevant_terms(cosine_score_list, input_links)
jaccard_terms = get_relevant_terms(jaccard_score_list, input_links)
print(cosine_terms)
print(jaccard_terms)

# Get relevant terms based on the Concept Net API 
conceptnet_list = concept_net(input)
print(conceptnet_list)

# Compare relevant terms in the cosine and jaccard similarity list to that of the ConceptNet API to get accuracy
cosine_accuracy = accuracy_score(cosine_terms, conceptnet_list)
jaccard_accuracy = accuracy_score(jaccard_terms, conceptnet_list)
print(cosine_accuracy)
print(jaccard_accuracy)

# Print list with higher accuracy
print("Relevant terms:")
# Only print jaccard terms if it has a higher accuracy than that of the cosine terms for terms in the list
if jaccard_accuracy > cosine_accuracy:
    for term in jaccard_terms:
        print(term)
# Print cosine terms if jaccard terms do not have a higher accuracy
else:
    for term in cosine_terms:
        print(term)