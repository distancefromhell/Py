from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import string
import threading

def usa_file(arg: str) -> None:
    with open('usa.txt', 'a') as f:
        f.write(f'{arg}\n')

def aus_file(arg: str) -> None:
    with open('aus.txt', 'a') as f:
        f.write(f'{arg}\n')

def ca_file(arg: str) -> None:
    with open('ca.txt', 'a') as f:
        f.write(f'{arg}\n')

def gb_file(arg: str) -> None:
    with open('gb.txt', 'a') as f:
        f.write(f'{arg}\n')

def nl_file(arg: str) -> None:
    with open('nl.txt', 'a') as f:
        f.write(f'{arg}\n')

def jp_file(arg: str) -> None:
    with open('jp.txt', 'a') as f:
        f.write(f'{arg}\n')

def de_file(arg: str) -> None:
    with open('de.txt', 'a') as f:
        f.write(f'{arg}\n')

def fr_file(arg: str) -> None:
    with open('fr.txt', 'a') as f:
        f.write(f'{arg}\n')

def se_file(arg: str) -> None:
    with open('se.txt', 'a') as f:
        f.write(f'{arg}\n')

def none_file(arg: str) -> None:
    with open('none.txt', 'a') as f:
        f.write(f'{arg}\n')

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

options = webdriver.ChromeOptions()
options.headless = True

def do_request():
       while True:
              driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
              driver.get("http://www.psnleaderboard.com/" + random_char(4))
              sleep(10)
              element = driver.find_element_by_id('profile-trophy-counts')
              get_title = driver.title
              if driver.find_elements_by_css_selector("img[src='images/flags/24/au.png"):
                  aus_file(f"{get_title} {element.text}")
              elif driver.find_elements_by_css_selector("img[src='images/flags/24/us.png"):
                  usa_file(f"{get_title} {element.text}")
              elif driver.find_elements_by_css_selector("img[src='images/flags/24/ca.png"):
                     ca_file(f"{get_title} {element.text}")
              elif driver.find_elements_by_css_selector("img[src='images/flags/24/nl.png"):
                     nl_file(f"{get_title} {element.text}")
              elif driver.find_elements_by_css_selector("img[src='images/flags/24/jp.png"):
                  usa_file(f"{get_title} {element.text}")
              elif driver.find_elements_by_css_selector("img[src='images/flags/24/de.png"):
                     de_file(f"{get_title} {element.text}")
              elif driver.find_elements_by_css_selector("img[src='images/flags/24/fr.png"):
                    fr_file(f"{get_title} {element.text}")
              elif driver.find_elements_by_css_selector("img[src='images/flags/24/gb.png"):
                    gb_file(f"{get_title} {element.text}")
              elif driver.find_elements_by_css_selector("img[src='images/flags/24/se.png"):
                    se_file(f"{get_title} {element.text}")
              else: none_file(f"{get_title} {element.text}")

threads = []

for i in range(5):
       t = threading.Thread(target=do_request)
       t.daemon = True
       threads.append(t)

for i in range(5):
       threads[i].start()

for i in range(5):
       threads[i].join()