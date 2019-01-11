from multiprocessing import Pool, cpu_count, freeze_support
from selenium import webdriver
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep
import random


def get_proxies(ua):
    proxies = []
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')

    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

  # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
                        'ip':   row.find_all('td')[0].string,
                        'port': row.find_all('td')[1].string})
    return proxies

def random_proxy(proxies):
  return random.choice(proxies)

def search_string_to_query(search_string):
    search = search_string.split(' ')
    query = '+'.join(search)
    return query

def search_and_click(ua,sleep_time,search_string,proxy,proxies,sleep_after):

    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s'%(proxy['ip'] + ':' + proxy['port']))
    options.add_argument('user-agent=%s'%ua.random)

    driver = webdriver.Chrome(chrome_options=options)
    query = search_string_to_query(search_string)
    driver.get('https://www.youtube.com/results?search_query=%s'%query)
    
    try:
        section_list = driver.find_element_by_class_name('section-list')

        link = section_list.find_element_by_class_name('yt-uix-tile-link')

        link.click()
    
        sleep(sleep_time)
    
        driver.quit()
        
        if sleep_after is not None:
            sleep(sleep_after)
    
    except:
        driver.quit()
        proxy = random.choice(proxies)
        search_and_click(ua,sleep_time,search_string,proxy,proxies,sleep_after)
        
def parse_line(line):
    delim_loc = line.find('=')
    return line[delim_loc+1:].strip()

def read_config(config_string):
    try:
        search_string = parse_line(config_string[0])
        min_watch = int(parse_line(config_string[1]))
        max_watch = int(parse_line(config_string[2]))
        sleep_after = int(parse_line(config_string[3]))
        views = int(parse_line(config_string[4]))
        multicore = parse_line(config_string[5])
        if multicore != 'True':
            multicore = False
        if sleep_after == 'None':
            sleep_after = None
        return search_string,sleep_after, min_watch, max_watch, views, multicore
    except:
        write_defaults()
        return 'Bad File', 'RIP', 'Bad File', 'RIP', 'Bad File', 'RIP'
    
def write_defaults():
    with open('config.txt', 'w') as config:
        config.write('search_string = Your Search Here\n')
        config.write('min_watch = 10\n')
        config.write('max_watch = 45\n')
        config.write('wait_after = 15\n')
        config.write('views = 100\n')
        config.write('multicore = False')

write_defaults()

if __name__ == "__main__":
    freeze_support()
    with open('config.txt', 'r') as config:
        config_values = config.readlines()
    
    search_string, sleep_after, min_watch ,max_watch, views, multicore = read_config(config_values)
    if min_watch == 'Bad File':
        i = 'rip'
    elif multicore:
        threads = int(cpu_count()*0.75)
        pool = Pool(threads)
        ua = UserAgent()
        proxies = get_proxies(ua)
        for i in range(views):
            sleep_time = random.randint(min_watch,max_watch)
            proxy = random_proxy(proxies)
            pool.apply_async(search_and_click, args=[ua,sleep_time,search_string,proxy,proxies,sleep_after])
        pool.close()
        pool.join()
    else:
        ua = UserAgent()
        proxies = get_proxies(ua)
        for i in range(views):
            sleep_time = random.randint(min_watch,max_watch)
            proxy = random_proxy(proxies)
            search_and_click(ua,sleep_time,search_string,proxy,proxies,sleep_after)

