import math
def transporte_logitudinal_arena(p,g,k,ps,n,hb,a,K=0.77):
    # p-Densidad del Mar  1025
    # g aceleracion gravitatoria 9.8 
    # k- Inidice de Rompiente 0.78
    # ps- Densidad Arena 2650
    # n -Coeficiente de porocidad  0.4
    # hb altura 0.29
    # a- angulo de Rompiente 20
    # K- Constante de Komar e Inman 0.77
    
    p= float (p)
    g=float(g)
    k=float(k)
    ps=float(ps)
    n=float(n)
    hb=float(hb)
    a=float(a)
    K=float(K)
    
    Q= K * ( (p * math.sqrt(g))/ ((16 * math.sqrt(k) )* (ps-p)*(1-n)) )* math.sqrt(math.pow(hb,5))* math.sin(2*a)
    return Q
