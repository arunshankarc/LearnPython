import time
import threading

def calculate_sum_squares(n):
    sum_squares = 0 
    for i in range(n):
        sum_squares += i ** 2
    print(sum_squares)


def sleep_little(seconds):
    time.sleep(seconds)
    

def main():
    # start = time.time()
    # for i in range(5):
    #     calculate_sum_squares(i*1000000)
        
    # print(f"Time taken to complete calculation w/o thread= {round(time.time() - start, 1)}")
    
    # start = time.time()
    # for i in range(6):
    #     sleep_little(i)
        
    # print(f"Time taken to complete sleep w/o thread= {round(time.time() - start, 1)}")
     
    start = time.time()
    current_thread = []
    for i in range(5):
        thread = threading.Thread(target=calculate_sum_squares, args=(i*1000000,))
        thread.start()
        current_thread.append(thread)
    
    for i in range(len(current_thread)):
        current_thread[i].join() 
    
    print(f"Time taken to complete calculation = {round(time.time() - start, 1)}")
    
    start = time.time()
    current_thread = []
    for i in range(6):
        thread = threading.Thread(target=sleep_little, args=(i,))
        thread.start()
        current_thread.append(thread)
    
    for i in range(len(current_thread)):
        current_thread[i].join() 
    print(f"Time taken to complete sleeping = {round(time.time() - start, 1)}")

if __name__ == "__main__":
    main()
        
    