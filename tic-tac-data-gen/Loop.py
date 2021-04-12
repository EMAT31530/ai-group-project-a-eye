import Random_vs_Random
import new
import time

start = time.time()
for i in range(0, 100):
    output = Random_vs_Random.main()
    print(output)
print('R vs R took', time.time()-start, "seconds")
