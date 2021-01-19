import urllib.request
import urllib.response
import lxml.etree
import sys
import json

def lookup(query):
    query = query.replace(" ", "-")
    url = str(getAPIprefix(query) + query)
    with urllib.request.urlopen(url) as test:
        dbpage = test.read()
    tree = lxml.etree.fromstring(dbpage)
    all_results = tree.findall(".//Result")
    all_books, correct_indexes = booklister(tree, all_results)
            
    if len(all_books) == 0:
        query = input("No results, please try again: ")
        return lookup(query)
    elif len(all_books) == 1:
        for i in ["\nOne book found:", all_books[0], "\nDescription: " + tree.find(".//Result[{}]/Description".format(correct_indexes[0])).text, jsondata(tree.find(".//Result[{}]/URI".format(correct_indexes[0])).text)]:
            print(i)
    else:
        pick = bookselector(all_books)
        for i in ["",  all_books[pick], "\nDescription: " + tree.find(".//Result[{}]/Description".format(correct_indexes[pick])).text, jsondata(tree.find(".//Result[{}]/URI".format(correct_indexes[pick])).text)]:
            print[i]

def getAPIprefix(query) -> str:
    """
    Detect functioning DBpedia lookup API
    """
    prefixes = ["https://lookup.dbpedia.org/api/search/PrefixSearch?QueryString=",
                "http://lookup.dbpedia.org/api/search/PrefixSearch?QueryString=",
                "https://lookup.dbpedia.org/api/prefix?query=",
                "http://lookup.dbpedia.org/api/prefix?query=",
                "http://akswnc7.informatik.uni-leipzig.de/lookup/api/search?query="]
    for prefix in prefixes:
        with urllib.request.urlopen(prefix + query) as test:
            if test.status == 200:
                return prefix
    sys.exit("No functioning DBpedia lookup API found!")
    
def booklister(tree, all_results):
    all_books = []
    correct_indexes = []
    allindex = 0
    for i in all_results:
        allindex += 1
        results = tree.findall(".//Result[{}]/Classes/Class/Label".format(allindex))
        for result in results:
            if result.text == "Book":
                bookname = tree.find(".//Result[{}]/Label".format(allindex)).text
                all_books.append(bookname)
                correct_indexes.append(allindex)
    return all_books, correct_indexes

def bookselector(all_books):
    bookindex = 0
    for book in all_books:
        print(str(bookindex + 1) + ". " + all_books[bookindex])
        bookindex += 1
    pickstr = input("\nPlease give the index of the book you want to know more about: ")
    indexlist = []
    for i in range(1, bookindex + 1):
        indexlist.append(str(i))
    while pickstr not in indexlist:
        pickstr = input("\nPlease give a number that's in the list!: ")
    return int(pickstr) - 1

def jsondata(URI):
    data = jsonload(URI)
    #print(data["{}".format(URI)])
    authorlink = data["{}".format(URI)]["http://dbpedia.org/ontology/author"][0]["value"]
    author = jsonload(authorlink)["{}".format(authorlink)]["http://xmlns.com/foaf/0.1/name"][0]["value"]
    for desc in jsonload(authorlink)["{}".format(authorlink)]["http://www.w3.org/2000/01/rdf-schema#comment"]:
        if desc["lang"] == "en":
            bio = desc["value"]
    return "\nAuthor: " + author + " (" + authorlink + ")" + "\nBiography: " + bio

def jsonload(URI):
    jsonURI = URI.replace("resource", "data") + ".json"
    with urllib.request.urlopen(jsonURI) as request:
        return json.loads(request.read().decode())
    
    
    
    