"""
---------
loader.py
---------

A minimal code to store data in MongoDB
"""
import json
from pymongo import MongoClient


def main():
    """The main script"""
    client = MongoClient('localhost', 27017)
    airbnb = client["airbnb"]
    sample_data = airbnb["sample_data"]

    with open("airbnb.json", "r") as f_in:
        data = json.loads(f_in)

    ids = sample_data.insert_many(data)
    assert len(ids) > 0


if __name__ == "__main__":
    main()
