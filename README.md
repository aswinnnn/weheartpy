[![PyPI version](https://badge.fury.io/py/weheartpy.svg)](https://badge.fury.io/py/weheartpy) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub issues](https://img.shields.io/github/issues/aswinnnn/weheartpy.svg)](https://GitHub.com/aswinnnn/weheartpy/issues/) [![Downloads](https://static.pepy.tech/personalized-badge/weheartpy?period=total&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/weheartpy) [![Top Language](https://img.shields.io/github/languages/top/aswinnnn/weheartpy)](https://img.shields.io/github/languages/top/aswinnnn/weheartpy) [![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
# **weheartpy**

**A fast, reliable API client for WeHeartIt.**

![weheartpy](https://media.discordapp.net/attachments/1002212458502557718/1003290415329443850/PicsArt_07-31-06.47.36.jpg) 

# Description
weheartpy is an unofficial API client for [weheartit](https://weheartit.com)

[WeHeartIt](https://weheartit.com) does not have an API. So I have to make use of `BeautifulSoup`
and `requests` to do my job. The speed is optimal, it has a limitation on number of results you can retreive through one search but its functional.


# Requirements
* requires `Python 10.*` or above.
* read the requirements [here](requirements.txt)

you can easily install the packages using [pip](https://pypi.org)

# Installation
```
pip install weheartpy
```
or
```
pip install git+https://github.com/aswinnnn/weheartpy.git

```

# Features
with weheartpy, you can search for:
- posts aka entries
- collections (including images inside them)
- users
- popular entries

I'm adding more functionalities and utilities later on, 
but this is all we got for now. 

# Usage
this is the most basic usage of the weheartpy module.

```python
# import the main class
from weheartpy import WeHeartIt

whi = WeHeartIt() # create an instance of WeHeartIt

entries = whi.popular() # returns a list of recent popular images from homepage.

for entry in entries:
	print(entry.image, entry.views, entry.creator.username) # view the entry's contents
	print(entry.hearts, entry.title)

	entry.save("\images\cool_pic_from_weheartit.jpeg") # save the image from the post locally.

```
* parameters - None

* returns - List[[Entry](weheartpy/models.py)] a list of `Entry` objects which help you access the entries easier. 
* errors - `ConnectionError`

# Posts / Entries
search for entries.
```python
entries = whi.search_entries("mean girls", sort="most_popular")
# returns a list of entries relevant to your query.

for entry in entries:
	print(entry.username, entry.image, entry.url)
```
* parameters - `query` - your search query

* returns - List[[Entry](weheartpy/models.py)] a list of `Entry` objects which help you access the entries easier. 
* errors - `ConnectionError`


# Collections

```python
# return a list of `Collection` objects resulting from the query.

from weheartpy import WeHeartIt

whi = WeHeartIt()

cocs = whi.search_collections("anime pfp")
for c in cocs:
    print(c.title, c.link)
    collection = c.get_full_collection()
    print(collection.images, collection.description)

	# save the images from a collection to a folder:
	collection.save("\collection\")
	# images will be saved as "collection0.jpeg", "collection1.jpeg", etc.
	
```
* parameters - `query` aka the search term
* returns - List[[Collection](weheartpy/models.py)] Check out the documentation to see what else you can do with `Collection` objects.
* errors - `NoCollectionsFound` 

# Documentation
* check out the [documentation](https://aswinnnn.github.io/weheartpy/) for more usages. 
* If you'd like to add something or fix mistakes, feel free to open an issue or a pull request.
  
# Updates
- `v0.2.3` - using `user-agent` has been made default. Fixed major bug in `search_entries` so you might wanna update to this version to use that correctly.
- `v0.2.2` - Big update, the library uses weheartit's natural API to bring `Entry` data.
-  - this features a whole new ton of information you can use from entries such as a views, hearts, tags, titles and creation dates.
-  - It also includes a `.creator` attribute which is a `User` object of the creator of the post.
-  - If you notice anything slow, its the API calls to weheartit.com. The IO time can be a pain if you have slow internet, nothing I can fix on my side.
- `v0.2.1` - Implement save feature, lets users save images locally.
  
# Disclaimer
- Since this makeshift API client relies on the websites elements to remain unchanged, expect this package to break easily someday. `useragent` will be supported soon.
- This package, code or software is made for educational purposes and does not intend to break any ToS of weheartit.com. The creator/maintainer of this package will not be responsible for any actions done using the code. Use with your own caution and volition.
 
