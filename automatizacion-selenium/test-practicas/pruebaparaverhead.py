import requests

#the required first parameter of the 'head' method is the 'url':
x = requests.head('https://www.w3schools.com/python/demopage.php')

#print the response headers (the HTTP headers of the requested file):
print(x.status_code)
