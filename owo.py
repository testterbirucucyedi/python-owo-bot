import pyautogui as auto
import time

print("1337 OwO Bot | 5 Saniye Sonra Aktif Edilecektir.")
print("----------------------------------------------------")
print("Developer > selim#1337 ")
print("----------------------------------------------------")
print("Bu Bot Python İle Geliştirilmiştir.")
time.sleep(5)
x=0
while True:
    auto.write("owo")
    auto.press("Enter")
    time.sleep(4)
    auto.write("owo hunt")
    auto.press("Enter")
    time.sleep(15)
    auto.write("owo battle")
    auto.press("Enter")
    time.sleep(20)
    x+=1
    if x == 4:
        x=0
        auto.write("Yoruldum")
        auto.press("Enter")
        time.sleep(60)
        auto.write("Neyse owo kasmaya devam")
        auto.press("Enter")