import time
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import json
import csv
from typing import Any, List, Dict

list_of_dicts: List[Any] = []  # variable refers to empty list


async def get_hrefs():  # define an asynchronous function without parameters
    headers: Dict[str, str] = {
        'Accept': '* / *',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }

    url = f'https://cars.av.by/kia/niro'
    async with aiohttp.ClientSession() as session:  # create a Client session
        response = await session.get(url=url, headers=headers)  # get page code
        soup = BeautifulSoup(await response.text(), 'lxml')  # create a BeautifulSoup object
        all_cars_hrefs = soup.find_all(class_="listing-item__link")  # create a list with that contains all hrefs
        hrefs_list: List[Any] = ['https://cars.av.by' + item.get('href') for item in all_cars_hrefs]
        # list contains all hrefs

        tasks: List[Any] = []

        for href in hrefs_list:  # cycle
            task = asyncio.create_task(get_information(session, href))  # create a task
            tasks.append(task)  # add task to list of tasks

        await asyncio.gather(*tasks)  # function returns  a list of finished results of waiting objects


async def get_information(session, href):  # define an asynchronous function with two parameters
    headers: Dict[str, str] = {
        'Accept': '* / *',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }

    async with session.get(url=href, headers=headers) as response:  # get a page code of a given link
        response_text = await response.text()  # html text of the given page
        soup = BeautifulSoup(response_text, 'lxml')  # create a BeautifulSoup object

        try:
            price_byn = soup.find('div', class_="card__price-primary").text.encode('ascii', errors='ignore').decode(
                'UTF-8')  # take a price in BYN from the page
            price_usd = soup.find('div', class_="card__price-secondary").text.encode('ascii', errors='ignore').decode(
                'UTF-8')  # take a price in USD from the page
            parameters = soup.find('div', class_="card__params").text.replace('\xa0', ' ').replace('\u2009', ' ')
            # take parameters from the page

            list_of_dicts.append(
                {
                    'href': href,
                    'price_byn': price_byn,
                    'price_uds': price_usd,
                    'parameters': parameters
                }
            )
            # create a dict and add it to the list

        except Exception as ex:  # code block for catching exceptions
            print(ex)


def main():  # function without parameters
    asyncio.run(get_hrefs())  # function runs the another function asynchronously

    with open(f'kia_niro_async.json', 'w', encoding='UTF-8') as file:  # open json file for writing
        json.dump(list_of_dicts, file, indent=4, ensure_ascii=False)  # write a list of dicts in the file

    with open(f'kia_niro_async.csv', 'w', encoding='UTF-8', newline='') as file:  # open or create csv file
        writer = csv.writer(file)  # create a writer object

        writer.writerow(
            (
                'Href',
                'Price BYN',
                'Price USD',
                'Parameters'
            )
        )
        # write a headlines

    for information in list_of_dicts:  # cycle
        with open(f'kia_niro_async.csv', 'a', newline='') as file:  # open file to add information
            writer = csv.writer(file)  # create a writer object

            writer.writerow(
                (
                    information['href'],
                    information['price_byn'],
                    information['price_uds'],
                    information['parameters']
                )
            )
            # add information to the file
    finish: float = time.time() - start  # variable that shows how many time takes this program
    print(finish)  # built-in function that print the information to the console


if __name__ == '__main__':  # condition: if we run the program from this file
    start: float = time.time()  # variable that contains time since the beginning of the era
    main()  # call the function
