import threading
from time import sleep

class SleepyWorker(threading.Thread):
    def __init__(self, seconds: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self._seconds = seconds
        self.start()
    
    def _sleep_a_little(self):
        sleep(self._seconds)
        
    def run(self) -> None:
        self._sleep_a_little()