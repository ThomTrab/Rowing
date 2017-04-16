#!/usr/bin/env python
import time
import math
from threading import Timer
import pm2

class Chrono(object):

    diff_pause = 0
    value = ''

    def __init__(self, interval=1, *args, **kwargs):
        ''' Initialize Timer
        @param interval : refresh frequency in seconds
        @self timer : timer call main function every self interval
        @self is_runing : flag use to track Chrono execution
        '''
        self._timer     = None
        self.interval   = interval
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
        self.value = '{:02d}{:02d}'.format(mins, secs)

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
    timer = Chrono()
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
           PM2.clear()
        elif input == 'all':
           PM2.display_all()
        input = raw_input('Command:')


if __name__ == '__main__':
    main()
