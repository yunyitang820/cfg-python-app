# Option [2] 
# Project Brief: Search
# In this project you'll create a program to search for recipes.txt based on an ingredient. The standard
# project uses the Edamam Recipe API, but can be changed to use a different API after completing
# the required tasks.
# You will not need any additional knowledge beyond what is covered in this course to complete this
# project.

# Setup
# To use the Edamam API you will need to register for an account. In your Edamam account
# dashboard you can find an Application ID and Application Key, which you will need to make
# requests to the API.
# To make a request to the Edamam API use the following URL:
# https://api.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_APP_KEY}
# For example, if the App ID and App Key for me account were “ch37j44” and “a58hia” I wanted to
# search for “cheese”, the url would look like this:
# https://api.edamam.com/search?q=cheese&app_id=ch37j44&app_key=a58hia

# Required Tasks 
# These are the required tasks for this project. You should aim to complete these tasks before
# adding your own ideas to the project.
# 1. Read the Edamam API documentation ★
# https://developer.edamam.com/edamam-docs-recipe-api
# 2. Ask the user to enter an ingredient that they want to search for
# 3. Create a function that makes a request to the Edamam API with the required ingredient as
# part of the search query (also included your Application ID and Application Key
# 4. Get the returned recipes.txt from the API response
# 5. Display the recipes.txt for each search result

# Ideas for Extending the Project
# Here are a few ideas for extending the project beyond the required tasks. These ideas are just
# suggestions, feel free to come up with your own ideas and extend the program however you want.
# ● Save the results to a file
# ● Order the results by weight or another piece of data
# ● Ask the user additional questions to decide which recipe they should choose
# ● Cross-reference the ingredient against the Edamam nutrition analysis API
# ● Use a different searchable API (suggestions in useful resources)

# Useful Resources
# API for Anime and Manga
# ● Homepage ★ jikan.moe/
# ● Documentation ★ jikan.docs.apiary.io
# ● Example search ★ https://api.jikan.moe/v3/search/anime?q=Sailor%20Moon
# Spotify API (can be very difficult to use as it requires a much more complicated setup process)
# ● Official Documentation ★ https://developer.spotify.com/documentation/web-api/
# ● Python library for Spotify API ★ https://spotipy.readthedocs.io/en/latest/
# Twitter API (can be very difficult to use as it requires a more complicated setup process)
# ● Official Documentation ★ https://developer.twitter.com/en/docs.html
# ● Python library for Twitter API ★ http://docs.tweepy.org/en/v3.5.0/api.html

# Example Project Code
# In this section you will find some example code to complete the required tasks. You can use this
# code for guidance if you are finding it difficult to complete the required tasks for this project.

import requests

def recipe_search(ingredient):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = '7ae3a3e9'
    app_key = '62aa8e5382f9b077225d833f60da616a'
    recipe_result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )
    data = recipe_result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')

    recipe_result = recipe_search(ingredient)

    f = open("recipes.txt", "w")

    for result in recipe_result:
        recipe = result['recipe']
        f.write(recipe['label'] + ':' + '\n')
        f.write(recipe['url'] + '\n')
        print(recipe['label'] + ':')
        print(recipe['url'])
        for ingrdt in recipe['ingredientLines']:
            f.write('* ' + ingrdt + '\n')
            print('* ' + ingrdt)
        f.write('\n')
        print()

    f.close()

run()



# def nutrition_analysis(body):
#     # Register to get an APP ID and key https://developer.edamam.com/
#     app_id = '04b19de6'
#     app_key = '6fe105bc8843ae297bc0ed45f5b41ce0'
#     nutrition_result = requests.get(
#     'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(body, app_id, app_key)
#     )
#     data = nutrition_result.json()
#     return data['hits']