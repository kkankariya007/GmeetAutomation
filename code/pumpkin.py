import pyautogui
import webbrowser
import time

time.sleep(2)
# r=webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open_new("https://www.google.com")

# #pyautogui.hotkey('ctrl','w')
# print(r)
# if(r):
#     pyautogui.hotkey('ctrl','w')
# 
webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://meet.google.com/dun-zrsx-xgu")
# else:
webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open_new("https://meet.google.com/dun-zrsx-xgu")
    
time.sleep(7)
pyautogui.hotkey('ctrl', 'd')
pyautogui.hotkey('ctrl', 'e')

time.sleep(3)
pyautogui.click(1328, 586)
print("done")