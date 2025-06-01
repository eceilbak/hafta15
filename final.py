import threading

# Define a function to run in a thread
def coder(x,y,z,c):
    print(f'Coder ID: k={k}, l={l}, m={m}, no={c}')

# Create and start 5 threads
threads = []
count=0
for k in range(3):
    for l in range(3):
        for m in range(3):
            count +=1
            t = threading.Thread(target=coder, args=(k,l,m, count))
            threads.append(t)
            t.start()
