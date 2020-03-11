# Task

# You are given an HTML code snippet of  lines.
# Your task is to print start tags, end tags and empty tags separately.

# Format your results in the following way:

# Start : Tag1
# End   : Tag1
# Start : Tag2
# -> Attribute2[0] > Attribute_value2[0]
# -> Attribute2[1] > Attribute_value2[1]
# -> Attribute2[2] > Attribute_value2[2]
# Start : Tag3
# -> Attribute3[0] > None
# Empty : Tag4
# -> Attribute4[0] > Attribute_value4[0]
# End   : Tag3
# End   : Tag2
# Here, the -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
# The > symbol acts as a separator of the attribute and the attribute value.

# If an HTML tag has no attribute then simply print the name of the tag.
# If an attribute has no attribute value then simply print the name of the attribute value as None.

# Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->).Comments can be multiline as well.

# Input Format

# The first line contains integer , the number of lines in a HTML code snippet.
# The next  lines contain HTML code.

# Output Format

# Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.

# Use proper formatting as explained in the problem statement.

# Sample Input

# 2
# <html><head><title>HTML Parser - I</title></head>
# <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
# Sample Output

# Start : html
# Start : head
# Start : title
# End   : title
# End   : head
# Start : body
# -> data-modal-target > None
# -> class > 1
# Start : h1
# End   : h1
# Empty : br
# End   : body
# End   : html

from html.parser import HTMLParser
import re

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Found a start tag  :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
    def handle_endtag(self, tag):
        print("Found an end tag   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Found an empty tag :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

html = ''

for _ in range(int(input())):
    html += input()

html = re.sub("(<!--.*?-->)", "", html, flags=re.DOTALL)

parser.feed(html)