import requests
from lxml import html
import time
import csv

base_url = "https://atcoder.jp/ranking?contestType=algo&page="

# TODO: also scrape info on number of contests to validate and clean data better.

filename = '/home/om/Downloads/scraped_data.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Atcoder id','AtCoder rating','Codeforces id', 'Codeforces Rating'])

    for page in range(1, 300):
        print(f"on page {page} ...")
        url = base_url + str(page)
        response = requests.get(url)
        if response.status_code == 200:
            res = response.text
            tree = html.fromstring(res)
            links = tree.xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/table/tbody')
            for tr in links[0].getchildren():
                href = tr.xpath('./td[2]/a[2]')
                atcoder_url = f"https://atcoder.jp{href[0].get('href')}"
                userpage = ''
                user = f"https://atcoder.jp{href[0].get('href')}"
                i = 0
                # print(atcoder_url)
                while(userpage == ''):
                    try:
                        userpage = requests.get(user) 
                        break
                    except:
                        print(f"oof trying in {i+5}")
                        i+=5
                        time.sleep(i)
                        continue
                usertree = html.fromstring(userpage.text)
                try:
                    tb = usertree.xpath('/html/body/div[1]/div/div[1]/div[3]')[0].getchildren()[2]
                    atcoder_rating = (tb[2].getchildren()[1].getchildren()[0].text_content())
                except:
                    continue
                try:
                    cf_id = (usertree.get_element_by_id("codeforces_id").get('href')).split('/')[-1]
                except KeyError:
                    continue
                try:
                    cf_url = f"https://codeforces.com/api/user.info?handles={cf_id}"
                    cf_res = requests.get(cf_url)
                    cf_rating = cf_res.json()['result'][0]['rating']
                    print(f"{atcoder_url} success")
                    writer.writerow([atcoder_url.split('/')[-1],atcoder_rating, cf_id,cf_rating])
                except:
                    continue
        else:
            print("Request failed with status code:", response.status_code)
