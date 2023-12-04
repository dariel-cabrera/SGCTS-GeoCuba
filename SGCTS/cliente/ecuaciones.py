import math
def transporte_logitudinal_arena(p,g,k,ps,n,hb,a,K=0.77):
    # p-Densidad del Mar 
    # g aceleracion gravitatoria 
    # k- Inidice de Rompiente 
    # ps- Densidad Arena 
    # n -Coeficiente de porocidad 
    # hb altura 
    # a- angulo de Rompiente 
    # K- Constante de Komar e Inman 
    
    Q= K * ( (p * math.sqrt(g))/ ((16 * math.sqrt(k) )* (ps-p)*(1-n)) )* math.sqrt(math.pow(hb,5))* math.sin(2*a)
    return Q
