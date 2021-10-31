from flask import render_template
from app import app
from .request import get_articles, get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

        # Getting popular source
    popular_sources = get_sources()
    technology_sources = get_sources()
    business_sources = get_sources()
    sports_sources = get_sources()
    
    title = 'Home - Welcome to The best Sources Review Website Online'
    
    return render_template('index.html', title = title,popular = popular_sources,technology = technology_sources,business = business_sources,sports = sports_sources)

@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    View source page function that returns the sources details page and its data
    '''
    return render_template('source.html',id = source_id) 

@app.route('/articles/<source_id>')
def articles(source_id) :

    myArticles =  get_articles('source_id')  


    return render_template('articles.html',myArticles = articles ) 

    