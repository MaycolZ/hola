print ("1  =  mostrar regiones")
print ("2  =  mostrar comparación entre la primera y segunda dosis de una región")
print ("3  =  mostrar las 5 regiones mas vacunadas con la primera dosis")
print ("4  =  mostrar las 5 regiones mas vacunadas con la segunda dosis")
print ("5  =  mostrar cantidad de personas que se vacunan con la segunda dosis y las que no")
print ("6  =  mostrar la region mas vacunada de Chile")
print ("7  =  mostrar una metrica de comparacion")
print ("8  =  finalizar")

print ("bienvenido, ingrese un número: ")
x=0
while x==0:
    x=int(input())

    while x == 0 :
        print("el numero es invalido, ingrese nuevamente")
        x=int(input())

    if x == 1 :
        Regiones_de_Chile = ["Tarapacá", "Antofagasta", "Atacama", "Coquimbo", "Valparaíso", "O'Higgins", "Maule", "Biobío", "La Araucanía", "Los Lagos", "Aysén", "Magallanes", "Metropolitana", "Los Ríos", "Arica y Parinacota", "Ñuble"]
        Números = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'RM', 'XIV', 'XV', 'XVI']

        z=0
        while x==1 :
        
            print (Números[z], Regiones_de_Chile[z])
            z = z+1
            if z==15:
                x=0
                print("Ingrese otra elección: ")
    

    while x == 2 :
        a1 = 217540
        a2 = 335388

        b1 = 417930
        b2 = 180987

        c1 = 196220
        c2 = 163416

        d1 = 536048
        d2 = 440037

        e1 = 1334967
        e2 = 1137628

        f1 = 687840
        f2 = 575592

        g1 = 765669
        g2 = 645355

        h1 = 1081509
        h2 = 927873

        i1 = 649132
        i2 = 555387

        j1 = 578212
        j2 = 478977

        k1 = 68840
        k2 = 61154

        l1 = 120293
        l2 = 112914

        m1 = 4978990
        m2 = 4138402

        n1 = 263757
        n2 = 226649

        o1 = 146884
        o2 = 118928

        p1 = 362431
        p2 = 313431
        
        print ("para Tarapacá ingrese : 1") 
        print ("para Antofagasta ingrese : 2") 
        print ("para Atacama ingrese : 3") 
        print ("para Coquimbo ingrese : 4") 
        print ("para Valparaíso ingrese : 5") 
        print ("para O'Higgins ingrese : 6") 
        print ("para El Maule ingrese : 7")  
        print ("para El Biobío ingrese : 8") 
        print ("para La Araucanía ingrese : 9") 
        print ("para Los Lagos ingrese : 10") 
        print ("para Aysén ingrese : 11") 
        print ("para Magallanes y Antártica Chilena ingrese : 12") 
        print ("para Región Metropolitana de Santiago ingrese : 13") 
        print ("para Los Ríos ingrese : 14") 
        print ("para Arica y Parinacotaingrese : 15") 
        print ("para Ñuble ingrese : 16")
        print ("Para volver a las Elecciones Anteriores ingrese : 17")
        
        z=0
        while z==0:

            z=int(input())

            while z == 1:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [a1, a2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Tarapacá)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 2:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [b1, b2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Antofagasta)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 3:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [c1, c2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Atacama)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 4:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [d1, d2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Coquimbo)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 5:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [e1, e2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Valparaíso)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 6:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [f1, f2]
 
                ax.set_ylabel('Dosis')

                ax.set_title("diferencia entre vacunaciones por dosis (O'Higgins)")

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 7:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [g1, g2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Maule)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 8:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [h1, h2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Biobío)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 9:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [i1, i2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (La Araucanía)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 10:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [j1, j2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Los Lagos)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 11:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [k1, k2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Aysén)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 12:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [l1, l2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Magallanes)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 13:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [m1, m2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Metropolitana)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 14:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [n1, n2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Los Ríos)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 15:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [o1, o2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Arica)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z == 16:
                import matplotlib
                import matplotlib.pyplot as plt
                import numpy as np
 
                fig, ax = plt.subplots()
                plt.rcParams["figure.figsize"] = (10, 5)
                regiones2 = ["1° Dosis", "2° Dosis"]
                numeros2 = [p1, p2]
 
                ax.set_ylabel('Dosis')

                ax.set_title('diferencia entre vacunaciones por dosis (Ñuble)')

                plt.bar(regiones2, numeros2)
                plt.savefig('Figure_1.png')
                plt.show()
        
                z=0
                print("Ingrese otra Número")

            while z==17:
                z=18
                print("Ingrese otra elección")
                x=0
    while x==3:
        import matplotlib
        import matplotlib.pyplot as plt
        import numpy as np
        plt.rcParams["figure.figsize"] = (7, 4,)
        regiones1 = [' ', "O'Higgins", 'Maule', 'Biobío', 'Valparaíso', 'Metropolitana']
        numeros1 = [0, 687840, 765669, 1081509, 1334967, 4978990]
 
        fig, ax = plt.subplots()

        ax.set_ylabel('Dosis')

        ax.set_title('Las 5 Regiones mas vacunadas con la Primera Dosis')

        plt.bar(regiones1, numeros1)
        plt.savefig('Figure_1.png')
        plt.xticks(rotation=270)

        plt.show()

        x=0
        print("Ingrese otra elección: ")


    while x==4:

        import matplotlib
        import matplotlib.pyplot as plt
        import numpy as np
 
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = (10, 5)
        regiones2 = [' ', "O'Higgins", 'Maule', 'Biobío', 'Valparaíso', 'Metropolitana']
        numeros2 = [0, 575592, 645355, 927873, 1137628, 4138402]
 
        

        ax.set_ylabel('Dosis')

        ax.set_title('Las 5 Regiones mas vacunadas con la segunda dosis')

        plt.bar(regiones2, numeros2)
        plt.savefig('Figure_1.png')
        plt.xticks(rotation=270)

        plt.show()

        x=0
        print("Ingrese otra elección: ")

    while x == 5:
        import numpy as np
        import matplotlib.pyplot as plt
 
        serie_1 = [180987, 335388, 163416, 440037, 1137628, 575592, 575592, 927873, 555387, 478977, 61154, 112914, 4138402, 226649, 118928, 313431]
        serie_2 = [36553, 82542, 32804, 96011, 197339, 112248, 120314, 153636, 93745, 99235, 7686, 7379, 840588, 37108, 27956, 49000]
 
 
        numero_de_grupos = len(serie_1)
        indice_barras = np.arange(numero_de_grupos)
        ancho_barras =0.35
 
        plt.bar(indice_barras, serie_1, width=ancho_barras, label='se vacunaron')
        plt.bar(indice_barras + ancho_barras, serie_2, width=ancho_barras, label='NO se vacunaron')
        plt.legend(loc='best')
        plt.xticks(indice_barras + ancho_barras, ("Tarapacá", "Antofagasta", "Atacama", "Coquimbo", "Valparaíso", "O'Higgins", "Maule", "Biobío", "La Araucanía", "Los Lagos", "Aysén", "Magallanes", "Metropolitana", "Los Ríos", "Arica y Parinacota", "Ñuble"))
 
        plt.ylabel('Dosis')
        plt.xlabel('Regiones')
        plt.title('diferencia entre las personas que se vacunan con la 2° Dosis y las que NO')
        plt.xticks(rotation=270)
        plt.show()

        x=0
        print("Ingrese otra elección: ")


    while x == 6:
        print("La Región más vacunada es : La región Metropolitana con un total de 9.117.392 Vacunaciones")
        x=0
        print("Ingrese otra elección: ")
    

    while x == 7:

        x=0
        print("Ingrese otra elección: ")

    while x == 8:
        x=9