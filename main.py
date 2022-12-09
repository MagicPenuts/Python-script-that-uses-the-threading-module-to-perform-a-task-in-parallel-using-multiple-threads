import threading

def task(arg):
    # Perform some task here
    pass

# Create a thread pool with 4 threads
thread_pool = []
for i in range(4):
    t = threading.Thread(target=task, args=(i,))
    thread_pool.append(t)

# Start the threads
for thread in thread_pool:
    thread.start()

# Wait for all threads to finish
for thread in thread_pool:
    thread.join()