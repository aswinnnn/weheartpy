=============================================
              **Introduction**
=============================================

Let's get to know weheartpy a bit before you start fully utilizing its features!


Description
-------------------
weheartpy is an unofficial API client for `weheartit`_ (https://weheartit.com)

`weheartit`_ does not have an API. (`or, at least not one for the public according to this article`_). So I have to make use of ``BeautifulSoup``
and ``requests`` to do my job. The speed is optimal, it has a limitation on number of results you can retreive through one search but its functional.

.. _weheartit: `https://weheartit.com`

.. _link: `weheartit`_

.. _or, at least not one for the public according to this article: `https://jordan-wright.com/blog/2014/10/12/reverse-engineering-the-we-heart-it-api/`

.. _articlelink: `or, at least not one for the public according to this article`_

-------------------


Disclaimer
---------------------

- Since this makeshift API client relies on the websites elements to remain unchanged, expect this package to break easily someday. ``useragent`` will be supported soon.
- This package, code or software is made for educational purposes and does not intend to break any ToS of weheartit.com. The creator/maintainer of this package will not be responsible for any actions done using the code. Use with your own caution and volition.



Requirements
------------------

* requires ``Python 10.4`` or above.
* read the `requirements.txt`_

you can easily install the packages using `pip`_.

.. _requirements.txt: `https://github.com/aswinnnn/weheartpy/blob/1940863576d61a71e25f6ab4246e81f898376dcd/requirements.txt`

.. _reqs: `requirements.txt`_

.. _pip: `https://pypi.org`
.. _piplink: `pip`_


---------------

Installation
-----------------------
Any of the two methods are supposed to work but the first one is preferred.

.. code-block:: python

    pip install weheartpy


or 

.. code-block:: python
    
    pip install git+https://github.com/aswinnnn/weheartit.git


----------

Features
------------------------

*With weheartpy, you can search for:*

+ posts aka entries
+ collections (including images inside them)
+ users
+ popular entries

For more functionalities inside them, check out the API reference.


----------------

**Quickstart**
------------------------
This is the most basic usage of the weheartpy module.

.. code-block:: python

    # import the main class
    
    from weheartpy import WeHeartIt
    
    whi = WeHeartIt() # create an instance of WeHeartIt
    
    entries = whi.popular() # returns a list of recent popular images from homepage.
    
    for entry in entries:
        print(entry.id)
        print(entry.username)
        print(entry.image)
        print(entry.url)



---------------------

Posts / Entries
------------------------
Search for entries.

.. code-block:: python
    
    entries = whi.search_entries("mean girls", sort="most_popular")
    
    # returns a list of entries relevant to your query.
    
    for entry in entries:
    print(entry.username, entry.image, entry.url)

* parameters - `query` - your search query

* returns - List[Entry] a list of `Entry` objects which help you access the entries easier. 
  
* errors - `ConnectionError`


-------------------------


Collections
----------------------

.. code-block:: python
    
    # return a list of `Collection` objects resulting from the query.
    
    from weheartpy import WeHeartIt
    
    whi = WeHeartIt()
    
    cocs = whi.search_collections("anime pfp")
    
    for c in cocs:
        print(c.title, c.link)
        collection = c.get_full_collection()
        print(collection.images, collection.description)

* parameters - `query` aka the search term
  
* returns - List[Collection] Check out the documentation to see what else you can do with `Collection` objects.
  
* errors - `NoCollectionsFound` 






