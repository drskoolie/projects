## Part 0: Initialization
import numpy as np
from statistics import NormalDist

x = np.arange(0, 5, 0.05)
y = np.zeros(len(x))

for idx, value in enumerate(x):
    y[idx] = 1 - NormalDist(mu=0, sigma=1).cdf(value)

## Part 1: Latex Document SetUp
rows = 20
cols = 5

string = r"""\documentclass{article}
\usepackage{amsmath}

\begin{document}
\thispagestyle{empty}

\begin{center}
  {\small\textbf{Values of Q(x) for 0 $\le$ x $\le$ 5}}
\end{center}

\begin{center}
"""

string += r"\begin{tabular}{|"
string += "cc||" * cols
string = string[:-1]

string += "}\n\n\t\hline\n"


string += "\t "
for col in range(cols):
    string += "$Q$ & $Q(x)$ & "

string = string[:-2]
string += "\\\ \hline \n"

for row in range(rows):
    string += "\t "
    for col in range(cols):
        string += f"{x[col + row*cols]:.2f} & "

    string = string[:-2]
    string += " \\\ \n"

string += r"""
\end{tabular}
\end{center}

\end{document}
"""

print(string)
with open("qfunc.tex", "w") as f:
    f.write(string)
