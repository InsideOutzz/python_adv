from bs4 import BeautifulSoup

#html content#
html_content = ("""
    <html>
        <head>
        <title> hi hello </title>
        </head>
        
        <body>
        <h1> Welcome to Beautiful Soup!!! </h1>
        <p class="intro"> Its very beautiful soup for web scraping</p>
        
        <div id="content">
        <p>Some random links:</p>
        <a>Link1</a>
        <a>Link2</a>
        <a>Link3</a>
        </div>
    </body>
 </html>
""")

soup = BeautifulSoup(html_content,"html.parser")

print("title of the pages:",soup.title.text)
intro_text = soup.find("p", class_='intro').text
print(intro_text)



div_contents = soup.find("div",id="content").text
links = div_contents.find_all("a")

print(links)