import Random_vs_Random
import new
import time

start = time.time()
win = 0
loss = 0
draw = 0

for i in range(0, 100):
    output = Random_vs_Random.main()
    print(output)

    if Random_vs_Random.main() == ('Bot wins!'):
        win = win + 1
    if Random_vs_Random.main() == ('Bot loses!'):
        loss = loss + 1
    if Random_vs_Random.main() == ('Draw!'):
        draw = draw + 1


print("wins"+str(win))
print("loses"+str(loss))
print("draws"+str(draw))
print('R vs R took', time.time()-start, "seconds")
