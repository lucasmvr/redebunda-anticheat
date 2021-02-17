from PIL import ImageGrab
from datetime import datetime
import time, multiprocessing, os, base64

from services.api import Api

class ScreenCapture(multiprocessing.Process):
    def __init__(self):
        super().__init__()

    def snapshot(self):
        created = False
        try:
            snapshot = ImageGrab.grab(all_screens=True)
            filename = './teste/{}_pego_no_pulo.png'.format(datetime.now().strftime('%Y-%m-%sT%H:%M:%S'))
            snapshot.save(filename)

            image = None
            with open(filename, 'rb') as t:
                image = t.read()

            Api().sendScreenshot({
                'nickname': os.environ['redebunda-anticheat-nickname'],
                'bundaId': os.environ['redebunda-anticheat-bundaId'],
                'codigo': os.environ['redebunda-anticheat-codigo'],
            }, image)
        except Exception as e:
            print(e)
        finally:
            if created:
                # todo deletar arquivo
                pass

    def run(self):
        while True:
            self.snapshot()
            time.sleep(120)