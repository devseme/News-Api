class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,url,category,language):
        self.id =id
        self.name = name
        self.description = description
        self.url= 'https://abcnews.go.com/'+ url
        self.category= category
        self.language = language

class Article:

    def __init__(self,id, author, title, description, url, urlToImage, publishedAt, content):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content        