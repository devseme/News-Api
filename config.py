import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'

    SOURCE_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    NEWS_API_KEY = '48b8d49793c8496288a3e67219f8a3a5'
    # NEWS_API_KEY = os.environ.get('NEWS_API_KEY')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production' :ProdConfig
}