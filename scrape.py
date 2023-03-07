"""
Python script to extract the images from wordpress single post page and save to disk
Requires pages.txt file containing the list of URL. each URL on single line required.
Author: Prabhat Giri
Author email: viaprabhat@gmail.com
Date: 2023/03/07
"""

# imports all the necessary libraries for the script
import requests
from bs4 import BeautifulSoup
import os

# opens the file containing the URLs. each URL to be on new line. no deliminator needed.
file = open('pages.txt', 'r')

# reads through lines of the file
Lines = file.readlines()
# gets the current working directory
dirname = os.path.dirname(__file__)

# replace the cookie if you need to access private/draft post
# user-agent is required so that the server thinks the request is coming from Chrome and not python bot
header = {  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', 
                                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                                            'cache-control': 'no-cache',
                                            'cookie':'',
                                            'pragma': 'no-cache',
                                            'upgrade-insecure-requests': '1'
                                          }
# loops through each lines of the provided file
for line in Lines:
    # sends request to the page along with header.
    r = requests.get(url = line, headers=header )
    # converts the response into beautiful soup
    soup = BeautifulSoup(r.content, 'html.parser')
    # select the div.blog_single element as the whole post is inside this element
    div = soup.find("div", class_="blog_single")
    #  find all the images inside the blog_single element
    images = div.find_all("img")
    # loops through each image and if they arent a gravatar image proceeds to save them to disk
    for image in images:
        url = image.get('src')
        if "gravatar.com" not in url:
            # create a new folder based on the last part of URL (this breaks in case of draft posts as they use ?p=id as URL)
            save_path = line.split('/')[-2]
            # check of above path exists and if not create a new one
            isExist = os.path.exists(save_path)
            print(save_path)
            if not isExist:
                os.makedirs(save_path)
            # joins the current pwd, folder name and file name into fullName variable
            save_at = os.path.join(dirname, save_path)
            filename = url.split('/')[-1]
            fullName = os.path.join(save_at, filename)
            # using the fullName/path, if the request gets the file writes the file to disk else prints error code to the console
            with open(fullName, 'wb') as handle:
                response = requests.get(url, stream=True, headers=header )
                # check for response. if not of print it
                if not response.ok:
                    print(response)
                # if response if ok, iterates through the content and writes the response to file
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)