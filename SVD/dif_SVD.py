import matplotlib
import numpy as np

A = matplotlib.image.imread('/content/1984.jpeg')
A = A[:,:,0]

U, s, Vt = np.linalg.svd(A, full_matrices = False, compute_uv = True )
sigma = np.diag(s)

def different_Ks(U, sigma, Vh, k):
    """
    U = matrix 
    sigma = matrix
    Vh = matrix
    k = array
    """
    #U = np.matrix(U[:,:2])
    #sig = np.matrix(sigma[:2,:2])
    #Vt = np.matrix(Vt[:2,:])
    Resultados = []
    for i in range(len(k)):
        u = np.matrix(U[:,:k[i]])
        s = np.matrix(sigma[:k[i], :k[i]])
        vt = np.matrix(Vh[:k[i],:])
        result = np.dot(u, np.dot(s, vt))
        Resultados.append(result)
        
    return Resultados


k = [1, 2, 3, 5, 10, 50, 100, 150]
results = different_Ks(U, sigma, Vt, k)
