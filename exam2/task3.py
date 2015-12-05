import requests
from lxml import etree

url = "https://twitter.com/googlefacts"
data = requests.get(url).text
#print(data)

parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

tweets = open('twitter.txt', 'w')
for element in tree.iter("p"):
    if 'class' in element.attrib:
        if element.attrib['class'] == "TweetTextSize TweetTextSize--16px js-tweet-text tweet-text":
            tweets.write(element.text)
            tweets.write('\n')

tweets.close()