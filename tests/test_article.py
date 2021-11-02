import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article =Article ('bbc-sport','BBC Sport','Pakistan into T20 World Cup semi-finals','https://www.bbc.co.uk/sport/cricket/59137683','https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/14D5D/production/_121314358_rizawan_getty.jpg',' 2021-11-02T17:52:30.3744651Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_source.id,'bbc-sport')
        self.assertEqual(self.new_source.author,'BBC Sport')
        self.assertEqual(self.new_source.title,'Pakistan into T20 World Cup semi-finals')
        self.assertEqual(self.new_source.url,'https://www.bbc.co.uk/sport/cricket/59137683')
        self.assertEqual(self.new_source.urlToImage,'https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/14D5D/production/_121314358_rizawan_getty.jpg')
        self.assertEqual(self.new_source.publishedAt,' 2021-11-02T17:52:30.3744651Z')
        