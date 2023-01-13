# Written by Eric Martin for COMP9021


dim = 128


with open('sierpinski_triangle.tex', 'w') as latex_file:
    print('\\documentclass[10pt]{article}\n'
          '\\usepackage{tikz}\n'
          '\\pagestyle{empty}\n'
          '\n'
          '\\begin{document}\n'
          '\n'
          '\\vspace*{\\fill}\n'
          '\\begin{center}\n'
          '\\begin{tikzpicture}[scale=0.047]', file=latex_file
         )
    for n in range(dim):
        for k in range(n + 1):
            if k | n == n:
                print(f'\\fill({2 * k - n},{-(2 * n)}) '
                      f'rectangle({2 * k - n + 2},{-(2 * n) + 2});',
                     file=latex_file
                     )
    print('\\end{tikzpicture}\n'
          '\\end{center}\n'
          '\\vspace*{\\fill}\n'
          '\n'
          '\\end{document}\n', file=latex_file
         )
