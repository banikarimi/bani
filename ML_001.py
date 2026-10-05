import subprocess
subprocess.call("cls",shell=True)
import numpy as np

info_age={}
while True:
    age=int(input("Enter Age : "))
    if age<1:
        break
    elif age<18:
        model=1
    elif age<40:
        model=2
    elif age<60:
        model=3
    else:
        model=4
    info_age[age]=model
age=[]
model=[]
for key in info_age:
    age.append(key)
    w=info_age[key]
    model.append(w)
import matplotlib.pyplot as plt
age=np.array(age)
model=np.array(model)
smooth_age = np.linspace(1, 100, 100)
smooth_model = np.interp(smooth_age, age, model)

plt.scatter(smooth_age, smooth_model, color="blue")
plt.xlabel("Age Model")
plt.ylabel("Model")
plt.title("Age vs Model")
plt.show()
