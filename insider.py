import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def fxp(xpath: str, rows=range(2, 102)) -> list:
    return [driver.find_element_by_xpath(xpath.replace("NONE", str(i))).text for i in rows]


# settings
chrome_options = Options()
chrome_options.add_argument("headless")
url = "https://www.insidearbitrage.com/insider-buying/?desk=yes"

driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options, keep_alive=False)
driver.get(url)

# xpaths
symbol_path = """//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[NONE]/td[2]"""
position_path = """//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[NONE]/td[4]"""
date_path = """//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[NONE]/td[5]"""
cost_path = """//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[NONE]/td[6]"""
shares_path = """//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[NONE]/td[7]"""
shares_held_path = """//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[NONE]/td[8]"""

# to csv
all_data = list(zip(fxp(symbol_path), fxp(position_path), fxp(date_path), fxp(cost_path), fxp(shares_path),
                    fxp(shares_held_path)))
df = pd.DataFrame(all_data, columns=["Symbol", "Position", "Date", "Share Cost", "Shares Bought", "Shares Held"])
df.to_csv('insider.csv', index=False)
