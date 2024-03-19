# import packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests

# titles
st.title("Customize Your Smoothie!")
st.write("Choose the fruits you want in your custom Smoothie!")

# name an order
name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:', name_on_order)

# load smoothies data
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'), col('SEARCH_ON'))
pd_df = my_dataframe.to_pandas()

# select ingredients and load them to the order table
ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:'
    , my_dataframe
    , max_selections = 5
)

if ingredients_list:
    ingredients_string = ''
    
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

        search_on = pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        st.write('The search value for ', fruit_chosen, 'is', search_on, '.')
        
        st.subheader(fruit_chosen + ' Nutrition Information')
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + search_on)
        fv_df = st.dataframe(data=fruityvice_response.json(), use_container_width=True) 

    my_insert_stmt = """INSERT INTO SMOOTHIES.PUBLIC.ORDERS(ingredients, name_on_order) 
        VALUES('""" + ingredients_string + """','""" + name_on_order + """')"""

    time_to_insert = st.button('Submit Order')
    
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")

# =========================== for skill sheet =======================================
# # import packages
# import streamlit as st
# from snowflake.snowpark.functions import col

# # titles
# st.title("Order products")
# st.write("Choose the products you want!")

# # name an order
# name_on_order = st.text_input('Name:')
# st.write('The name on your order will be:', name_on_order)

# # load product data
# cnx = st.connection("snowflake")
# session = cnx.session()
# my_dataframe = session.table("SHOHIN.PUBLIC.PRODUCT_OPTIONS").select(col('NAME'))

# # select products and load them to the order table
# product_list = st.multiselect(
#     'Choose products:'
#     , my_dataframe
# )

# if product_list:
#     product_string = ''

#     for product_chosen in product_list:
#         product_string += product_chosen + '/ '

#     my_insert_stmt = """INSERT INTO SHOHIN.PUBLIC.ORDERS(PRODUCTS, NAME_ON_ORDER) 
#         VALUES('""" + product_string + """','""" + name_on_order + """')"""

#     time_to_insert = st.button('Submit Order')
    
#     if time_to_insert:
#         session.sql(my_insert_stmt).collect()
#         st.success('Your products are ordered, ' + name_on_order + '!', icon="✅")
