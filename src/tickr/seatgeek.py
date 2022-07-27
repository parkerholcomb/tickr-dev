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
        