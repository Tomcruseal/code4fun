from scipy.stats import norm 

def calculusing(x,p):
    m=(x+0.5-25.0*p)/((25.0*p*(1-p))**0.5)
    return norm(m)

print calculusing(20.0,0.5)
