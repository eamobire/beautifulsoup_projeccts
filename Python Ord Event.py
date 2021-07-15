from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.python.org/")
py_org = response.text

soup = BeautifulSoup(py_org, "html.parser")
dates = soup.select(".event-widget time")
events = soup.select(".event-widget li a")

list_of_dates = [date.text for date in dates]
list_of_events = [event.text for event in events]
#
# print(list_of_dates)
# print(list_of_events)

upcoming_events = {}
for n in range(0, (len(list_of_events))):
    upcoming_events[n] = {
        "date": list_of_dates[n],
        "event": list_of_events[n]
    }

print(upcoming_events)