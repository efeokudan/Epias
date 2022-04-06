from selenium.webdriver.common.keys import Keys
import selenium
from selenium import webdriver


webbrowser=webdriver.Chrome("C:\\Users\\theef\\Desktop\\chromedriver.exe")

webbrowser.get("https://seffaflik.epias.com.tr/transparency/uretim/gerceklesen-uretim/gercek-zamanli-uretim.xhtml")
button = webbrowser.find_element_by_xpath("/html/body/div[5]/form/div[1]/div/div/div[1]/div[2]/span/input")
button.send_keys(Keys.DELETE)
button.send_keys("30.04.2021")
button = webbrowser.find_element_by_xpath("/html/body/div[5]/form/div[1]/div/div/div[2]/div[2]/span/input")
button.send_keys(Keys.DELETE)
button.send_keys("30.04.2021")
button = webbrowser.find_element_by_xpath ("/html/body/div[5]/form/div[1]/div/div/div[4]/div/div[1]/button")
button.click()
row = webbrowser.find_elements_by_class_name("TexAlCenter")
saat = ([r.text for i,r  in enumerate(row) if i % 18 == 1])
megawat = ([r.text for i,r  in enumerate(row) if i % 18 == 2])

webbrowser.get("https://seffaflik.epias.com.tr/transparency/tuketim/gerceklesen-tuketim/gercek-zamanli-tuketim.xhtml")
button = webbrowser.find_element_by_xpath("/html/body/div[5]/form/div[1]/div/div/div[1]/div[2]/span/input")
button.send_keys(Keys.DELETE)
button.send_keys("30.04.2021")
button = webbrowser.find_element_by_xpath("/html/body/div[5]/form/div[1]/div/div/div[2]/div[2]/span/input")
button.send_keys(Keys.DELETE)
button.send_keys("30.04.2021")
button = webbrowser.find_element_by_xpath ("/html/body/div[5]/form/div[1]/div/div/div[3]/div/button")
button.click()
row = webbrowser.find_elements_by_class_name("TexAlCenter")
megawatt = ([r.text for i,r  in enumerate(row) if i % 3 == 2])

for i in range (1,25):
    fwatt = (float(megawatt[i].replace('.', '').replace(',', '.')))
    fwat = (float(megawat[i].replace('.', '').replace(',', '.')))
    print(f"{saat[i]}   ::   {fwat-fwatt}")

webbrowser.close()
