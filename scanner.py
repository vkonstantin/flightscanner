import time
from selenium import webdriver
from search import search

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
b = webdriver.Chrome(options=options)

for to in range(10, 30):
    query = "MOW0502YTO"+str(to)+"0222"
    result = search(b, query)
    print(query, "result:", result)

time.sleep(10)
#b.close()

"""
MOW0502YTO100222 result: 
[
{'price': '1692', 
    1: {'from_time': '05:30', 'from_city': 'Moscow', 'from_date': '5 Feb 2020, We', 
        'to_time': '15:35', 'to_city': 'Toronto', 'to_date': '5 Feb 2020, We', 
        'duration': '18h 5m', 'stops': ['AMS']
        }, 
    2: {'from_time': '18:05', 'from_city': 'Toronto', 'from_date': '10 Feb 2020, Mo', 
        'to_time': '01:55', 'to_city': 'Moscow', 'to_date': '12 Feb 2020, We', 
        'duration': '23h 50m', 'stops': ['AMS']}
        }, 
{'price': '1710', 1: {'from_time': '05:30', 'from_city': 'Moscow', 'from_date': '5 Feb 2020, We', 'to_time': '15:35', 'to_city': 'Toronto', 'to_date': '5 Feb 2020, We', 'duration': '18h 5m', 'stops': ['AMS']}, 2: {'from_time': '20:00', 'from_city': 'Toronto', 'from_date': '10 Feb 2020, Mo', 'to_time': '18:55', 'to_city': 'Moscow', 'to_date': '11 Feb 2020, Tu', 'duration': '14h 55m', 'stops': ['YUL', 'CDG']}}, {'price': '1733', 1: {'from_time': '18:00', 'from_city': 'Moscow', 'from_date': '5 Feb 2020, We', 'to_time': '19:50', 'to_city': 'Toronto', 'to_date': '6 Feb 2020, Th', 'duration': '1d 9h 50m', 'stops': ['AMS']}, 2: {'from_time': '18:05', 'from_city': 'Toronto', 'from_date': '10 Feb 2020, Mo', 'to_time': '01:55', 'to_city': 'Moscow', 'to_date': '12 Feb 2020, We', 'duration': '23h 50m', 'stops': ['AMS']}}, {'price': '1744', 1: {'from_time': '05:30', 'from_city': 'Moscow', 'from_date': '5 Feb 2020, We', 'to_time': '15:35', 'to_city': 'Toronto', 'to_date': '5 Feb 2020, We', 'duration': '18h 5m', 'stops': ['AMS']}, 2: {'from_time': '15:00', 'from_city': 'Toronto', 'from_date': '10 Feb 2020, Mo', 'to_time': '00:40', 'to_city': 'Moscow', 'to_date': '12 Feb 2020, We', 'duration': '1d 1h 40m', 'stops': ['YUL', 'CDG']}}, {'price': '1744', 1: {'from_time': '18:00', 'from_city': 'Moscow', 'from_date': '5 Feb 2020, We', 'to_time': '19:50', 'to_city': 'Toronto', 'to_date': '6 Feb 2020, Th', 'duration': '1d 9h 50m', 'stops': ['AMS']}, 2: {'from_time': '20:00', 'from_city': 'Toronto', 'from_date': '10 Feb 2020, Mo', 'to_time': '18:55', 'to_city': 'Moscow', 'to_date': '11 Feb 2020, Tu', 'duration': '14h 55m', 'stops': ['YUL', 'CDG']}}, {'price': '1744', 1: {'from_time': '18:00', 'from_city': 'Moscow', 'from_date': '5 Feb 2020, We', 'to_time': '19:50', 'to_city': 'Toronto', 'to_date': '6 Feb 2020, Th', 'duration': '1d 9h 50m', 'stops': ['AMS']}, 2: {'from_time': '15:00', 'from_city': 'Toronto', 'from_date': '10 Feb 2020, Mo', 'to_time': '00:40', 'to_city': 'Moscow', 'to_date': '12 Feb 2020, We', 'duration': '1d 1h 40m', 'stops': ['YUL', 'CDG']}}, {'price': '1761', 1: {'from_time': '06:50', 'from_city': 'Moscow', 'from_date': '5 Feb 2020, We', 'to_time': '15:35', 'to_city': 'Toronto', 'to_date': '5 Feb 2020, We', 'duration': '16h 45m', 'stops': ['CDG', 'AMS']}, 2: {'from_time': '18:05', 'from_city': 'Toronto', 'from_date': '10 Feb 2020, Mo', 'to_time': '01:55', 'to_city': 'Moscow', 'to_date': '12 Feb 2020, We', 'duration': '23h 50m', 'stops': ['AMS']}}, {'price': '1763', 1: {'from_time': '05:30', 'from_city': 'Moscow', 'from_date': '5 Feb 2020, We', 'to_time': '15:35', 'to_city': 'Toronto', 'to_date': '5 Feb 2020, We', 'duration': '18h 5m', 'stops': ['AMS']}, 2: {'from_time': '15:00', 'from_city': 'Toronto', 'from_date': '10 Feb 2020, Mo', 'to_time': '18:55', 'to_city': 'Moscow', 'to_date': '11 Feb 2020, Tu', 'duration': '19h 55m', 'stops': ['YUL', 'CDG']}}, {'price': '1763', 1: {'from_time': '05:30', 'from_city': 'Moscow', 'from_date': '5 Feb 2020, We', 'to_time': '15:35', 'to_city': 'Toronto', 'to_date': '5 Feb 2020, We', 'duration': '18h 5m', 'stops': ['AMS']}, 2: {'from_time': '15:00', 'from_city': 'Toronto', 'from_date': '10 Feb 2020, Mo', 'to_time': '18:55', 'to_city': 'Moscow', 'to_date': '11 Feb 2020, Tu', 'duration': '19h 55m', 'stops': ['YUL', 'CDG']}}, {'price': '1763', 1: {'from_time': '05:30', 'from_city': 'Moscow', 'from_date': '5 Feb 2020, We', 'to_time': '15:35', 'to_city': 'Toronto', 'to_date': '5 Feb 2020, We', 'duration': '18h 5m', 'stops': ['AMS']}, 2: {'from_time': '20:00', 'from_city': 'Toronto', 'from_date': '10 Feb 2020, Mo', 'to_time': '00:40', 'to_city': 'Moscow', 'to_date': '12 Feb 2020, We', 'duration': '20h 40m', 'stops': ['YUL', 'CDG']}}]

loading is finished!
"""