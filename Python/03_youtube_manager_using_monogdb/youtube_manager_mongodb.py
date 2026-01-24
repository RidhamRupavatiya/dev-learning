from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URL = os.getenv('MONGO_URL')

# Note:- tlsAllowInvalidCertificates for handle SSL Certificate for localhost only.
client = MongoClient(MONGO_URL, tlsAllowInvalidCertificates=True)
db = client["ytmanager"]
video_collection = db["videos"]

def list_videos():
    print('\n', '*' * 50)
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name:- {video['name']}, Duration:- {video['time']}")
    print('\n','*' * 50)

def add_videos(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_videos(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_videos(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})

def main():
    while True:
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter Video name: ")
            time = input("Enter Video time: ")
            add_videos(name, time)
        elif choice == '3':
            video_id = input("Enter Video ID to Update: ")
            name = input("Enter Video name: ")
            time = input("Enter Video time: ")
            update_videos(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter Video ID to Delete: ")
            delete_videos(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice..!")

if __name__ == "__main__":
    main()