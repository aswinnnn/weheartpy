import requests 
from bs4 import BeautifulSoup as bs

# ErrorClass to raise if no posts/collections/users are found.	
class NoContentFound(Exception):
	pass

# the main class, whi (weheartit)
class whi:
	@staticmethod
	def posts(query=None, sort=None):
		if query == None:
			e = "No query given. Give me something to search for."
			print(e)
			return e
		query = str(query)
		if sort == None:
			sort = "recent"
			
		elif sort == "popular":
			sort = "most_popular"
			
		elif sort == "recent":
			sort = "recent"
			
		url = f"https://weheartit.com/search/entries?query={query}&sort={sort}"
		
		res = requests.get(url)
		if res.status_code != requests.codes.ok:
			print("Something is wrong with weheartit.com. Either its your internet connection or  weheartit's fault.")
			return res.raise_for_status()
		
		soup = bs(res.content, features="html.parser")		
		divs = str(soup.find_all('div', class_='entry grid-item'))
		soup2 = bs(divs, features="html.parser")
		images = soup2.find_all('img')
		links = []
		for image in images:
			if "data.whicdn.com/images/" in str(image):
				links.append(image['src'])
				
		if len(links) == 0:
				raise NoPostsFound("Couldnt find any posts for the search. Try again using different keyworfs maybe?")
				
		
				
		return links
		
	@staticmethod
	def collections(query):
			query = str(query)
			url = f"https://weheartit.com/search/collections?query={query}&sort=most_popular"
			response = requests.get(url)
			if response.status_code != requests.codes.ok:
				print("Something is wrong with weheartit.com. \n Either its your internet connection or  weheartit's fault.")
				return response.raise_for_status()
				
			soup = bs(response.text, features="html.parser")
			atag = soup.find_all('a')
			links = []
			
			for link in atag:
				if "/collections/" in str(link):
					links.append(link['href'])
			
			if len(links) == 0:
				raise NoContentFound("couldnt find anything for the given search query. \n Try another search term?")
			
			return links
			
	@staticmethod
	def users(query):
				query = str(query)
				url = f"https://weheartit.com/search/users?query={query}"
				res = requests.get(url)
				if res.status_code != requests.codes.ok:
					print("Something is wrong with weheartit.com. \n Either its your internet connection or  weheartit's fault.")
					raise res.raise_for_status()
					
				soup = bs(res.text, features="html.parser")
				atags = soup.find_all('a', class_="js-blc js-blc-t-user")
				links = []
				for tag in atags:
					links.append(f"https://weheartit.com{tag['href']}")
					
				if len(links) == 0:
					raise NoContentFound("Looks like we couldnt find anyone with that user or username.")
					
				return links
				
				
	@staticmethod
	def popular():
				res = requests.get("https://weheartit.com")
				if res.status_code != requests.codes.ok:
					print("somethings wrong with weheartit.com")
					raise res.raise_for_status()
					
				soup = bs(res.text, features="html.parser")
				atags = soup.find_all('a')
				links = []
				for tag in atags:
					if "/popular_images/" in str(tag):
						links.append(f"https://weheartit.com{tag['href']}")
						
				if len(links) == 0:
						raise NoContentFound("couldnt find any popular posts. Seems like an error with the website.")
						
				return links
					
					
					

						
				
				
				

				
				
				
			

			
			

			