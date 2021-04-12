import Minimax_vs_Random
import time

start = time.time()
win = 0
loss = 0
draw = 0

for i in range(0, 10):
    output = Minimax_vs_Random.main()
    print(output)

    if output == ('Bot wins!'):
        win = win + 1
    if output == ('Bot loses!'):
        loss = loss + 1
    if output == ('Draw!'):
        draw = draw + 1


print("wins"+str(win))
print("loses"+str(loss))
print("draws"+str(draw))
print('R vs R took', time.time()-start, "seconds")
