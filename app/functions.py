from celery import Celery
import requests
import datetime
from sec_api import QueryApi

# def fetch_13f_filings():
#     # Calculate today's date and the date from two days ago
#     end_date = datetime.date.today()
#     start_date = end_date - datetime.timedelta(days=2)

#     # API endpoint
#     url = "https://api.sec-api.io"

#     # Define the payload for the POST request
#     data = {
#         "query": {
#             "query_string": {
#                 "query": "formType:\"13F-HR\" AND filedAt:[{} TO {}]".format(start_date, end_date)
#             }
#         },
#         "sort":[{"filedAt":{"order":"desc"}}]
#     }

#     # Your API Key (Replace 'YOUR_API_KEY' with your actual API key)
#     headers = {
#         "Authorization": "Bearer cdafa1286e4c879452fa735831299488afa7993764f089623a6493a4bf10ffa2",
#         "Content-Type": "application/json"
#     }

#     # Send the POST request
#     response = requests.post(url, json=data, headers=headers)

#     # Check response
#     filings=""
#     if response.status_code == 200:
#         filings = response.json()
#         # Process the filings as needed
#     else:
#         print("Error:", response.status_code, response.text)
#     print(filings)
#     return filings  # Or return any other appropriate result

queryApi=QueryApi(api_key="cdafa1286e4c879452fa735831299488afa7993764f089623a6493a4bf10ffa2")

def fetch_13f_filings():
    print(f"Getting next 13F batch starting ")
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=2)

    query={
        "query":{
            "query_string":{
                # "query":"formType:\"13F-HR\" AND NOT formtype:\"13F=HR/A\" AND periodOfReport:\"2021-06-30\""
                "query":"formType:\"13F-HR\" AND filedAt:[{} TO {}]".format(start_date, end_date)
                
            }
        },
        "sort":[{"filedAt":{"order":"desc"}}]
    }
    response=queryApi.get_filings(query)
    return response['filings']