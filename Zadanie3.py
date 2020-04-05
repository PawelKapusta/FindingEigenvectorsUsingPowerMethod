import numpy as np

#obliczanie wartosci wlasnych
def ownValues(A, y) :
   Ay= np.dot(A,y)
   yTy=np.dot(np.transpose(y), y)
   return np.dot(np.transpose(Ay),y) / yTy

#obliczanie wektrorów wlasnych
def onwVectors(A, x):

    while True:
        Ax = np.dot(A,x)
        temporary1=ownValues(A, x) #obliczanie wartosci wlasnych
        temporary2=ownValues(A, Ax)

        if np.abs(temporary1-temporary2) < eps:
            x=Ax/np.linalg.norm(Ax)
            temporary3=ownValues(A, x)
            break
        x=Ax/np.linalg.norm(Ax)

    vectorOfOnlyOnes = x
    #Obliczenia da drugiej wartości wlasnej
    while True:
        Ax = np.dot(A,vectorOfOnlyOnes)
        # reortogonalizacja
        Ax = np.subtract(Ax, np.dot(x, np.dot(np.transpose(x), Ax)))
        temporary4 = ownValues(A, vectorOfOnlyOnes)
        temporary5 = ownValues(A, Ax)

        if np.abs(temporary4 - temporary5) < eps:
            vectorOfOnlyOnes = Ax/ np.linalg.norm(Ax)
            temporary6 = ownValues(A, vectorOfOnlyOnes)
            break
        vectorOfOnlyOnes = Ax / np.linalg.norm(Ax)


    print("The biggest intrinsic value of the matrix: {}".format(temporary3))
    print("Her eigenvector: {}".format(x))
    print("Second biggest intrinsic value of the matrix: {}".format(temporary6))
    print("Her eigenvector: {}".format(vectorOfOnlyOnes))
    return


eps = 1e-15

A =[[19. / 12., 13. / 12., 5. / 6., 5. / 6., 13. / 12., -17. / 12.],
          [13. / 12., 13. / 12., 5. / 6., 5. / 6., -11. / 12., 13. / 12.],
          [5. / 6., 5. / 6., 5. / 6., -1. / 6., 5. / 6., 5. / 6.],
          [5. / 6., 5. / 6., -1. / 6., 5. / 6., 5. / 6., 5. / 6.],
          [13. / 12., -11. / 12., 5. / 6., 5. / 6., 13. / 12., 13. / 12.],
          [-17. / 12., 13. / 12., 5. / 6., 5. / 6., 13. / 12., 19. / 12.]]

x = np.ones( (6) )


test=onwVectors(A,x)
print(test)

