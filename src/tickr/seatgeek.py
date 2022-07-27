import pandas as pd
import requests


class SeatGeekWrapper:

    @staticmethod
    def event_search(performers_id = "1388", page_index = 1, per_page = 25) -> pd.DataFrame:
        params = {
            'page': str(page_index),
            'per_page': str(per_page),
            'performers.id': performers_id,
            'client_id': 'MTY2MnwxMzgzMzIwMTU4', # huh... guess this is where my location is
        }

        response = requests.get('https://seatgeek.com/api/events', params=params)
        data = response.json()
        data.keys()
        pd.options.display.max_columns = None
        df = pd.DataFrame(data['events'])
        return df

    def ticket_search(event_id = "todo") -> pd.DataFrame:
        cookies = {
            'sixpack_client_id': 'c0180531-3cf2-4506-8b93-05549e06dbe4',
            'sg_uuid': '5a2a0515-1823-e064-7d50-88bdaf7786a3',
            'sixpack_client_id': 'c0180531-3cf2-4506-8b93-05549e06dbe4',
            'sg_session': '98a9668ba852e4b569827df81b38618e',
            'SeatGeekAffiliate': '%5B225%2Cnull%2C616810256%2Cnull%2Cnull%5D',
            'sg_sess': 'd7193ed7f926fdc27d7cd5d71b87ba2c2c42045aattributes%7Ca%3A3%3A%7Bs%3A10%3A%22attributes%22%3Ba%3A3%3A%7Bs%3A17%3A%22entranceSignature%22%3Bs%3A39%3A%22category%3Aentrance%3Aaffiliate%3A225%3Baid%3A225%22%3Bs%3A12%3A%22entrancePath%22%3Bs%3A1%3A%22%2F%22%3Bs%3A13%3A%22search_direct%22%3Bs%3A1%3A%220%22%3B%7Ds%3A5%3A%22flash%22%3Ba%3A0%3A%7B%7Ds%3A12%3A%22flash%2Fremove%22%3Ba%3A0%3A%7B%7D%7Dculture%7Cs%3A2%3A%22en%22%3B',
            'pxcts': 'a40a5e88-0d3a-11ed-b617-524277746459',
            '_pxvid': 'a3c801d6-0d3a-11ed-992e-484755674261',
            '__pxvid': 'a430cc94-0d3a-11ed-a902-0242ac120003',
            'fullstory-loaded': 'false',
            '_ga': 'GA1.2.1505320341.1658878102',
            '_gid': 'GA1.2.1156921031.1658878102',
            '_gcl_au': '1.1.144814828.1658878102',
            '__ssid': 'da7801d4e7cffa13f33888e21ed84fc',
            '_scid': 'b0327f28-060a-47d5-878f-72d93f2e34d0',
            '_fbp': 'fb.1.1658878102808.1673726922',
            '_tt_enable_cookie': '1',
            '_ttp': '09be065f-951c-4d93-bead-c44e77fb4e2c',
            '_sctr': '1|1658811600000',
            '_pxhd': 'I/w0BNScylsqv8RNqiHYnlzmvXm2AFCoS9rh9xbCKIHGytzOJQcvlZ/kxPUP/GKEeykvBjS21Bzswf5Cpap65w==:za4URej0T85YlRsdhxYpmrt8GwbQRE-4Iba34WXyVOvpMmCGh-9J3aRppZauuvUxZARfGRdeBcm0tVXMC-rMA3Vs/ujG858HpqTFfiDINwA=',
            'SeatGeekTimer': '1658880499',
            'tatari-session-cookie': 'c527cebe-7ee7-0e74-8c0b-d8cced1c3419',
            '_px2': 'eyJ1IjoiOWYwMDA0YzAtMGQ0MC0xMWVkLWJhZjctMzMzZmJlZTEzZmNiIiwidiI6ImEzYzgwMWQ2LTBkM2EtMTFlZC05OTJlLTQ4NDc1NTY3NDI2MSIsInQiOjE2NTg4ODA5NzQyNTQsImgiOiJkNGZmOTEwYzM2MTdlMzM1ZDc2MWI1ZWMxYjk2YjJlMDNlZDJiYmY4MDY0MDZmMGVkYWUxODY5Y2MyODdmOTNmIn0=',
            '_uetsid': 'a3ed5d000d3a11edb1d43be32e2e1eaf',
            '_uetvid': 'a3ed68700d3a11eda61a59ca87e59f69',
            'tatari-cookie-test': '32742149',
            'viewedSeatgeekEmailModal': 'true',
            'sg-event-page-view-id': '80eb8036-8077-a804-d5ce-c72b974b8f61',
        }

        headers = {
            'authority': 'seatgeek.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'sixpack_client_id=c0180531-3cf2-4506-8b93-05549e06dbe4; sg_uuid=5a2a0515-1823-e064-7d50-88bdaf7786a3; sixpack_client_id=c0180531-3cf2-4506-8b93-05549e06dbe4; sg_session=98a9668ba852e4b569827df81b38618e; SeatGeekAffiliate=%5B225%2Cnull%2C616810256%2Cnull%2Cnull%5D; sg_sess=d7193ed7f926fdc27d7cd5d71b87ba2c2c42045aattributes%7Ca%3A3%3A%7Bs%3A10%3A%22attributes%22%3Ba%3A3%3A%7Bs%3A17%3A%22entranceSignature%22%3Bs%3A39%3A%22category%3Aentrance%3Aaffiliate%3A225%3Baid%3A225%22%3Bs%3A12%3A%22entrancePath%22%3Bs%3A1%3A%22%2F%22%3Bs%3A13%3A%22search_direct%22%3Bs%3A1%3A%220%22%3B%7Ds%3A5%3A%22flash%22%3Ba%3A0%3A%7B%7Ds%3A12%3A%22flash%2Fremove%22%3Ba%3A0%3A%7B%7D%7Dculture%7Cs%3A2%3A%22en%22%3B; pxcts=a40a5e88-0d3a-11ed-b617-524277746459; _pxvid=a3c801d6-0d3a-11ed-992e-484755674261; __pxvid=a430cc94-0d3a-11ed-a902-0242ac120003; fullstory-loaded=false; _ga=GA1.2.1505320341.1658878102; _gid=GA1.2.1156921031.1658878102; _gcl_au=1.1.144814828.1658878102; __ssid=da7801d4e7cffa13f33888e21ed84fc; _scid=b0327f28-060a-47d5-878f-72d93f2e34d0; _fbp=fb.1.1658878102808.1673726922; _tt_enable_cookie=1; _ttp=09be065f-951c-4d93-bead-c44e77fb4e2c; _sctr=1|1658811600000; _pxhd=I/w0BNScylsqv8RNqiHYnlzmvXm2AFCoS9rh9xbCKIHGytzOJQcvlZ/kxPUP/GKEeykvBjS21Bzswf5Cpap65w==:za4URej0T85YlRsdhxYpmrt8GwbQRE-4Iba34WXyVOvpMmCGh-9J3aRppZauuvUxZARfGRdeBcm0tVXMC-rMA3Vs/ujG858HpqTFfiDINwA=; SeatGeekTimer=1658880499; tatari-session-cookie=c527cebe-7ee7-0e74-8c0b-d8cced1c3419; _px2=eyJ1IjoiOWYwMDA0YzAtMGQ0MC0xMWVkLWJhZjctMzMzZmJlZTEzZmNiIiwidiI6ImEzYzgwMWQ2LTBkM2EtMTFlZC05OTJlLTQ4NDc1NTY3NDI2MSIsInQiOjE2NTg4ODA5NzQyNTQsImgiOiJkNGZmOTEwYzM2MTdlMzM1ZDc2MWI1ZWMxYjk2YjJlMDNlZDJiYmY4MDY0MDZmMGVkYWUxODY5Y2MyODdmOTNmIn0=; _uetsid=a3ed5d000d3a11edb1d43be32e2e1eaf; _uetvid=a3ed68700d3a11eda61a59ca87e59f69; tatari-cookie-test=32742149; viewedSeatgeekEmailModal=true; sg-event-page-view-id=80eb8036-8077-a804-d5ce-c72b974b8f61',
            'referer': 'https://seatgeek.com/kevin-hart-tickets/comedy/2022-08-07-7-pm/5644493?listing=6mOhKp6bG09',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }

        params = {
            '_include_seats': '1',
            'aid': '225',
            'client_id': 'MTY2MnwxMzgzMzIwMTU4',
            'event_page_view_id': '80eb8036-8077-a804-d5ce-c72b974b8f61',
            'id': '5644493',
            'listing': '6mOhKp6bG09',
            'sixpack_client_id': 'c0180531-3cf2-4506-8b93-05549e06dbe4',
        }

        response = requests.get('https://seatgeek.com/api/event_listings_v2', params=params, cookies=cookies, headers=headers)
        data = response.json()
        return pd.DataFrame(data['listings'])
        