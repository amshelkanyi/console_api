'''
API for showing book titles when given the authors name
Im using Goodreads.com to make my requests
An API key is required which i obtained by logging in
Import the xml dom for parsing since the api will respond in xml format
key: zP9LAJl2GjZfNRjS7bKyg
'''

from xml.dom import minidom
import urllib3

#make a request using pool manager
connection = urllib3.PoolManager()

#define a function that takes an authours name
def find_book_by_author(author):

#empty list where books will be stored
    list_books = []

#key is required by the api
    api_key = "zP9LAJl2GjZfNRjS7bKyg"

#replace the spaces between names with %20
    author_name = author.replace(' ', '%20')

#obtain the final url to be requested
    url = "https://www.goodreads.com/search/index.xml?key="+api_key+ "&q=" +author_name

#open a connection to the url
    obj = connection.urlopen('GET', url)

#parse the http response
    parser = minidom.parseString(obj.data)
    titles = parser.getElementsByTagName('title')

#iterate through each one to display one book title at a time
    for title in titles:
#get value of the first tag
        book_title = title.firstChild.nodeValue
#append to empty list
        list_books.append(book_title)
    return list_books


