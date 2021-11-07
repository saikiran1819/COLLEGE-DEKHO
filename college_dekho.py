###   COLLEGE DEKHO.com   ###
import os,json
from sys import maxsize
from bs4 import BeautifulSoup
import requests
url=requests.get("https://www.collegedekho.com/btech-mechanical_engineering-colleges-in-india/")
soup=BeautifulSoup(url.text,"html.parser")
trs=soup.find("div",class_="middle-container").find_all("div",class_="box")

colleges_list_details=[]
for tr in trs:
    ### COLLEGE LINK
    c_link="https://www.collegedekho.com/"+tr.find('a').get('href')
    c_req=requests.get(c_link)
    c_soup=BeautifulSoup(c_req.text,"html.parser")

    ### COLLEGE NAME
    name=c_soup.find("div",class_="collegeDesc").h1
    c_name=name.text
    
    ### COLLEGE TYPE
    type=c_soup.find('td',class_="data").text

    ### COLLEGE APPROVED BY,LOCATION
    spans=c_soup.find("div",class_="subDesc").find_all('span')
    c=0
    for s in spans:
        if c==1:
            c_app=s.text
        else:
            c_loc=s.text
        c+=1

    ### COLLEGE FACILITIES
    faci=c_soup.find(class_="block facilitiesBlock").find(class_="box").find_all(class_="title")
    faci_l=[]
    for f in faci:
        faci_l.append(f.text)
    
    ### COLLEGE CONTACT DETAILS
    add=c_soup.find('div',class_="collegeAddress").ul
    li=add.find_all('li')
    contact={}
    for a in li:
        b=a.text.rsplit(":")
        c=b[-1].strip('\n').strip()
        contact[b[0]]=c

    ### STORING IN A DICTIONARY
    dict1={"college_name":c_name,"type":type,"approved_by":c_app,"loation":c_loc,"facilities":faci_l,"contact_details":contact,"college_link":c_link}
    
    ### cCOLLEGE DETAILS APPEND IN A LIST
    colleges_list_details.append(dict1)

if os.path.exists("/home/navgurukul/Desktop/6WEBS/college_details.json"):
    print('file exists')
else:
    with open("/home/navgurukul/Desktop/6WEBS/college_details.json",'w') as file:
        json.dump(colleges_list_details,file,indent=3)
        file.close()