import Minimax
import time
import matplotlib.pyplot as plt
import numpy as np

start = time.time()
win = 0
loss = 0
draw = 0

for i in range(0, 1000):
    output = Minimax_vs_Minimax2.main()
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
print('MM vs MM took', time.time()-start, "seconds")

labels = ['Minimax vs Minimax player']
win = [win]
draw = [draw]

x = np.arange(len(labels))
width = 0.3  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - width/2, win, width, label='Win')
rects2 = ax.bar(x, draw, width, label='Draw')
rects3 = ax.bar(x + width/2, loss, width, label='Lose')

ax.set_ylabel('No. of Games')
ax.set_title('Outcome of games of an Intelligent (Minimax) vs Intelligent (Minimax) player')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.show()
