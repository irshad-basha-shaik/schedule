import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
driver = None

def getText(obj):
    try:
        return obj.text
    except:
        return ""
def doit(a):
    a1 = a.split("\n")
    for item3 in a1:
        list = driver.find_elements(By.CLASS_NAME, "web_ui__Cell__title")
        for element in list:
            item4 = getText(element)
            if item3 == item4:
                element.click()
                break

def getParent(obj):
    a = None
    try:
        a = driver.find_element(By.CLASS_NAME, obj)
    except:
        a = None
    return a
def getTitle(obj,str):
    a1 = None
    try:
        a1 = obj.find_element(By.CLASS_NAME, str)
    except:
        a1 = None
    return a1
def getDescription(obj,str):
    a = None
    try:
        a = obj.find_elements(By.CLASS_NAME, str)
    except:
        a = None
    return a

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("user-data-dir=C:\\Users\\yaseen\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument('profile-directory=Profile 5')
# url='https://www.vinted.co.uk/entertainment/video-games-and-consoles/xbox-one/games/2700309217-ufc-3-xbox-one'
#Google Chrome 112.0.5615.121#
#driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe', options=options)
#save_path = "C:/Users/yaseen/instagram-auto-create-account/image.jpg"

def getOldData(url):
    #driver.get(url)

    x = driver.find_elements(By.CLASS_NAME, "details-list__item")
    v = {}
    v['category'] = addCategory(url)
    a = getParent("details-list--info")
    b = getTitle(a, "web_ui__Text__title")
    c = b.text
    v['title'] = c
    b1 = getDescription(a, "u-text-wrap")
    if b1!=None :
        c1 = b1[0].text
        v['text'] = c1
    #v['text'] = c1
    #v['Category'] = 'Entertainment\nVideo games & consoles\nXbox one\nGames'
    for y in x:
        try:
            v[y.find_element(By.CLASS_NAME, "details-list__item-title").text.replace(" ", "")] = \
            y.find_element(By.CLASS_NAME, "details-list__item-value").text.split("\n")[0]
        except:
            i = 1
    v['image_path'] = getImage()
    driver.close()
    driver.quit()

    #  print(v)
   # driver.close()
    return v
def getImage():
    save_path = "C:/Users/yaseen/instagram-auto-create-account/image.jpg"
   # driver.get(url)

    try:
        a = driver.find_elements(By.CLASS_NAME,'item-thumbnail')
        print("ok")
    except:
        print("error in reading image")

    if len(a) >= 2:
        tag_name = a[1].tag_name
        style = a[1].get_attribute("style")
        url = style.split("(")[1].split(")")[0]
        url = url.strip('"')
    #    print("Image URL:", url)

        # download the image using requests
        response = requests.get(url)
        with open(save_path, "wb") as f:
            f.write(response.content)
    return save_path
def addCategory(txt):
    dx = txt.split("/")
    x = ""
    for v in range(len(dx)):
        if v > 2 and v < len(dx) - 1:
          x = x+dx[v].replace("and","&").replace("-"," ").capitalize()+"\n"
    w = x[0:len(x) - 1]
    return w
def addNewData(obj):
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe', options=options)
    driver.get("https://www.vinted.co.uk/items/new")
    """1.image section"""
    driver.implicitly_wait(3)
    js = 'p = document.getElementById("photos");'
    driver.execute_script(js)
    js = 'p.children[0].classList.remove("u-hidden");'
    driver.execute_script(js)
    s = driver.find_element(By.NAME, "photos")
    s.send_keys(obj['image_path'])

    """2.title section"""
    title = driver.find_element(By.ID, "title")
    title.send_keys(obj['title'])

    """3.description section"""
    description = driver.find_element(By.ID, "description")
    description.send_keys(obj['text'])

    """4.category"""
    catalog_id = driver.find_element(By.ID, "catalog_id").click()
    cid = driver.find_element(By.CLASS_NAME, "input-dropdown")
    #v2 = 'Women\nShoes\nClogs &'
    category = addCategory(
      'https://www.vinted.co.uk/entertainment/video-games-and-consoles/xbox-one/games/2700309217-ufc-3-xbox-one')
    v2 = category
    v3 = cid.text
    doit(v2)

    """5.brand"""
    title = driver.find_element(By.ID, "brand_id")
    title.send_keys(obj['BRAND'])
    """condition"""
    title = driver.find_element(By.ID, "status_id").click()
    title.send_keys(obj['text'])
    """6.size"""
    size_id = driver.find_element(By.ID, "size_id").click()
    cid = driver.find_element(By.CLASS_NAME, "input-dropdown")
    v2 = '2.5'
    v3 = cid.text
    doit(v2)

    """7.condition
    status_id = driver.find_element(By.ID, "status_id").click()
    cid = driver.find_element(By.CLASS_NAME, "input-dropdown")
    v2 = obj['text']
    v3 = cid.text
    doit(v2)"""

    """8.color"""
    color = driver.find_element(By.ID, "color").click()
    cid = driver.find_element(By.CLASS_NAME, "input-dropdown")
    v2 = 'Black\nOrange'
    doit(v2)
    driver.implicitly_wait(1)
    driver.find_element(By.TAG_NAME, "body").click()

    """9.price"""
    price = driver.find_element(By.ID, "price")
    price.send_keys()

    """10.parcel size"""
    time.sleep(2)
    list = driver.find_elements(By.CLASS_NAME, "web_ui__Cell__heading")
    for element in list:
        item4 = getText(element)
        print(item4)
        if "Small" == item4:
            element.click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "web_ui__Button__content").click()

    time.sleep(30)
xyz = getOldData( "https://www.vinted.co.uk/entertainment/video-games-and-consoles/xbox-one/games/2700309217-ufc-3-xbox-one")
#print(xyz)
#a = getImage("https://www.vinted.co.uk/entertainment/video-games-and-consoles/xbox-one/games/2700309217-ufc-3-xbox-one")
addNewData(xyz)


