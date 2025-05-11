from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import Driver
from bs4 import BeautifulSoup
import time
import json


def scrape():
    driver = Driver(browser="chrome", headless=True)
    URL = "https://insider.in/all-events-in-bengaluru"
    driver.get(URL)

    # Wait until events are fully loaded
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-list-item'))
    )

    # Scroll to trigger lazy loading
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(0, scroll_height, 600):
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(1)

    # Data structure to hold all events
    event_data = []

    # Parse the page source
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    events = soup.find_all('li', class_='card-list-item')

    # Extract data
    for event in events:
        cur_dict = {}

        image_tag = event.find('img')
        if image_tag and image_tag.get('src'):
            image_url = image_tag['src']
        else:
            image_div = event.find('div', {'id': 'event_image'})
            if image_div and image_div.get('style'):
                style = image_div.get('style')
                image_url = style.split('url(')[-1].split(')')[0].replace('"', '')
            else:
                image_url = ""
        
        link_div = event.find('div', class_='css-clv2ol')
        if link_div:  
            link_tag = link_div.find('a')
            event_link = link_tag['href'] if link_tag and link_tag.get('href') else ""

            if event_link != "":
                event_link = event_link.rsplit('/', 1)[0]
                event_link = 'https://www.district.in/events' + event_link + '-buy-tickets'
        else:
            event_link = ""

        event_type_tag = event.find('span', class_='card-genre')
        event_type = event_type_tag.get_text(strip=True) if event_type_tag else ""

        location_tag = event.find('div', {'data-ref': 'event_card_location'})
        location = location_tag.get_text(strip=True) if location_tag and location_tag.find('p') else ""

        timing_tag = event.find('div', {'data-ref': 'event_card_date_string'})
        timing = timing_tag.get_text(strip=True) if timing_tag and timing_tag.find('p') else ""

        price_tag = event.find('p', class_='css-1sh8h77')
        price = price_tag.get_text(strip=True) if price_tag else ""

        print(f"Image URL: {(image_url)}")
        print(f"Event Type: {(event_type)}")
        print(f"Location: {(location)}")
        print(f"Timing: {(timing)}")
        print(f"Price: {price}")
        print(f"Event Link: {event_link}")

        if all(len(field.strip()) != 0 for field in [image_url, event_type, location, timing]):
            event_data.append({
                "image_url": image_url,
                "event_type": event_type,
                "location": location,
                "timing": timing,
                "price": price,
                "event_link": event_link
            })

    driver.quit()

    # Save the extracted data to a JSON file
    with open('events.json', 'w', encoding='utf-8') as f:
        json.dump(event_data, f, ensure_ascii=False, indent=4)

    print("Data has been successfully saved to events.json")


