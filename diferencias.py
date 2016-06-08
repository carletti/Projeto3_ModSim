# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import odeint 
import math 
#%matplolib inline
 
 
def derivadas(I, t): 
    # Parâmetros flutuantes 
    A = 0.01655 # Área da asa (cm2) 
    m = 0.0045 # massa do avião (g) 
#    x = I[0] # posição em x
#    y = I[1] # posição em y
    vx = I[2] # Velocidade em x 
    vy = I[3] # Velocidade em y
    a = I[4] # ângulo do avião em relação ao eixo X
    o = I[5] # Velocidade ângular
    
    # Parâmetros fixos    
    g = 9.8 # Gravidade 
    ro =  1.2 # Densidade do ar 
    Cd0 = 0.15 # Coeficiente de arrasto quando o ângulo de ataque é zero 
    e = 0.7 # Fator de eficiência da asa 
    S = 0.03 # Largura da asa (cm) 
    d = 0.10 # Distânciaentre o centro de massa e onde se aplica o impuxo (cm)
    
    # Funções 
    v = ((vx**2)+(vy**2))**(1/2) # Velocidade 
    print(v)
    Ce = 2*math.pi*Cd0 # Coeficiente de empuxo 
    Cdi = (Ce**2)/(math.pi*((S**2)/A)*e) # Coenficiente de ???? 
    Ca = Cd0+Cdi # Coeficiente de atrito 
    E = (Ce*ro*(v**2)*A)/2 # Empuxo 
    Fres = (Ca*ro*(v**2)*A)/2 # Força de resistência do ar  
    P = m*g # Força peso 
    i = (d*m)/3 # Momento de inércia
    Tr = E*d #torque
    Ex = E*math.cos(a) # Empuxo em x
    Ey = E*math.sin(a) # Empuxo em y
    Fresx = Fres*math.cos(a) # Força de resistência do ar em x
    Fresy = Fres*math.sin(a) # Foça de resistênia do as em y
    
    # Diferenciais 
    dxdt = vx 
    dydt = vy 
    dvxdt = (-Ex - Fresx)/m 
    dvydt = (Ey + Fresy - P)/m 
    dadt = o
    dodt = i/Tr
    return [dxdt, dydt, dvxdt, dvydt, dadt, dodt] 

# Condições iniciais     
x0 = 0 #cm
y0 = 0.7 #cm 
vx0 = 3.16 #m/s
vy0 = 3.16 #m/s
a0 = np.pi/4 # Ângulo de lançamento
o0 = 0 # Velocidade angular 
I0 = [x0, y0, vx0, vy0, a0, o0] 
 
# Lista tempo 
t = np.arange(0,5,0.01) 
 
# Chamada da odeint 
r = odeint(derivadas, I0, t) 
print(r[:,0])
#print(r[:,1])
#print(r[:,2])
#print(r[:,3])
#print(r[:,4])
#print(r[:,5])

# Plotagem dos gráficos 

# Gráfico posição X 

plt.plot(t, r[:, 0]) 
#plt.ScalarFormatter(0, 0.00000001) 
plt.legend(loc = 'upper right') 
plt.ylabel('Distância x (m)') 
plt.xlabel('Tempo (segundos)') 
plt.title(r'Posição em X') 
plt.grid(True) 
plt.show()

# Gráfico posição Y 
plt.plot(t, r[:, 1]) 
#plt.ScalarFormatter(0, 0.00000001) 
plt.legend(loc = 'upper right') 
plt.ylabel('Distância y (m)') 
plt.xlabel('Tempo (segundos)') 
plt.title(r'Posição em Y') 
plt.grid(True) 
plt.show()

# Gráfico Velocidade X 
plt.plot(t, r[:, 2]) 
#plt.ScalarFormatter(0, 0.00000001) 
plt.legend(loc = 'upper right') 
plt.ylabel('Velocidade em x (m/s)') 
plt.xlabel('Tempo (segundos)') 
plt.title(r'Velocidade X') 
plt.grid(True) 
plt.show()

# Gráfico Velocidade y 
plt.plot(t, r[:, 3]) 
#plt.ScalarFormatter(0, 0.00000001) 
plt.legend(loc = 'upper right') 
plt.ylabel('Velocidade em y (m/s)') 
plt.xlabel('Tempo (segundos)') 
plt.title(r'Velocidade Y') 
plt.grid(True) 
plt.show()

# Testes
plt.plot(t, r[:4])
plt.show()
plt.plot(t, r[:5])
plt.show()
plt.plot(r[:,0], r[:1])
plt.show()

