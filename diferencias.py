# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import math

def derivadas(I, t):
    # Parâmetros flutuantes
    t =  # Ângulo de ataque
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
    Ce = 2*math.pi*t # Coeficiente de empuxo
    Cdi = (Ce**2)/(math.pi*((S**2)/A)*e) # Coenficiente de ????
    Ca = Cd0*Cdi # Coeficiente de atrito
    E = (Ce*ro*(v**2)*A)/2 # Empuxo
    Fres = (Ca*ro*(v**2)*A)/2 # Força de resistência do ar 
    P = m*g # Força peso
    Ex = E*(Vx/((Vx**2)+(Vy**2)**(1/2))
    Ey = E*(Vy/((Vx**2)+(Vy**2)**(1/2))
    Fresx = Fres*(Vx/((Vx**2)+(Vy**2)**(1/2))
    Fresy = Fres*(Vx/((Vx**2)+(Vy**2)**(1/2))
    # Diferenciais 
    dxdt = vx
    dydt = vy
    dvxdt = (Ex - Fresx)/m
    dvydt = (Ey + Fresy - P)/m
    return [dxdt, dydt, dvxdt, dvydt]

# Condições iniciais    
x0 = 0
y0 = 0
vx0 = 
vy0 =    
I0 = [x0, y0, vx0, yv0]

# Lista tempo
t = np.arange(0,10,0.0000001)

# Chamada da odeint
r = odeint(derivadas, I0, t)

# Plotagem dos gráficos
