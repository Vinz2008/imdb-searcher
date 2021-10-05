import imdb
ia = imdb.IMDb()
name = input("What is the name of the film that you search ? ")
search = ia.search_movie(name)
id = search[0].movieID
name_found = search[0]
def count_characters_in_string(input_string):
    letter_count = 0

    for char in input_string:
        if char.isalpha():
            letter_count += 1
count_characters_in_string(id)
length_name = count_characters_in_string(name_found)
length_id = count_characters_in_string(id)
length_movie_character_line = 23 + int(length_name)
length_id_character_line = 21 + int(length_id)
if length_movie_character_line < length_id_character_line:
    movie_line_longer_id_line = True

else:
    movie_line_longer_id_line = False

print("--------------------------------------------------------")
print("| Name of the movie: " , name_found," |")
print("| Id of the movie: ", id," |")

