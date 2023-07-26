import time
import pyautogui
import requests

pyautogui.press('win')
pyautogui.typewrite('chrome')
pyautogui.press('enter')
time.sleep(2)  # Wait for the browser to open
pyautogui.hotkey('win', 'up')
time.sleep(2)  # Wait for the window to maximize
pyautogui.typewrite("https://www.example.com")
pyautogui.press('enter')
time.sleep(5)  # Wait for the page to load (adjust as needed)
element_location = pyautogui.locateOnScreen('element_class_name.png')
if element_location:
    element_center = pyautogui.center(element_location)
    pyautogui.moveTo(element_center)
    pyautogui.click()

# Create a dictionary and add a 'category' key
v = {}
v['category'] = "addCategory(url)"  # Replace with the appropriate value

# Get the parent element with class name "details-list--info" using PyAutoGUI
parent_element_location = pyautogui.locateOnScreen('parent_element_class_name.png')
if parent_element_location:
    parent_element_center = pyautogui.center(parent_element_location)
    pyautogui.moveTo(parent_element_center)
    pyautogui.click()

# Get the title element with class name "web_ui__Text__title" using PyAutoGUI
title_element_location = pyautogui.locateOnScreen('title_element_class_name.png')
if title_element_location:
    title_element_center = pyautogui.center(title_element_location)
    pyautogui.moveTo(title_element_center)
    pyautogui.click()

# Get the text of the title element
title_text = pyautogui.hotkey('ctrl', 'c')

# Add the 'title' key to the dictionary with the value of 'title_text'
v['title'] = title_text

# Close the browser window using PyAutoGUI
pyautogui.hotkey('alt', 'f4')
