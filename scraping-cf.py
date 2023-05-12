import undetected_chromedriver as uc
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
import sys
import io

# Wrap sys.stdout with an encoding-aware StreamWriter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

options = uc.ChromeOptions()
options.add_argument('--headless=new')
driver = uc.Chrome(use_subprocess=True)
driver.get("https://www.blackhatworld.com/forums/blogging.3")
driver.maximize_window()
time.sleep(5)
site = BeautifulSoup(driver.page_source, 'html.parser')
print(site)
