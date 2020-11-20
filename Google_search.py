from googlesearch import search
search_q=input("Enter whatever you want to search")
for z in search(search_q, tld="co.in", stop=2):
    print(z)