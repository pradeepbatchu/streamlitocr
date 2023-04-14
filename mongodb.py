from pymongo import MongoClient


def insert(mongo_collection: str, raw_data_from_file: str) -> None:
    try:
        client = MongoClient("mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase")
        db = client["OCR"]
        collection = db[mongo_collection]
        collection.insert_one(raw_data_from_file)
        client.close()
        print("Insert Success ✅")
    except Exception as err:
        print(f"Error something went wrong {err}")
