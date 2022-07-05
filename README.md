# **weheartit**

**A fast, reliable API wrapper for WeHeartIt.**

## This repository will be going through breaking changes in the following weeks. The readme will be updated constantly and a documentation will be introduuced.

![weheartit](https://cdn.discordapp.com/attachments/672436233229828108/818444209291657226/images_1.png) 

# Description
weheartit (named after the site itself, [weheartit](https://weheartit.com))
is a fast, **usable** API wrapper for weheartit.com

[We Heart It](https://weheartit.com) does not have an API. So i make use of `BeautifulSoup`
and `requests` to do my job. The speed is optimal, but if you want
an asynchronous or faster module, just let me know.


# requirements
there are only two requirements for this module:
* `beautifulsoup4`
* `requests`

you can easily install these packages using [pip](https://pypi.org)

# installation

```
pip install git+https://github.com/aswinnnn/weheartit.git

```
since twine is being an ass to me, this is the way supported
for now. Let me know if this doesn't work

# usage
**with weheartit, you can search and retrive:**
* posts
* collections
* users
* popular posts

I'm adding more functionalities and utilities later on, 
but this is all we got for now. 


# posts

this shows the most basic way you can utilize weheartit
```python
from weheartit import whi
# import the module

posts = whi.posts("animals", sort="popular") 
# This returns a list of images (links) 
for post in post:
    print(post) 
```
* parameters - `query` - which is your search query, 
`sort` - sort has two options, `recent` and `popular`

* returns - Image Links[[List](https://docs.python.org/3/library/stdtypes.html#list)], A`NoContentFound` error if it couldn't find any results. 


# collections

```python
collections = whi.collections("cute") 
# returns a List of collection links
for collection in collections:
    print(collection) 
```
* parameters - `query` aka the search term
* returns - A python [List](https://docs.python.org/3/library/stdtypes.html#list) 
of [collection](https://weheartit.com/aargauu/collections/180895449-?usr=64895904) links, A`NoContentFound` error if it couldn't find any results. 


# users

```python
users = whi.users("someusername") 
# returns a list of all the accounts that possibly match with the username given. 
```
* parameters - `username` the username of the person you're searching for. 
* returns - A [List](https://docs.python.org/3/library/stdtypes.html#list) 
of all possible accounts matching the username.And of course a `NoContentFound` error if it couldn't find any results. 


# popular

```python
popularposts = whi.popular() 
# returns a list of all the popular images. 
```
* parameters - none, because it retrives the popular images
right from the homepage. 

* returns - A [List](https://docs.python.org/3/library/stdtypes.html#list) of the popular images. 

# About

- more utilities might come later, not sure
- feel free to fork, pull, and open issues! 
- I'm sorry if the code is a little shabby, this is my first time writing a package

 
