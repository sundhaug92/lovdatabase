from lxml import html
import requests,redis

def Download(url):
    page=requests.get(url)
    return html.fromstring(page.text)

def DownloadLov(lovNavn):
   return Download('https://lovdata.no/dokument/NL/lov/' + lovNavn)

def ExtractDocument(tree):
    tittel=tree.xpath('//h1[1]/text()')[0]
    dato=tree.xpath('//*[@id="metaField_dato"]/text()')[0]
    dept=tree.xpath('//*[@id="metaField_departement"]/text()')[0]
    ktittel=tree.xpath('//*[@id="metaField_korttittel"]/text()')[0]
    return {"tittel":tittel,"dato":dato,"dept":dept,"ktittel":ktittel}

r=redis.Redis()
for i in range(0,745, 20):
    tree=Download('https://lovdata.no/register/lover?offset='+str(i)+'&dir=asc')
    for link in tree.xpath('//div[@class="documentList"]/h3/a/@href'):
        if "nn" not in link:
            doc=ExtractDocument(DownloadLov(link.split('/')[-1]))
            r.hmset("LOVDATA-"+doc["dato"], doc)
