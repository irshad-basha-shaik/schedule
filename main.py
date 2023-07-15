import schedule
import time
import requests

base="http://localhost:8080"
vintedPath="/api/Vinted/getVintedListing/71527462-excelstuff?status=not sent"
listingPath="/api/Vinted/vintedListingStatus"
Header={'Cookie':'csrftoken=bD0kdBbkK2ufeX55O4XtK4AF6v2k6QD0; JSESSIONID=B89E52FF26D9DA9DE1EAFC7F18B19B24'}
'''
Cookie: csrftoken=bD0kdBbkK2ufeX55O4XtK4AF6v2k6QD0; JSESSIONID=F63A94341CE20C5A637EEF04C5E39296
'''
def job():
    response = requests.get(base+vintedPath,headers=Header)
    k = response.json()
    #print(response)
    for element in k["results"]:
        response = requests.post(base+listingPath, params={'id':element["id"]}, headers=Header)
        kk = response.json()
        #,params={'address': location}
        print("The pastebin URL is:%s" % kk)
        print(element)



schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)