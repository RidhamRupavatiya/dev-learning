import sqlite3

conn = sqlite3.connect('youtube_manager.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
 ''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    print('\n', '*' * 50)
    if not videos:
        print("No data found.")
    else:
        for video in videos:
            print(f"{video[0]}. Video name: {video[1]}, duration: {video[2]}")
    print('\n','*' * 50)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    conn.commit()

def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name, new_time, video_id))
    conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()

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
            video_id = int(input("Enter Video ID to Update: "))
            name = input("Enter Video name: ")
            time = input("Enter Video time: ")
            update_videos(video_id, name, time)
        elif choice == '4':
            video_id = int(input("Enter Video ID to Delete: "))
            delete_videos(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice..!")
    
    conn.close()

if __name__ == "__main__":
    main()