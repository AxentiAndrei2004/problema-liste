with open ('input.txt', 'r') as f:
    z=list(eval(f.readline()))
with open ('output.txt', 'w') as f:
    f.write('Lista 1' + str(z) + '\n')
    a=sorted(z)
    f.write('Lista 2' + str(a) + '\n')
    a.sort(reverse=True)
    f.write('Lista 3' + str(z) + '\n')
    f.write('Numarul de caractere' +str(len(a)) + '\n')
    f.write('Elementul MAXIM' + str(max(a)) + '\n')
    f.write('Elementul MINIM' + str(min(a))+ '\n')
    z.extend([111])
    f.write('Lista 4' + str(z) + '\n')
    z[1]=222
    f.write('Lista finala' + str(z)+ '\n')