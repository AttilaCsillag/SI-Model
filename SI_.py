import matplotlib.pyplot as plt

# s+i=n
susp=150000 #nr sussceptiblie 
inf=1    #nr infected
k=0.3135   #konstanta de tranmitere
t=0
tf=150
i=1
dt=0.05
#initializare lista
vsusp=[] 
vinf=[]
vt=[]

while t<=tf:
    #definire ecuatii diferentiale
     dsuspdt=-k*susp
     dinfdt=k*susp
     #Euler
     susp+=dsuspdt*dt
     inf+=dinfdt*dt
     #memorare vectori
     vsusp.append(susp)
     vinf.append(inf)
     vt.append(t)
     #incrementare
     i+=1
     t+=dt

plt.plot(vt, vsusp)  
plt.plot(vt, vinf)
plt.xlabel("Timp [zile]")
plt.ylabel("Nr-suspset,Nr-infected")
plt.grid()
plt.show()