from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_articles, get_sources
from ..models import Source

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

        # Getting popular source
    technology_sources = get_sources('technology')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    
    title = 'Home - Welcome to The best Sources Review Website Online'
    
    return render_template('index.html', title = title,technology = technology_sources,business = business_sources,sports = sports_sources)

@main.route('/source/<int:source_id>')
def source(source_id):

    '''
    View source page function that returns the sources details page and its data
    '''
    return render_template('source.html',id = source_id) 

@main.route('/articles/<id>')
def articles(id) :
    '''
    View articles page showing articles  and its data
    '''

    articles =  get_articles(id)  
    print(articles)
    
    return render_template('articles.html',articles = articles ) 

    