import pandas as pd
import requests


class StubHubWrapper:
    @staticmethod
    def event_search(phrase) -> pd.DataFrame:
        cookies = {
            "d": "XZVCGqzf2gEc-zug3L3FQKs_j9QCN0WWJdyaVg2",
            "s": "EpypxOGOQUapLhqTeo9iylwYwyBXb9oI0",
            "akacd_rls": "3836327721~rv=21~id=160b8cbf67608165394aef2e6d669092",
            "ak_bmsc": "4076A3DE7576FC55898A7EDEAAD4CFD6~000000000000000000000000000000~YAAQVx8euI+YIhmCAQAAqIemPBDtsUGfNwJ8f513gnwNyUPPBfhutPInxbzwgYNxCwTjkQmE3oIq9+p7IQ0gCP4TbsBHWGgPeUoX/6tfB3Z+s+BWieP8TsY3eOtQM9drB1HiSkRKVI180w0ZMtr446p4ojHTlkhe+bKNROCDMQ+Pr6T5PwMHS1Oma+Xe0/JNaDkpISqjXeAyM8yAYpCUvKOXngONsPxYTClBnFt4pp73nyRwryC3ZtldWcwlDdaPiC5b8THYZ1NEPsOnn+oV+htq+ZvwopgznrpIPMRl+Kpq1CpJ2ozLeRC1mMutO7g2unW93j9Qr3VcMCDtv+au4qrK003EDIgYRU8Y1P4C5Y4SQTkDcaaox1PNqLXXa3vGGoJS940CSIZClRs=",
            "_rvt": "lILSeCodMYATYFxhTMvO78OshgPvChWjtmL6xSBceLgoZIONgIhLGqkRu4SD5nTAHZDl7MG9Cxkc3_UNIg0wBmSTvRCuBw0CyUTjJ9zn2QU1",
            "_ga": "GA1.2.753079407.1658874923",
            "_gid": "GA1.2.645383823.1658874923",
            "_gat": "1",
            "bm_sv": "CDA4099AC0DE2E86A4C6103D006102A6~YAAQVx8euM6YIhmCAQAAgoymPBBTJ0yhgspbbOTaCrQFAteqqvdG5NtT7tbrMC6SggrliSzeEVzykzFp7LKLXPlNwG2HlV3+yfb2oA/2qIlozbZXF995xAU3blB70N01JNYR0Q8UtfbIm85+dpNsyZ3onPBPty55UjMMTgc0cMLw+CmZRpyV8YcG70rCBPLgVdlr0RrAGIZEDU105P5djYjnh0T/aF/6QqWJgsjkKLUhn4yJ8g95YhPEuCNZaSO+OQ==~1",
            "ai_user": "jLak+SfaGz5eUB7fIeSsu1|2022-07-26T22:35:23.013Z",
            "ai_session": "hWOHBf4l9E8lftaDSB4Jra|1658874923018|1658874923018",
            "_uetsid": "3cb8def00d3311edabe253a736d40b6c",
            "_uetvid": "3cb91d400d3311eda216a1519e9b7378",
            "_clck": "qgqz06|1|f3h|0",
            "wsso": "eyJ1bCI6eyJuIjpudWxsLCJzIjpmYWxzZSwibGciOi05Ny43NDMsImx0IjozMC4yNjcsImN0IjoiVVMifSwidXBsIjp7ImN0IjoiVVMiLCJuIjoiQXVzdGluJTJDJTIwVFglMkMlMjBVU0EiLCJsdCI6MzAuMjY3MTUzLCJsZyI6LTk3Ljc0MzA2MDh9LCJkIjp7InR5cGUiOjAsImRhdGVzIjp7ImZyb20iOm51bGwsInRvIjoiOTk5OS0xMi0zMVQyMzo1OTo1OS45OTk5OTk5WiJ9fSwicnYiOnsiYyI6W10sImUiOltdLCJsIjpbXSwicnRjX3UiOm51bGwsInJ0Y19ldCI6IjIwMjItMDctMjZUMjI6MzU6MjIuOTg1MTQ3OVoifSwicCI6W10sImlkIjpudWxsfQ==",
        }

        headers = {
            "authority": "www.stubhub.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            # Requests sorts cookies= alphabetically
            # 'cookie': 'd=XZVCGqzf2gEc-zug3L3FQKs_j9QCN0WWJdyaVg2; s=EpypxOGOQUapLhqTeo9iylwYwyBXb9oI0; akacd_rls=3836327721~rv=21~id=160b8cbf67608165394aef2e6d669092; ak_bmsc=4076A3DE7576FC55898A7EDEAAD4CFD6~000000000000000000000000000000~YAAQVx8euI+YIhmCAQAAqIemPBDtsUGfNwJ8f513gnwNyUPPBfhutPInxbzwgYNxCwTjkQmE3oIq9+p7IQ0gCP4TbsBHWGgPeUoX/6tfB3Z+s+BWieP8TsY3eOtQM9drB1HiSkRKVI180w0ZMtr446p4ojHTlkhe+bKNROCDMQ+Pr6T5PwMHS1Oma+Xe0/JNaDkpISqjXeAyM8yAYpCUvKOXngONsPxYTClBnFt4pp73nyRwryC3ZtldWcwlDdaPiC5b8THYZ1NEPsOnn+oV+htq+ZvwopgznrpIPMRl+Kpq1CpJ2ozLeRC1mMutO7g2unW93j9Qr3VcMCDtv+au4qrK003EDIgYRU8Y1P4C5Y4SQTkDcaaox1PNqLXXa3vGGoJS940CSIZClRs=; _rvt=lILSeCodMYATYFxhTMvO78OshgPvChWjtmL6xSBceLgoZIONgIhLGqkRu4SD5nTAHZDl7MG9Cxkc3_UNIg0wBmSTvRCuBw0CyUTjJ9zn2QU1; _ga=GA1.2.753079407.1658874923; _gid=GA1.2.645383823.1658874923; _gat=1; bm_sv=CDA4099AC0DE2E86A4C6103D006102A6~YAAQVx8euM6YIhmCAQAAgoymPBBTJ0yhgspbbOTaCrQFAteqqvdG5NtT7tbrMC6SggrliSzeEVzykzFp7LKLXPlNwG2HlV3+yfb2oA/2qIlozbZXF995xAU3blB70N01JNYR0Q8UtfbIm85+dpNsyZ3onPBPty55UjMMTgc0cMLw+CmZRpyV8YcG70rCBPLgVdlr0RrAGIZEDU105P5djYjnh0T/aF/6QqWJgsjkKLUhn4yJ8g95YhPEuCNZaSO+OQ==~1; ai_user=jLak+SfaGz5eUB7fIeSsu1|2022-07-26T22:35:23.013Z; ai_session=hWOHBf4l9E8lftaDSB4Jra|1658874923018|1658874923018; _uetsid=3cb8def00d3311edabe253a736d40b6c; _uetvid=3cb91d400d3311eda216a1519e9b7378; _clck=qgqz06|1|f3h|0; wsso=eyJ1bCI6eyJuIjpudWxsLCJzIjpmYWxzZSwibGciOi05Ny43NDMsImx0IjozMC4yNjcsImN0IjoiVVMifSwidXBsIjp7ImN0IjoiVVMiLCJuIjoiQXVzdGluJTJDJTIwVFglMkMlMjBVU0EiLCJsdCI6MzAuMjY3MTUzLCJsZyI6LTk3Ljc0MzA2MDh9LCJkIjp7InR5cGUiOjAsImRhdGVzIjp7ImZyb20iOm51bGwsInRvIjoiOTk5OS0xMi0zMVQyMzo1OTo1OS45OTk5OTk5WiJ9fSwicnYiOnsiYyI6W10sImUiOltdLCJsIjpbXSwicnRjX3UiOm51bGwsInJ0Y19ldCI6IjIwMjItMDctMjZUMjI6MzU6MjIuOTg1MTQ3OVoifSwicCI6W10sImlkIjpudWxsfQ==',
            "referer": "https://www.stubhub.com/secure/search?q=moody+center&sellSearch=false&ct=1",
            "request-context": "appId=cid-v1:d2ec73bc-3fa1-4bd1-8c0c-c27c69bb4833",
            "request-id": "|3a4bf3c2fb7e4b5290067dd161a0e03a.cfcf1aa6bac04f20",
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "traceparent": "00-3a4bf3c2fb7e4b5290067dd161a0e03a-cfcf1aa6bac04f20-01",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        }

        params = {
            "gridFilterType": "0",
            "sortBy": "0",
            "pageIndex": "0",
            "method": "GetSearchEvents",
            "searchKeyWord": phrase,
            "radiusFrom": "0",
            "radiusTo": "80467",
            "from": "2022-07-26T22:35:23.267Z",
            "to": "9999-12-31T23:59:59.999Z",
            "lat": "30.267153",
            "lon": "-97.7430608",
        }

        response = requests.get(
            "https://www.stubhub.com/secure/search",
            params=params,
            cookies=cookies,
            headers=headers,
        )
        search_response = response.json()
        search_response.keys()

        df = pd.DataFrame(search_response["items"])
        return df

    @staticmethod
    def tickets_search(
        endpoint="", quantity=2, page_size=20, current_page=1
    ) -> pd.DataFrame:
        cookies = {
            "d": "1mZMfATa2gEq6cbPsdDaTrassNaz5IFOnpRgdw2",
            "akacd_rls": "3835705975~rv=36~id=507c2ef846a4db20ab214ac3a45fd9fc",
            "PCID": "PSUSGOOCONJAMESD15B5A6117",
            "vTrack": "49",
            "wsp": "eyJsIjoyMDU3fQ2",
            "s": "T4Neczaqe0a4_BBMN9thLiEb2IKvadoI0",
            "_rvt": "xMkPoTKgIhFBR0FVph8KGgaQaceNdw-BLJhUMS7k7COnKKuUO-7ZdPd59jbtpcOCFfBRfLnGlJ0sx-gpi2-npSsoZRo0VV5KYBKfiFd69QA1",
            "_ga": "GA1.2.898719181.1658253177",
            "_gac_UA-266806-12": "1.1658253177.CjwKCAjwrNmWBhA4EiwAHbjEQCgy5N99IADEKIofTNHI748zNSbuJcKUC1ZHJn1yoVJjFsAdhZ2rjhoCoEMQAvD_BwE",
            "_gcl_aw": "GCL.1658253177.CjwKCAjwrNmWBhA4EiwAHbjEQCgy5N99IADEKIofTNHI748zNSbuJcKUC1ZHJn1yoVJjFsAdhZ2rjhoCoEMQAvD_BwE",
            "_gcl_au": "1.1.2085686699.1658253177",
            "ai_user": "Oid/uAay+pWBLr69C0HZ1U|2022-07-19T17:52:56.852Z",
            "_fbp": "fb.1.1658253177052.317686073",
            "wsso": "eyJ1bCI6eyJuIjpudWxsLCJzIjpmYWxzZSwibGciOi05Ny43NDMsImx0IjozMC4yNjcsImN0IjoiVVMifSwidXBsIjp7ImN0IjoiVVMiLCJuIjoiQXVzdGluJTJDJTIwVFglMkMlMjBVU0EiLCJsdCI6MzAuMjY3MTUzLCJsZyI6LTk3Ljc0MzA2MDh9LCJkIjp7InR5cGUiOjAsImRhdGVzIjp7ImZyb20iOm51bGwsInRvIjoiOTk5OS0xMi0zMVQyMzo1OTo1OS45OTk5OTk5WiJ9fSwicnYiOnsiYyI6W10sImUiOltdLCJsIjpbXSwicnRjX3UiOm51bGwsInJ0Y19ldCI6IjIwMjItMDctMTlUMTc6NTI6NTYuMjY0NDA1WiJ9LCJwIjpbXSwiaWQiOm51bGx9",
            "rskxRunCookie": "0",
            "rCookie": "k8yuxejyqa8n4z8p7xs4fl5sh4nzw",
            "ftr_ncd": "6",
            "ak_bmsc": "26F67497E975BEFD589D23B2F4EE757D~000000000000000000000000000000~YAAQBKjOF0pwiyGCAQAA5pqiPBBgwdpEV0azXi02S7sKQnrnupRjt1oM0+8b4Fv1IXGeYP41MvcS+TBO+OjJAabE1Gwhek/NAt0PAHas2tRd7l1bJpriC1LSb5qN35SC9ritBZrBQMAshqLi18RdV7L8QFyZw83lo8RkvEYB0VJfWdCygAis1irfT2QQqtokeCBe+vEnJ6KaOUVe8d/fAkX5ysEorLjacIzMua0OcE6jUL2Zue4hKbBeXVHi5FaYxXsSrURuURtsOwlX9K14oO+rUoE+QPj2PQkGclWAfnXJnsMJYr9YPziCh+YfjK2dFIQa3JXZRENI0jTL7civosE1kvkr9BAWEqz6WI5Y51q0FbS+3vmTVpMGEAKX24CGsMl3+C3sk6QEPM8=",
            "_gid": "GA1.2.795214417.1658874665",
            "_clck": "jvj0lf|1|f3h|0",
            "_uetsid": "a31d26000d3211ed92ad1bb6acd6b7e7",
            "_uetvid": "4abb9b10aac411ec9826d9fe676d5b2a",
            "lastRskxRun": "1658875527861",
            "bm_sv": "F510CB9DC578EFCA6130FE35AB9F37F7~YAAQJDsvF+ebAyeCAQAAWsivPBDXZe4DzOTZ4M5CIqBkbSZ96T5LB1wNswAj2P5xgVci7Xv9YqA8WAUS/UfYZdCGwQ6Cx8kdkfu/J+YthRtLLb+P73YL6WFcNrJH2CmjOjDmErzSQs+EFYuxFMg9ujSXs6uu0jUj2EYisSCjpHo4mnPA7dB1ptjoa6FvhZsQBLOByPrKNLRe3I8tkn4B/nDXzF4mcwKG8oe3Qo0bDqsZDgwkXCzcwumqmF80PkWrwTU=~1",
            "forterToken": "3976839465ce40918d1dc4709992da52_1658875527651__UDF43_9ck",
            "_clsk": "1ozixrb|1658875528363|9|0|h.clarity.ms/collect",
            "ai_session": "KGi2odv5q0PEkickRczorE|1658874664998|1658875559666",
        }

        headers = {
            "authority": "www.stubhub.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'd=1mZMfATa2gEq6cbPsdDaTrassNaz5IFOnpRgdw2; akacd_rls=3835705975~rv=36~id=507c2ef846a4db20ab214ac3a45fd9fc; PCID=PSUSGOOCONJAMESD15B5A6117; vTrack=49; wsp=eyJsIjoyMDU3fQ2; s=T4Neczaqe0a4_BBMN9thLiEb2IKvadoI0; _rvt=xMkPoTKgIhFBR0FVph8KGgaQaceNdw-BLJhUMS7k7COnKKuUO-7ZdPd59jbtpcOCFfBRfLnGlJ0sx-gpi2-npSsoZRo0VV5KYBKfiFd69QA1; _ga=GA1.2.898719181.1658253177; _gac_UA-266806-12=1.1658253177.CjwKCAjwrNmWBhA4EiwAHbjEQCgy5N99IADEKIofTNHI748zNSbuJcKUC1ZHJn1yoVJjFsAdhZ2rjhoCoEMQAvD_BwE; _gcl_aw=GCL.1658253177.CjwKCAjwrNmWBhA4EiwAHbjEQCgy5N99IADEKIofTNHI748zNSbuJcKUC1ZHJn1yoVJjFsAdhZ2rjhoCoEMQAvD_BwE; _gcl_au=1.1.2085686699.1658253177; ai_user=Oid/uAay+pWBLr69C0HZ1U|2022-07-19T17:52:56.852Z; _fbp=fb.1.1658253177052.317686073; wsso=eyJ1bCI6eyJuIjpudWxsLCJzIjpmYWxzZSwibGciOi05Ny43NDMsImx0IjozMC4yNjcsImN0IjoiVVMifSwidXBsIjp7ImN0IjoiVVMiLCJuIjoiQXVzdGluJTJDJTIwVFglMkMlMjBVU0EiLCJsdCI6MzAuMjY3MTUzLCJsZyI6LTk3Ljc0MzA2MDh9LCJkIjp7InR5cGUiOjAsImRhdGVzIjp7ImZyb20iOm51bGwsInRvIjoiOTk5OS0xMi0zMVQyMzo1OTo1OS45OTk5OTk5WiJ9fSwicnYiOnsiYyI6W10sImUiOltdLCJsIjpbXSwicnRjX3UiOm51bGwsInJ0Y19ldCI6IjIwMjItMDctMTlUMTc6NTI6NTYuMjY0NDA1WiJ9LCJwIjpbXSwiaWQiOm51bGx9; rskxRunCookie=0; rCookie=k8yuxejyqa8n4z8p7xs4fl5sh4nzw; ftr_ncd=6; ak_bmsc=26F67497E975BEFD589D23B2F4EE757D~000000000000000000000000000000~YAAQBKjOF0pwiyGCAQAA5pqiPBBgwdpEV0azXi02S7sKQnrnupRjt1oM0+8b4Fv1IXGeYP41MvcS+TBO+OjJAabE1Gwhek/NAt0PAHas2tRd7l1bJpriC1LSb5qN35SC9ritBZrBQMAshqLi18RdV7L8QFyZw83lo8RkvEYB0VJfWdCygAis1irfT2QQqtokeCBe+vEnJ6KaOUVe8d/fAkX5ysEorLjacIzMua0OcE6jUL2Zue4hKbBeXVHi5FaYxXsSrURuURtsOwlX9K14oO+rUoE+QPj2PQkGclWAfnXJnsMJYr9YPziCh+YfjK2dFIQa3JXZRENI0jTL7civosE1kvkr9BAWEqz6WI5Y51q0FbS+3vmTVpMGEAKX24CGsMl3+C3sk6QEPM8=; _gid=GA1.2.795214417.1658874665; _clck=jvj0lf|1|f3h|0; _uetsid=a31d26000d3211ed92ad1bb6acd6b7e7; _uetvid=4abb9b10aac411ec9826d9fe676d5b2a; lastRskxRun=1658875527861; bm_sv=F510CB9DC578EFCA6130FE35AB9F37F7~YAAQJDsvF+ebAyeCAQAAWsivPBDXZe4DzOTZ4M5CIqBkbSZ96T5LB1wNswAj2P5xgVci7Xv9YqA8WAUS/UfYZdCGwQ6Cx8kdkfu/J+YthRtLLb+P73YL6WFcNrJH2CmjOjDmErzSQs+EFYuxFMg9ujSXs6uu0jUj2EYisSCjpHo4mnPA7dB1ptjoa6FvhZsQBLOByPrKNLRe3I8tkn4B/nDXzF4mcwKG8oe3Qo0bDqsZDgwkXCzcwumqmF80PkWrwTU=~1; forterToken=3976839465ce40918d1dc4709992da52_1658875527651__UDF43_9ck; _clsk=1ozixrb|1658875528363|9|0|h.clarity.ms/collect; ai_session=KGi2odv5q0PEkickRczorE|1658874664998|1658875559666',
            "origin": "https://www.stubhub.com",
            "referer": "https://www.stubhub.com/hot-wheels-monster-trucks-live-austin-tickets-8-13-2022/event/105285686/?quantity=2",
            "request-context": "appId=cid-v1:d2ec73bc-3fa1-4bd1-8c0c-c27c69bb4833",
            "request-id": "|794e5ec61f42482b8bd11583e17c6340.dc51e03918a24a00",
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "traceparent": "00-794e5ec61f42482b8bd11583e17c6340-dc51e03918a24a00-01",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        }

        json_data = {
            "ShowAllTickets": True,
            "HideDuplicateTicketsV2": False,
            "Quantity": quantity,
            "PageVisitId": "2cb28cde9b7a4c8cb2b8d1bb2e4fa3e7",
            "PageSize": page_size,
            "CurrentPage": current_page,
            "SortBy": "NEWPRICE",
            "Sections": "",
            "TicketClasses": "",
            "ListingNotes": "",
            "TicketTypeGroups": "",
            "PriceRange": "0,100",
            "InstantDelivery": False,
            "EstimatedFees": False,
            "BetterValueTickets": False,
            "Method": "IndexSh",
        }

        # 'https://www.stubhub.com/hot-wheels-monster-trucks-live-austin-tickets-8-13-2022/event/105285686/'
        url = f"https://www.stubhub.com/{endpoint}"
        response = requests.post(url, cookies=cookies, headers=headers, json=json_data)
        data = response.json()
        # print(data.keys())
        print(f"showing {len(data['items'])} of {data['totalCount']} items")
        return pd.DataFrame(data["items"])
