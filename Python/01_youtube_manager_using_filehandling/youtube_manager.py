import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("*" * 70)

def add_video(videos):
    name = input("Enter Video name: ")
    time = input("Enter Video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be update: "))

    if 1<=index<=len(videos):
        name = input("Enter video name: ")
        time = input("Enter video time: ")

        u_name = name if name else videos[index - 1]['name']
        u_time = time if time else videos[index - 1]['time']

        videos[index-1] = {'name': u_name, 'time': u_time}
        save_data_helper(videos)
    else:
        print("Invalid Index..!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be delete: "))

    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid Index..!")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube Video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice : ")
        # print("videos:",videos)

        match choice:
            case '1':
                list_all_videos(videos)

            case '2':
                add_video(videos)

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)

            case '5':
                break

            case _:
                print("Invalid Choice..!")

if __name__ == "__main__":
    main()