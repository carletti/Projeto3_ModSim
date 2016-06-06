# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import odeint 
import math 
 
 
def derivadas(I, t): 
    # Parâmetros flutuantes 
    A = 165.5 # Área da asa (cm2) 
    m = 4.5 # massa do avião (g) 
    vx = I[2] # Velocidade em x 
    vy = I[3] # Velocidade em y 
    # Parâmetros fixos    
    g = 9.8 # Gravidade 
    ro =  1.2 
    Cd0 = 0.15 # Coeficiente de arrasto quando o ângulo de ataque é zero 
    e = 0.7 # Fator de eficiência da asa 
    S = 3 # Largura da asa (cm) 
    # Funções 
    v = ((vx**2)+(vy**2))**(1/2) # Velocidade 
    Ce = 2*math.pi*Cd0 # Coeficiente de empuxo 
    Cdi = (Ce**2)/(math.pi*((S**2)/A)*e) # Coenficiente de ???? 
    Ca = Cd0*Cdi # Coeficiente de atrito 
    E = (Ce*ro*(v**2)*A)/2 # Empuxo 
    Fres = (Ca*ro*(v**2)*A)/2 # Força de resistência do ar  
    P = m*g # Força peso 
    Ex = E*(vx/v) 
    Ey = E*(vy/v) 
    Fresx = Fres*(vx/((vx**2)+(vy**2)**(1/2))) 
    Fresy = Fres*(vy/((vx**2)+(vy**2)**(1/2))) 
    # Diferenciais  
    dxdt = vx 
    dydt = vy 
    dvxdt = (Ex - Fresx)/m 
    dvydt = (Ey + Fresy - P)/m 
    return [dxdt, dydt, dvxdt, dvydt] 


# Condições iniciais     
x0 = 0 #cm
y0 = 40 #cm 
vx0 = 316 #cm/s
vy0 = 316 #cm/s  
I0 = [x0, y0, vx0, vy0] 

 
# Lista tempo 
t = np.arange(0,10,0.0000001) 

 
# Chamada da odeint 
r = odeint(derivadas, I0, t) 

 
# Plotagem dos gráficos 
# Gráfico posição X 
plt.plot(t, r[:, 0]) 
#plt.ScalarFormatter(0, 0.00000001) 
plt.legend(loc = 'upper right') 
plt.ylabel('Distância x (cm)') 
plt.xlabel('Tempo (dias)') 
plt.title(r'Posição em X') 
plt.grid(True) 
plt.show
# Gráfico posição Y 
plt.plot(t, r[:, 1]) 
#plt.ScalarFormatter(0, 0.00000001) 
plt.legend(loc = 'upper right') 
plt.ylabel('Distância y (cm)') 
plt.xlabel('Tempo (dias)') 
plt.title(r'Posição em Y') 
plt.grid(True) 
plt.show
# Gráfico Velocidade X 
plt.plot(t, r[:, 2]) 
#plt.ScalarFormatter(0, 0.00000001) 
plt.legend(loc = 'upper right') 
plt.ylabel('Velocidade em x (cm/s)') 
plt.xlabel('Tempo (dias)') 
plt.title(r'Velocidade X') 
plt.grid(True) 
plt.show
# Gráfico Velocidade y 
plt.plot(t, r[:, 3]) 
#plt.ScalarFormatter(0, 0.00000001) 
plt.legend(loc = 'upper right') 
plt.ylabel('Velocidade em y (cm/s)') 
plt.xlabel('Tempo (dias)') 
plt.title(r'Velocidade Y') 
plt.grid(True) 
plt.show

