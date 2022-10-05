import http.client
import json
from tqdm import tqdm

conn = http.client.HTTPSConnection("www.jarir.com")

payload = ""

headers = { 'cookie': "__cf_bm=Yi9c62OSBgXrB_plPFgV.UvamLouXzgGSaEcZdb9qIg-1663145002-0-AWnPBFBeMJQOhDHBO7px%2BSfdfqJwqW0zFiwlbrcRmxT%2BAMIdFwS5GYDt9s7t6fmM8CIubU1OV2sC9ekxJgaH0Vo%3D" }

conn.request("GET", "/api/catalogv1/product/store/sa-ar/category_ids/1008/aggregation/true/size/12/from/24/sort-priority/asc", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

#client connection
conn = http.client.HTTPSConnection("www.jarir.com")

payload = ""

headers = { 'cookie': "__cf_bm=Yi9c62OSBgXrB_plPFgV.UvamLouXzgGSaEcZdb9qIg-1663145002-0-AWnPBFBeMJQOhDHBO7px%2BSfdfqJwqW0zFiwlbrcRmxT%2BAMIdFwS5GYDt9s7t6fmM8CIubU1OV2sC9ekxJgaH0Vo%3D" }
pagelode=["12","24","36"]
import json
list_prices = []
BASE_URL = "/api/catalogv1/product/store/sa-ar/category_ids/1008/aggregation/true/size/12/from/{}/sort-priority/asc"


#scrape method Arg
list_prices = []
list_error_items = []
list_ids = []
init_page = 12


#scraping method 
for _ in tqdm(range(90)):
    conn.request(f"GET", BASE_URL.format(init_page), payload, headers)
    res = conn.getresponse()
    data = res.read()
    responseObject = json.loads(data)['hits']['hits']
    for product in responseObject:
        if product['_source']['id'] not in list_ids:
            try:
                list_prices.append({
                    'before':product['_source']['price'],
                    'special_price':product['_source']['special_price'],
                    'after': product['_source']['final_price_ex_tax'],
                    'name':product['_source']['seri'],
                    'capcity_GB':product['_source']['arabicname_field3'],
                    'RAM':product['_source']['arabicname_field4'],
                    'processer':product['_source']['arabicname_field6'],
                    'Colour':product['_source']['arabicname_field7'],
                    'model':product['_source']['model'],
                    'meta_keyword':product['_source']['meta_keyword']
                })
                list_ids.append(product['_source']['id'])
            except:
                list_error_items.append({
                    'link':BASE_URL,
                    'object': product
                })
    init_page +=12


#convert list to dataframe
import pandas as pd
pd.DataFrame(list_prices).to_csv("PATH.csv")


#save scraping Data
import pandas as pd
pd.DataFrame(list_prices).to_csv("PATH.csv")