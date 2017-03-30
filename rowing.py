#!/usr/bin/env python
import time
import math
from threading import Timer, Event, Thread
import pm2

class Chrono(object):

    diff_pause = 0

    def __init__(self, display, interval=1, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.display    = display
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
#        self.start()

    def _run(self):
        self.is_running = False
        self.loop()
        #self.function(*self.args, **self.kwargs)
        self.diff = int(round((time.time() - self.start_time))) + self.diff_pause
        mins, secs = divmod(self.diff, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        self.display.display(place = "upper", value = timeformat)

    def loop(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def start(self):
        self.start_time = time.time()
        self.loop()

    def stop(self):
        self._timer.cancel()
        self.is_running = False
        self.diff_pause = 0

    def pause(self):
        self._timer.cancel()
        self.is_running = False
        self.diff_pause = self.diff


def main():
    PM2 = pm2.PM2()
    timer = Chrono(display=PM2)
    input = raw_input('Command:')
    while input != 'q':
        if input == 'start':
           print("Start chrono")
           timer.start()
        elif input == 'stop':
           print("Stop chrono")
           timer.stop()
        elif input == 'pause':
           print("Pause chrono")
           timer.pause()
        elif input == 'clear':
           PM2.clear_screen()
        elif input == 'all':
           PM2.display_all()
        input = raw_input('Command:')


if __name__ == '__main__':
    main()
