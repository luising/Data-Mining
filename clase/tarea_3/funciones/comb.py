"""C."""
import itertools


ele = "QWERTYUIOPLKJHGFDSAZXCVBNM!#$%&/"
C = itertools.permutations(ele, 4)
TOTAL = []
for i in C:
    D = "".join(i)
    TOTAL.append(i)

print(TOTAL)
