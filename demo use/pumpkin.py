import pyautogui
import webbrowser
import time

s="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
time.sleep(2)
webbrowser.get(s).open_new("https://meet.google.com/dun-zrsx-xgu")
time.sleep(5)
pyautogui.hotkey('ctrl', 'd')
pyautogui.hotkey('ctrl', 'e')

time.sleep(3)
pyautogui.click(1328, 586)
print("done")