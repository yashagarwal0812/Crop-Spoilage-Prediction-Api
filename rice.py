temperature = 40
moisture_content = 20
pesticide = 0
light = 2
oxygen = 10




T = 0;
if temperature < 0:
    T = 1;
elif temperature < 15:
    T = 5
elif temperature < 25:
    T = 8
elif temperature < 35:
    T = 13
else: 
    T = 18


P = 0;
if pesticide == 0:
    P = 9


L = 0;
if light == 2:
    L = 8
elif light == 1:
    L = 4
else:
    L = 1


O = 0;
if oxygen<1:
    O = 1
elif oxygen<1:
    O = 2
elif oxygen<5:
    O = 5
else:
    O = 9


M = 0;
if moisture_content<12:
    M = 2
elif moisture_content <13:
    M = 3
elif moisture_content <15:
    M = 5
elif moisture_content <16:
    M = 6
elif moisture_content <18:
    M = 9
else:
    M = 14




spoilage = 10 + M + O + T + L + P
print(spoilage)