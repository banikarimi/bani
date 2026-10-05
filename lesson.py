import subprocess
subprocess.call("cls",shell=True)
import numpy as np

persian_teachers=np.array([["Mohamadi","Roshan","Amiri"],["Riazi","Python","varzesh"],["Tiz","Nasim","academic"]])
print(persian_teachers)

usa_teachers=np.array([["elizabet","jack","kati"],["math","Python","Sport"],["Tiz","Nasim","academic"]])
print(usa_teachers)

while True:
    q=input(" :")
    for i in range(len(persian_teachers)):
        for j in range(len(persian_teachers[0])):
            if persian_teachers[i,j]==q:
                print(usa_teachers[i,j])