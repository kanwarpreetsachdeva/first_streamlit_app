import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text(' 🥣 Imega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index) , ['Avocado', 'Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page
streamlit.dataframe(fruit_to_show)

#New Section to display FruityVice response
streamlit.header('FruityVice Fruit Advice!')
# Ask the user to enter a fruit choice, Default is Kiwi
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#Print the user entered fruit choice on the screen
streamlit.write('The user entered the following fruit chooce', fruit_choice)


import requests
# Call the fruitvice API for the fruit choice entered by the user
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Normalize the json format in dataframe with keys as columns and values as rows
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Print the normalized json data in dataframe on the screen as a table
streamlit.dataframe(fruityvice_normalized)
