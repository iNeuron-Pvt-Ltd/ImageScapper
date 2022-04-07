import os
import time
import requests
import selenium
import time
import io
import streamlit as st
import instagramy
from PIL import Image
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

def app():
    st.header("Welcome to iNeuron scrapper!!")
    platform = st.sidebar.selectbox("Select the platform you want to scrape", ['Instagram', 'Google', 'Baidu'])
    try:
        if platform == 'Instagram':
            user = st.text_input("Enter the instagram id you want to scrape..")

            user = instagramy.InstagramUser(user)

        #     printing the details like followers, following, bio
            st.subheader('Account\'s Details:')
            st.write(f'Is the account verified?', user.is_verified)
            st.write(f'Total followers: {user.number_of_followers}')
            st.write(f'Total followings: {user.number_of_followings}')
            st.write(f'User\'s bio: {user.biography}')
            st.subheader('Post\'s Details:')
        posts = user.posts
        for post in posts:
            st.write(f'No of likes on the post: {post.likes}')
            st.write(f'No of comments on the post {post.comments}')
            st.write(f'Post\'s URL: {post.post_url}')


        if platform == 'Google':
            pass

        if platform == 'Baidu':
            pass
    except Exception as e:
        print(e)




    # # Install driver
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    #
    # # specify search url
    # q = input("Value you want to search")
    # search_url = "https://www.google.com/search?q={q}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"          #the images will be copyright-free images
    # driver.get(search_url.format(q=q))
    #
    # def scroll_to_end(driver):
    #     # scroll to the end of page
    #     driver.execute_script('window.scrollTo(0, document.body.scrillHeight);')
    #     # sleep between interactions
    #     time.sleep(5)
    #
    # # locate the images to be scrapped from the current page
    # imgResults = driver.find_elements(by=By.XPATH, value="//img[contains(@class,'Q4LuWd')]")

app()
