import matplotlib.pyplot as plt

# s+i=n
susp=150000 #nr susceptible 
inf=1    #nr infected
k=0.3135   #transmission contant
t=0
tf=150
i=1
dt=0.05
#initialise list
vsusp=[] 
vinf=[]
vt=[]

while t<=tf:
    #defining differential ecuations
     dsuspdt=-k*susp
     dinfdt=k*susp
     #Euler Integrator
     susp+=dsuspdt*dt
     inf+=dinfdt*dt
     #saving calculation results to list
     vsusp.append(susp)
     vinf.append(inf)
     vt.append(t)
     #increment
     i+=1
     t+=dt

plt.plot(vt, vsusp)  
plt.plot(vt, vinf)
plt.xlabel("Time [days]")
plt.ylabel("Nr-suspected,Nr-infected")
plt.grid()
plt.show()
