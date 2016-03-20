def quicksort(L):  
    if len(L) <= 1: return L  
    return quicksort([l for l in L[1:] if l < L[0]]) + [L[0]] + quicksort([r for r in L[1:] if r >= L[0]])  
def getKth(k);
	return L[k]