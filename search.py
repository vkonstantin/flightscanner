import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def search(b, query):
    b.get("https://www.aviasales.com/search/" + query)

    delay = 60  # seconds
    try:
        WebDriverWait(b, delay).until(EC.presence_of_element_located((By.ID, 'stops_all')))
    except TimeoutException:
        print("Loading stops_all took too much time!")
        return False

    try:
        bar = b.find_element_by_class_name("loader__bar")
    except NoSuchElementException:
        print("Search haven't been started!")
        return False

    i = 0
    while True:
        i = i + 1
        if i == delay:
            print("Loading results took too much time!")
            return False
        time.sleep(1)
        is_finished = "--animation-finished" in bar.get_attribute("class")
        if is_finished:
            break

    result = parse_result(b)
    return result


def parse_result(b):
    try:
        list = b.find_elements_by_class_name("ticket-desktop")
    except NoSuchElementException:
        print("ticket-desktop not found!")
        return False

    result = []
    for i in list:
        r = parse_result_item(i)
        if r:
            result.append(r)

    return result


def parse_result_item(i):
    r = {}
    # price
    try:
        pb = i.find_element_by_class_name("buy-button__price")
        p = pb.find_element_by_class_name("price")
        price = p.get_attribute('innerHTML').replace('\u2009', '')
        r["price"]=price
    except NoSuchElementException:
        print("price not found!")

    try:
        segments = i.find_elements_by_class_name("ticket-desktop__segment")
        n = 0
        for s in segments:
            n = n + 1
            sr = parse_segment(s)
            r[n] = sr
    except NoSuchElementException:
        print("segments not found!")

    return r

def parse_segment(s):
    r = {}
    try:
        o = s.find_element_by_class_name("origin")
        r["from_time"] = get(o, "segment-route__time")
        r["from_city"] = get(o, "segment-route__city")
        r["from_date"] = get(o, "segment-route__date")
    except NoSuchElementException:
        print("origin not found!")

    try:
        d = s.find_element_by_class_name("destination")
        r["to_time"] = get(d, "segment-route__time")
        r["to_city"] = get(d, "segment-route__city")
        r["to_date"] = get(d, "segment-route__date")
    except NoSuchElementException:
        print("destination not found!")

    r["duration"] = get(s, "segment-route__duration").replace('Duration:','').strip()

    stops = []
    try:
        iata_list = s.find_elements_by_class_name("segment-route__stop")
        for it in iata_list:
            ita = it.get_attribute('data-iatas')
            stops.append(ita)
    except:
        print("iatas not found!")

    r["stops"] = stops

    return r

def get(element, class_name):
    try:
        e = element.find_element_by_class_name(class_name)
        v = e.get_attribute('innerHTML')
        return v
    except NoSuchElementException:
        return ""
    return ""

