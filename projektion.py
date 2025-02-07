import numpy
import math
def projV(point, vektor1, vektor2): #tar punkt och två vektorer som parametrar
        point = numpy.array(point)
        normal = numpy.cross(vektor1, vektor2)
        print("Normalen är: ", normal)
        result = normal * ((numpy.dot(point,normal)) / math.pow(numpy.linalg.norm(normal), 2))
        return(result)

def projN(point, normal): #tar punkt och normal som parametrar
        point = numpy.array(point)
        normal = numpy.array(normal)
        result = normal * ((numpy.dot(point,normal)) / math.pow(numpy.linalg.norm(normal), 2))
        return(result)


print(projV([math.pi, math.e, 1], [1,1,0], [0,-1,0]))   #Uppgift b (u,v)

print(projN([math.pi, math.e, 1], [1,1,1]))             #Uppgift c (n)
print(projN([math.pi, math.e, 1], [3,3,3]))             #Uppgift c (m)