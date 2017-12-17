from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import urllib.request
import urllib.parse


#let's create a file that we will want later to write parsed data to
filename="NFL_ScrapedData.csv"
f=open(filename,'w')
headers="Name,Team,Pos.,Completions,Targets,Comp%,TDs,Target %\n"
f.write(headers)

my_url="http://www.nflsavant.com/index.php"
netloc = urllib.parse.urlparse(my_url).netloc

req=urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}) #sends GET request to URL
uClient = urllib.request.urlopen(req)
page_html = uClient.read()
uClient.close() #close the connection

#now for the good stuff... let's use BeautifulSoup to parse the webpage
page_soup=soup(page_html,"html.parser") #applying BeautifulSoup to the obtained html

result = []
for anchor in page_soup.find('div').findAll('a'):
    if len(anchor.get('href')) > 50:
        result += ['http://'+netloc+'/'+anchor.get('href')]

for url in result:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})  # sends GET request to URL
    uClient = urllib.request.urlopen(req)
    page_html = uClient.read()
    uClient.close()  # close the connection

    # now for the good stuff... let's use BeautifulSoup to parse the webpage
    page_soup = soup(page_html, "html.parser")  # applying BeautifulSoup to the obtained html

    containers = page_soup.findAll("tr", {"class", "tblTotalTargets_loadPxP"})

    for container in containers:

        All_Tags=container.findAll("td")
        name = All_Tags[0].text
        team = All_Tags[1].text
        pos = All_Tags[2].text
        compl = All_Tags[3].text
        targets = All_Tags[4].text
        compl_perc = All_Tags[5].text
        tds = All_Tags[6].text
        target_perc = All_Tags[7].text

        f.write(name.replace(",", ";") + ',')
        f.write(team + ',')
        f.write(pos + ',')
        f.write(compl + ',')
        f.write(targets + ',')
        f.write(compl_perc + ',')
        f.write(tds + ',')
        f.write(target_perc + '\n')


f.close()


