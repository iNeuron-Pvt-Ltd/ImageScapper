
import requests
import pandas as pd
import streamlit as st
import instagramy
from PIL import Image
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from bs4 import BeautifulSoup


def app():
    st.header("Welcome to iNeuron scrapper!!")
    platform = st.sidebar.selectbox("Select the platform you want to scrape", ('Instagram', 'Naukari', 'Stack Overflow', 'Baidu'))

# Instagram Scrapper
    try:
        if platform == 'Instagram':
            user = st.text_input("Enter the instagram id you want to scrape..")
            user = instagramy.InstagramUser(user)

            # printing the details like followers, following, bio
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
    except Exception as e:
        return e

    # Naukari Scrapper
    try:
        if platform == 'Naukari':
            job = st.text_input("Enter the job you want to apply for:").replace(' ', '')
            location = st.text_input("Enter the location you want to apply for:").replace(' ', '')
            df = pd.DataFrame(
                columns=['Job Title', 'Job URL', 'Company Title', 'Company URL', 'Ratings', 'Reviews', 'Experience',
                         'Salary', 'Location', 'Job_Post_History'])
            url = f"https://www.naukri.com/{job}-jobs-in-{location}"
            page = requests.get(url)
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            results = soup.find(class_='list')
            job_elems = results.find_all('article', class_="jobTuple bgWhite br4 mb-8")
            for job_elem in job_elems:
                job_URL = job_elem.find('a', class_='title fw500 ellipsis').get('href')  # job listing URL
                job_title = job_elem.find('a', class_='title fw500 ellipsis')  # Opening position title
                company_URL = job_elem.find('a', class_='subTitle ellipsis fleft').get('href')  # company's URL
                company_title = job_elem.find('a', class_='subTitle ellipsis fleft')  # company's title
                rating_span = job_elem.find('span', class_='starRating fleft dot')
                if rating_span is None:  # job ratings
                    continue
                else:
                    Ratings = rating_span.text
                review_span = job_elem.find('a', class_='reviewsCount ml-5 fleft blue-text')

                if review_span is None:  # no of reviews
                    continue
                else:
                    reviews = review_span.text

                Exp = job_elem.find('li', class_='fleft grey-text br2 placeHolderLi experience')  # experience required
                Exp_span = Exp.find('span', class_='ellipsis fleft fs12 lh16')
                if Exp_span is None:
                    continue
                else:
                    Experience = Exp_span.text

                Sal = job_elem.find('li', class_='fleft grey-text br2 placeHolderLi salary')  # offered salary
                Sal_span = Sal.find('span', class_='ellipsis fleft fs12 lh16')
                if Sal_span is None:
                    continue
                else:
                    Salary = Sal_span.text

                Loc = job_elem.find('li', class_='fleft grey-text br2 placeHolderLi location')  # location
                Loc_exp = Loc.find('span', class_='ellipsis fleft fs12 lh16')
                if Loc_exp is None:
                    continue
                else:
                    Location = Loc_exp.text

                Hist = job_elem.find("div", ["type br2 fleft grey", "type br2 fleft green"])  # posted ago
                Post_Hist = Hist.find('span', class_='fleft fw500')
                if Post_Hist is None:
                    continue
                else:
                    Post_History = Post_Hist.text

                # df = df.append(
                #     {'Job Title': job_title, 'Job URL': job_URL, 'Company Title': company_title,
                #      'Company URL': company_URL, 'Ratings': Ratings, 'Reviews': reviews,
                #      'Experience': Experience, 'Salary': Salary, 'Location': Location, 'Post History': Post_History},
                #     ignore_index=True)
                # st.write(df)
                st.write(job_title.text)
                st.write(job_URL)
                st.write(company_title.text)
                st.write(company_URL)
                st.write(Ratings)
                st.write(reviews)
                st.write(Experience)
                st.write(Salary)
                st.write(Location)
                st.write(Post_History)
    except Exception as e:
        return e

    if platform == 'Google':
        st.subheader('hi')


app()
