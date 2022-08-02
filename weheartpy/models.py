# The objects through which the results will be returned.
import requests
from bs4 import BeautifulSoup as bs
from pathlib import Path

class Entry():
    '''
    Base class of a weheartit.com "post" or entry, as they like to call it.

    - attributes:
    - - id: `int` : entry id
    - - username: `str`: username of creator of the post.
    - - url: `str`: url of the post.
    - - image: `str`: a `.jpg` link to the image of the post.

    this class is not meant to be modified or instantiated by you, rather the API.
    you will be utilizing this object to deal with the results you get from `popular()` or `search_entries()`
    '''

    def __init__(self, id: int, username: str,entry: str, image: str, title: str=None) -> None:
        self.id = id
        self.username = username
        
        self.url = "https://weheartit.com" + entry
        self.image = image
        self.title = title

    def __repr__(self) -> str:
        return f"Entry(id={self.id}, username={self.username}, url={self.url}, image={self.image}, title={self.title})"


    def __eq__(self, __o: object) -> bool:
        return self.url == __o.url

    def __ne__(self, __o: object) -> bool:
        return self.url != __o.url

    def save(self, fp) -> None:
        img = requests.get(self.image)
        with open(Path(fp), "x") as f:
            f.write(img.content)




class Collection():
    '''
    The base `Collection` object through which you can access collections
    - attributes
    - - username: `str`: username of the collection creator
    - - link: `str`: link to the collection
    - - title: `str`: title of the collection

    - methods
    - - `get_full_collection`: returns the `Collection` object with (first page) images inside the collection and its description.
    '''
    def __init__(self, username: str, title: str, link: str) -> None:

        self.username = username
        self.title = title
        self.link = link
        self.description = None
        self.images = None

    
    def __repr__(self) -> str:
        return f"Collection(username={self.username}, title={self.title}, link={self.link}), description={self.description}, images={self.images}"


    def __eq__(self, __o: object) -> bool:
        return self.link.casefold() == __o.link.casefold()

    def __ne__(self, __o: object) -> bool:
        return self.link.casefold() != __o.link.casefold()

    def get_full_collection(self):
        '''
        return the `Collection` with the (first page) images inside and its description.
        ```
        cocs = whi.search_collections("egirl")
        for collection in cocs:
            print(collection.description, collection.images)
        ```
        '''
        res = requests.get(self.link)
        res = bs(res.text, features="lxml")
        desc = res.find_all('p', {'class': 'text-gray'})
        desc = "".join([d.text for d in desc])
        
        entries = []
        entrier = res.find_all('a', {'class': 'js-entry-detail-link js-blc js-blc-t-entry'})

        for e in entrier:
            entries.append("https://data.whicdn.com" + (e['href']).replace("entry", "images") + "/original.jpg")

        self.images = entries
        self.description = desc
        return self

    def save(self, fp) -> None:
        for img in self.images:
            img = requests.get(img)
            with open(Path(fp), "x") as f:
                f.write(img.content)

class User():
    '''
    Base class for one weheartit user.

    - attributes
    - - username: `str`: username of the user.
    - - name: `str`: name of the user.
    - - avatar: link to the avatar of the user.
    '''
    def __init__(self, username: str, name: str, avatar: str) -> None:
        self.username = username
        self.name = name
        self.avatar = avatar

    def __repr__(self) -> str:
        return f"User(username={self.username}, name={self.name}, avatar={self.avatar})"


    def __eq__(self, __o: object) -> bool:
        return self.username.casefold() == __o.username.casefold()

    def __ne__(self, __o: object) -> bool:
        return self.username.casefold() != __o.username.casefold()



        

        






    



