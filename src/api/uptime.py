# uptime.py

# Ported by from original npm package (@mitchallen/uptime)

import time

class Uptime:
    def __init__(self):
        self.start_time = time.monotonic()

    def toHHMMSS(self):
        def pad(s):
            return ('0' if s < 10 else '') + str(s)

        t = time.monotonic() - self.start_time

        hours = int(t // (60 * 60))
        minutes = int(t % (60 * 60) // 60)
        seconds = int(t % 60)

        return pad(hours) + ':' + pad(minutes) + ':' + pad(seconds)
