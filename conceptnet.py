import requests

def concept_net(query):
    related_terms = []
    obj = requests.get('http://api.conceptnet.io/c/en/{}?rel=/r/RelatedTo&limit=1000filter=/c/en'.format(query.lower())).json()
    related = 'RelatedTo'
    for i in obj['edges']:
        # Look for related words in JSON file
        if related in i['@id']:
            # Split string on comma
            split = i['@id'].split(",")
            # Get last related word
            word = split[2]
            # Remove '/c/en/
            word = word.replace('/c/en/', '')
            # Remove '/]' at the back to get word
            word = word.replace('/]', '')
            # Append word to related terms 
            related_terms.append(word)
    return related_terms