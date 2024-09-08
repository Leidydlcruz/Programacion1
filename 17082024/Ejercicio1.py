class Estudiante:
    
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}" 
    
    
class Curso:
    
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado al curso {self.nombre}")
        
    def eliminar_estudiante(self, nombre_estudiante):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre_estudiante:
                self.estudiantes.remove(estudiante)
                print(f"Estudiante {nombre_estudiante} eliminado del curso {self.nombre}")
                return
                
    def mostrar_estudiantes(self):
        if self.estudiantes:
            print(f"Estudiantes inscritos al curdo {self.nombre}")
            for estudiante in self.estudiantes:
                print(estudiante)
        else:
            print(f"No existen estudiantes en el curso {self.nombre}")
            
            
estudiante1 = Estudiante('Juan Perez',12,'Septimo')
estudiante2 = Estudiante('Maria Lopez', 13, 'Octavo')

curso1 = Curso('Matematicas Especiales', 'Jorge Ruiz')
curso1.agregar_estudiante(estudiante1)
curso1.agregar_estudiante(estudiante2)

curso1.mostrar_estudiantes()

curso1.eliminar_estudiante('Maria Lopez')

curso1.mostrar_estudiantes()
