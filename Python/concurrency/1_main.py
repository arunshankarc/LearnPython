from time import sleep
import time
import threading


def calculate_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i*2
    print(sum_squares)


def sleep_a_little(seconds):
    sleep(seconds)


def main():
    start_time = time.time()
    current_threads_calc = []
    # daemon=True in threading.Thread(target=calculate_sum_squares, args=((i+1)*1000000,)) 
    # will complete immediately after main thread finishes.
    for i in range(10):
        t = threading.Thread(target=calculate_sum_squares, args=((i+1)*1000000,), daemon=False)
        # calculate_sum_squares((i+1)*1000000)
        t.start()
        current_threads_calc.append(t)
    for thread in current_threads_calc:
        thread.join()
    print(f"calculate sum squares took {round(time.time() - start_time, 4)}")
    
    start_time = time.time()
    current_threads_sleep = []
    for i in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(i,))
        # sleep_a_little(i)
        t.start()
        current_threads_sleep.append(t)
    for thread in current_threads_sleep:
        thread.join()
    print(f"sleep_a_little took {round(time.time() - start_time, 4)}")


if __name__ == "__main__":
    main()
