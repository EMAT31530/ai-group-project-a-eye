import Random_vs_Random
import time
import matplotlib.pyplot as plt
import numpy as np

start = time.time()
win = 0
loss = 0
draw = 0

for i in range(0, 1000):
    output = Random_vs_Random.main()
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

labels = ['Randon vs Random player']
win = [win]
draw = [draw]
loss = [loss]

x = np.arange(len(labels))
width = 0.3  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - (2*(width/3)), win, width, label='Win')
rects2 = ax.bar(x - width/3, draw, width, label='Draw')
rects3 = ax.bar(x + width/3, loss, width, label='Lose')

ax.set_ylabel('No. of Games')
ax.set_title('Outcome of game of Random vs Random players')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()
plt.show()