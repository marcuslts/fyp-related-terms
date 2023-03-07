import unittest
from query import *
from similarities import *
from conceptnet import *

class TestQuery(unittest.TestCase):

    def test_get_abstract(self):
        test_query = Query('Kiasu')
        test_abstract = test_query.get_abstract()
        self.assertEqual(test_abstract, 'Kiasu (simplified Chinese: 惊输; traditional Chinese: 驚輸; Pe̍h-ōe-jī: kiaⁿ-su) is a Hokkien word that denotes a "grasping, selfish attitude" that arises from fear of missing out.')

    def test_get_links(self):
        test_query = Query('Kiasu')
        test_links = test_query.get_links()
        self.assertEqual(test_links, ['Kiasi', 'The_7_Habits_of_Highly_Effective_People', 'Fear_of_missing_out', 'Culture_of_Singapore', 'Hokkien', 'Singapore', 'Singlish', 'Vernacular_Chinese'])

class TestSimilarities(unittest.TestCase):

    def test_cosine_similarity_score(self):
        result = cosine_similarity_score(['test'], ['test'])
        self.assertEqual(result, [0.9999998211860657])

    def test_jaccard_similarity_score(self):
        result = jaccard_similarity_score(['1'], ['1'])
        self.assertEqual(result, [1])

    def test_get_relevant_terms(self):
        scores = [0.8, 0.3, 0.5, 0.1]
        terms = ['1', '2', '3', '4']
        result = get_relevant_terms(scores, terms)
        self.assertEqual(result, ['1', '3'])

    def test_accuracy_score_same(self):
        list_1 = ['1', '2', '3']
        list_2 = ['1', '2', '3']
        result = accuracy_score(list_1, list_2)
        self.assertEqual(result, 1)

    def test_accuracy_score_zero(self):
        list_1 = ['1', '2', '3']
        list_2 = ['4', '5', '6']
        result = accuracy_score(list_1, list_2)
        self.assertEqual(result, 0)

class TestConceptNet(unittest.TestCase):

    def test_concept_net(self):
        query = "Kiasu"
        result = concept_net(query)
        self.assertEqual(result, ['kiasi', 'competitive', 'kiasu', 'afraid', 'lose_out'])