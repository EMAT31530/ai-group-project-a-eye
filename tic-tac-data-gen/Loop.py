import new
import time

start = time.time()
for i in range(0, 5):
    output = new.main()
    print(output)
print('It took', time.time()-start, "seconds")

