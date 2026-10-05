import subprocess
subprocess.call("cls",shell=True)
import numpy as np

fasl_irani=np.array([["farvardin","ordibehesht","khordad"],["tir","mordad","shahrivar"],["mehr","aban","azar"],["dey","bahman","esfand"]])
print(fasl_irani)

fasl_latin=np.array([["apr","may","jun"],["jul","aug","sep",],["oct","nov","dec"],["jan","feb","mar"]])
print(fasl_latin)
while True:
    q=input("Enter Month :")
    for i in range(len(fasl_irani)):
        for j in range(len(fasl_irani[0])):
            if fasl_irani[i,j]==q:
                print(fasl_latin[i,j])