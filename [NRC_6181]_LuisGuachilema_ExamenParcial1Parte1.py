ListaDocentes=[]
#-------------------------------------------------------------
#           CLASE PADRE, PERSONALaCADEMICO
#-------------------------------------------------------------
class PersonalAcademico:
    '''
    Clase Padre, donde contendrá los atributos de los docentes como:nombre, apellido, edad
    '''
    def __init__(self, nombre, apellido, edad):
        '''
        Atributos de la clase padre
        '''
        self.atributo1=nombre
        self.atributo2=apellido
        self.atributo3=edad
#-------------------------------------------------------------
#           CLASE HIJA DOCENTE
#-------------------------------------------------------------
class Docente(PersonalAcademico):
    '''
    Clase hija/subclase donde tendrá sus propios atributos como:rol, area, salario 
    '''
    def perfil(self, rol, area, salario ):
        self.atributo4=rol
        self.atributo5=area
        self.atributo6=salario
#-------------------------------------------------------------------------
#             INSTACIAMOS LAS CLASES
#-------------------------------------------------------------------------
def crearPersonalAcademico():
    '''
    Función para crear un docente con atributos de las clase padre y la subclase hija
    Se validará a que el ingreso de registro de doncestes sea mayor a 0 y almacenará en una lista
    '''
    print("===========================================================")
    print("|                  CREAR PERSONAL                         |")
    print("===========================================================")
    #-------------------------------------------------------------------------
    #              Ingreso docentes a registrar
    #-------------------------------------------------------------------------
    numeroDocentesRegistro=int(input("Ingrese el numero de docentes que desea registrar: "))
    if numeroDocentesRegistro>0:

        for i in range(numeroDocentesRegistro):
            nombre=str(input("Ingrese el nombre del docente: "))
            apellido=str(input("Ingrese el apellido del docente: "))
            edad=int(input("Ingrese la edad del docente: "))
            rol=str(input("Ingrese el rol del docente: "))
            docenteNuevo=Docente(nombre,apellido,edad)
            docenteNuevo.perfil(rol,str(input("Ingrese el área del docente: ")),str(input("Ingrese su salio: ")))
            '''
            Almacenamos los docentes en una lista, con los atributos de la clase padre y la subclase hija
            '''
            ListaDocentes.append(docenteNuevo.atributo1)
            ListaDocentes.append(docenteNuevo.atributo2)
            ListaDocentes.append(docenteNuevo.atributo3)
            ListaDocentes.append(docenteNuevo.atributo4)
            ListaDocentes.append(docenteNuevo.atributo5)
            ListaDocentes.append(docenteNuevo.atributo6)
            print("===========================================================")
            print("|             LISTA DE DOCENTES REGISTRADOS                |")
            print("===========================================================")
            for i in range (numeroDocentesRegistro):
                print(ListaDocentes)
    else:
        print("No se puede registrar esa cantidad de docentes")
crearPersonalAcademico()

