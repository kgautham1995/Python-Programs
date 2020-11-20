import pyshorteners
myurl=input("Enter your URL")
s_url=pyshorteners.Shortener().tinyurl.short(myurl)
print("shortened URL is",s_url)
