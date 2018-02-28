import media
import fresh_tomatoes


"""
    This module will create an array of details( such as the title, image url
    and youtube url) for each by calling the Movie class in the media.py file.
    It will then create a list of the created movie objects, which will be
    passed back to the open_movies_page function in the fresh_tomatoes.py file.
"""

kung_pow = media.Movie(
        "Kung Pow! Enter the First",
        "https://upload.wikimedia.org/wikipedia/en/5/54/Kungpow.jpg",
        "https://www.youtube.com/watch?v=GXrAYdSeWY8&t=11s")

walle = media.Movie(
        "Wall-E",
        "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
        "https://www.youtube.com/watch?v=9pyBKj5-jVk")

a_million_ways = media.Movie(
        "A Million Ways To Die In The West",
        "https://upload.wikimedia.org/wikipedia/en/2/22/A_Million_Ways_to_Die_in_the_West_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=WhGkcOoTlkQ")

secret_life_pets = media.Movie(
        "Secret Life of Pets",
        "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=UZJVc_JTI_w")

talladega_nights = media.Movie(
        "Talladega Nights: The Ballad of Ricky Bobby",
        "https://upload.wikimedia.org/wikipedia/en/e/e7/Talladega_nights.jpg",
        "https://www.youtube.com/watch?v=-zPcMma_C7A")

other_guys = media.Movie(
        "The Other Guys",
        "https://upload.wikimedia.org/wikipedia/en/6/6b/Other_guys_poster.jpg",
        "https://www.youtube.com/watch?v=D6WOoUG1eNo")

# movies is a list of the movie classes created
movies = [kung_pow, walle, a_million_ways, secret_life_pets, talladega_nights,
          other_guys]

# Call to open_movies_page on fresh_tomatoes.py with movies list
fresh_tomatoes.open_movies_page(movies)
