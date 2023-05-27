
# Website link : https://www.hopkinsmedicine.org/profiles/search?query=

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
Links=[]
Name=[]
Title=[]
Gender=[]
Expertise=[]
ResearchInterests=[]
Phone=[]
Location=[]
Education=[]
for i in range(1,296):
    url="https://www.hopkinsmedicine.org/profiles/search?query=&page="+str(i)
    r= requests.get(url)
    soup= BeautifulSoup(r.text,"lxml")
    #print(r.content)
    #print(soup)
    links=soup.find_all('a', class_="doctorLink heading-chevron")
    for j in links:
        links=j.get('href')
        Links.append(links)

    for k in Links:
        ur='https://www.hopkinsmedicine.org'+k
        p=requests.get(ur)
        sou=BeautifulSoup(p.text,"lxml")
        title=""
        name=sou.find('div', class_="name").find('h1').text
        n=name.split(',')
        Name.append(str(n[0]))
        T=n[1:]
        for i in T:
            title=title+i
        Title.append(title)
        g=sou.find("div",class_="gender")
        if g==None:
            Gender.append("-")
        else:
            gender=g.text
            Gender.append(gender)
        e=sou.find("p", class_="read-more-wrapper")
        if e==None:
            Expertise.append("-")
        else:
            expertise=e.text
            Expertise.append(expertise)
        ResearchInterests.append("-")
        p=sou.find("div", class_="phone")
        if p==None:
           Phone.append("-")
        else:
            phone=p.text
            phone=phone.strip()
            Phone.append(phone) 

        l=sou.find("div",class_="address")
        if l==None:
            Location.append("-")
        else:
            location=l.text
            location=re.sub(' +', '', location)
            location=location.replace("map","")
            Location.append(location)
        ed=sou.find("div",class_="section education")
        if ed==None:
            Education.append("-")
        else:
            education=ed.text
            education=re.sub(' +', '',education)
            education=education.replace("Education","")
            Education.append(education)
ab=len(Name)
print(ab)
bc=len(Title)
print(bc)
cd=len(Gender)
print(cd)
de=len(Expertise)
print(de)
ef=len(ResearchInterests)
print(ef)
fg=len(Phone)
print(fg)
gh=len(Location)
print(gh)
hi=len(Education)
print(hi)
df= pd.DataFrame({"Name":Name, "Title":Title, "Gender":Gender, "Expertise":Expertise, "ResearchInterests":ResearchInterests, "Phone":Phone, "Location":Location, "Education":Education})
df.to_csv("Provider_Details_Python_Task1.csv")
        

        
        




        


        
        


        
    






 