# Website link : https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY

import requests
from bs4 import BeautifulSoup
import pandas as pd
Name=[]
Price=[]
Description=[]
Reviews=[]
for j in range(1,11):
    url="https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off="+str(j)
    # Making a GET request
    r = requests.get(url)
    
    # check status code for response received
    #print(r)
    
    # Parsing the HTML
    soup = BeautifulSoup(r.text, 'lxml')
    #print(soup)
    #creating object only box containing list of products 
    np=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    name= np.find_all("div", class_="_4rR01T")
    for i in name:
        name= i.text
        Name.append(name)

    price= np.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in price:
        price= i.text
        Price.append(price)
   
    description= np.find_all("ul", class_="_1xgFaf")
    for i in description:
        description= i.text
        Description.append(description)
   
    reviews= np.find_all("div", class_="_3LWZlK")
    for i in reviews:
        reviews= i.text
        Reviews.append(reviews)
a=len(Name)
b=len(Price)
c=len(Description)
d=len(Reviews)
df= pd.DataFrame({"Name":Name, "Price":Price, "Description":Description, "Reviews":Reviews  })
if (a==b==c==d):
    print("hi")
    df.to_csv("flipKa_Scraping.csv")