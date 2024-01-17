from matplotlib import pyplot as plt
import numpy as np

def recaman(max_terms):
    seq=np.empty(max_terms)
    exist = set([])
    n = 0 
    a = 0
    while n < max_terms:
        diff=a-n
        if diff > 0 and diff not in exist:
            a = diff
        else:
            a = a + n
        seq[n]=a
        exist.add(a)
        n += 1
    return seq
seq = recaman(20)
for i in range(1, len(seq)):
    h = (seq[i] + seq[i-1])/2
    r = abs((seq[i] - seq[i-1]))/2
    x = np.linspace(seq[i], seq[i-1], 40)
    y = (-1)**i * np.sqrt(r**2 - (x-h)**2)
    plt.plot(x, y)

plt.savefig('recaman.pdf')
plt.show()