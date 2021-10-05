#import imdb
from imdb import IMDb
ia = IMDb()
#ia = imdb.IMDb()
name = input("What is the name of the film that you search ? ")
search = ia.search_movie(name)
for i in search:
	print(i)
