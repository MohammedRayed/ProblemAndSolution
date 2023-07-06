# Reference: https://docs.python.org/3/library/webbrowser.html
# 
# Mohammed Rayed

# This import is used to open web browsers and can open the default web browser.
import webbrowser

# Google Search function
def Google_Search(query):

    # Replace spaces (' ') with '+' for the URL extention for google
    query = query.replace(' ', '+')

    # Creates the URL for a google search of the specific toping and uses the query to get rid of any spaces
    url = f"https://www.google.com/search?q={query}"

    # This is used to open the default web browser and inputs the url into the address box
    webbrowser.open(url)

# Prompt the user to enter a topic
topic = input("Enter a topic to search on Google: ")

# This is used use the Google_Search function above
Google_Search(topic)