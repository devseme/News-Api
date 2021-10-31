from app import app
import urllib.request,json
from .articles import Article

from app.source_test import Source
from .models import source

Source = source.Source
# Getting api key
api_key = app.config['SOURCE_API_KEY']


# Getting the source base url
base_url = app.config["SOURCE_API_BASE_URL"]

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey=48b8d49793c8496288a3e67219f8a3a5'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for articles_item in source_list:
        id = articles_item.get('id')
        name = articles_item.get('name')
        description = articles_item.get('description')
        url = articles_item.get('url')
        category = articles_item.get('category')
        language = articles_item.get('language')

        if id:
            source_object = Source(id,name,description,url,category,language)
            source_results.append(source_object)

    return source_results    

def process_articles(articles_list): 


    articles_list = []
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')


        if id:
            articles_object = Article(author,title,description,url,urlToImage,publishedAt,content)
            articles_list.append(articles_object)

    return articles_list

def get_articles(source_id):
    get_sources_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=48b8d49793c8496288a3e67219f8a3a5'.format(source_id)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['articles']:
            source_results_list = get_sources_response['articles']
            source_results = process_articles(source_results_list)


    return source_results





   