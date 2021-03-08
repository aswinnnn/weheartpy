## **weheartit**
**A fast, reliable API wrapper for weheartit.com**

# Description
weheartit (named after the site itself, [weheartit](https://weheartit.com))
is a fast, **usable** API wrapper for weheartit.com

[We Heart It](https://weheartit.com) does not have an API. So i make use of `BeautifulSoup`
and `requests` to do my job. The speed is optimal, but if you want
as asynchronous or faster module, just let me know.

# requirements
there are only two requirements for this module:
* `beautifulsoup4`
* `requests`

you can easily install these packages using [pip](https://pypi.org)

# functions 
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

* returns - Image Links[[List](https://docs.python.org/3/library/stdtypes.html#list)], 
A`NoContentFound` error if it couldn't find any results. 

# collections

```python
collections = whi.collections("cute") 
# returns a List of collection links
for collection in collections:
    print(collection) 
```
* parameters - `query` aka the search term
* returns - A python [List](https://docs.python.org/3/library/stdtypes.html#list) 
of [collection](https://weheartit.com/aargauu/collections/180895449-?usr=64895904) links
A`NoContentFound` error if it couldn't find any results. 

# users

```python
users = whi.users("someusername") 
# returns a list of all the accounts that possibly match with the username given. 
```
* parameters - `username` the username of the person you're searching for. 
* returns - A [List](https://docs.python.org/3/library/stdtypes.html#list) 
of all possible accounts matching the username. 
 
