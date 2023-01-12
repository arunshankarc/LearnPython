import time
import threading
from SleepyWorker import SleepyWorker
from SquaredSumWorker import SquaredSumWorker 

def main():
     
    start = time.time()
    current_worker = []
    
    for i in range(5):
        square_sum_worker = SquaredSumWorker(n=(i+1)*1000000)
        current_worker.append(square_sum_worker)
    
    for i in range(len(current_worker)):
        current_worker[i].join() 
    
    print(f"Time taken to complete calculation = {round(time.time() - start, 1)}")
    
    start = time.time()
    current_worker = []
    for seconds in range(6):
        sleepy_worker = SleepyWorker(seconds=seconds)
        current_worker.append(sleepy_worker)
    
    for i in range(len(current_worker)):
        current_worker[i].join() 
    print(f"Time taken to complete sleeping = {round(time.time() - start, 1)}")

if __name__ == "__main__":
    main()
        
    