from PIL import ImageGrab


class ScreenCapture():
    def __init__(self):
        snapshot = ImageGrab.grab(all_screens=True)
        # snapshot.convert('RGBA')
        snapshot.save('./teste/snapshot.png')