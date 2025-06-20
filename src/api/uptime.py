# uptime.py

# Ported by from original npm package (@mitchallen/uptime)

import time


class Uptime:
    def __init__(self) -> None:
        self.start_time = time.monotonic()

    def toHHMMSS(self) -> str:
        def pad(s: int) -> str:
            return ("0" if s < 10 else "") + str(s)

        t = time.monotonic() - self.start_time

        hours: int = int(t // (60 * 60))
        minutes: int = int(t % (60 * 60) // 60)
        seconds: int = int(t % 60)

        return pad(hours) + ":" + pad(minutes) + ":" + pad(seconds)
