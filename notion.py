import json
import requests

class NotionClient:
    def __init__(self, token, db) -> None:
        self.db = db
        self.headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def get_db(self):
        get_db_url = f"https://api.notion.com/v1/databases/{self.db}"
        res = requests.get(get_db_url, headers=self.headers)
        print(res.text)
        return res

    # create, read, update
    def create_page(self, desc, date, status):
        create_url = "https://api.notion.com/v1/pages"

        data = {
        "parent": { "database_id": self.db },
        "properties": {
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": desc
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                            "start": date,
                            "end": None
                        }
            },
            "Status": {
                "id": "DjuQ",
                "type": "status",
                "status": {
                    "id": "3afa8183-c6f6-4b3b-b24a-171cd37e99b7",
                    "name": "Not started",
                    "color": "default"
                }
            }
        }}

        data = json.dumps(data)
        res = requests.post(create_url, headers=self.headers, data=data)
        print(res.status_code, res.content)
        return res