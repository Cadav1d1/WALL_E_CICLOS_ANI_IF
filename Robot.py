class Robot:
    def __init__(self):
        self.estado_actual = "Robot Apagado"
        self.basura_reciclable = 0
        
        #self.basura_no_reciclable = 0

    def encender(self):
        if self.estado_actual == "Robot Apagado":
            self.estado_actual = "Robot Encendido-Posicion Home"
            return "El robot se ha encendido"  
        else:
            return "El robot ya está encendido"
    def seguir_camino(self):
        if self.estado_actual=="Robot Apagado":
            return "El robot esta apagado. Enciendelo para navegar camino"
        elif self.estado_actual=="Robot Encendido-Posicion Home" or "Objeto recolectado correctamente" or "El robot exploro el terreno y encontro un objeto" or "Objeto desechado correctamente" or "Objetos soltados correctamente":
            self.estado_actual="El robot exploro el terreno y encontro un objeto"
            return "Navegando terreno"
        elif self.estado_actual=="El robot exploro el terreno y encontro un objeto":
            return "Ya se exploro el terreno y se encontro un objeto"
    def recolectar_objeto(self):
        if self.estado_actual=="Robot Encendido-Posicion Home":
            return "Estas en Home, selecciona la opcion de navegar por el terreno para encontrar objetos reciclables"
        elif self.estado_actual == "El robot exploro el terreno y encontro un objeto":
            self.basura_reciclable += 1
            self.estado_actual ="Objeto recolectado correctamente"
            return "Recolectando objetos"
        elif self.estado_actual== "Robot Apagado":
            return "El robot esta apagado. Enciendelo para recolectar objetos"
        else:
            return "Ya no hay mas objetos que recoger en esta zona"
    def apagar(self):
        if self.estado_actual == "Robot Encendido-Posicion Home" or "El robot exploro el terreno y encontro un objeto" or "Objeto recolectado correctamente" or "Basura reciclable desechada" or "Objetos soltados correctamente":
            self.estado_actual = "Robot Apagado"
            return "El robot se ha apagado"
        elif self.estado_actual == "Robot Apagado":
             return "El robot ya está apagado"

    

    def botar_reciclable(self):
        if self.estado_actual == "Robot Encendido-Posicion Home" or "El robot exploro el terreno y encontro un objeto" or "Objeto recolectado correctamente" or "Objeto desechado correctamente":
            if self.basura_reciclable > 0:
                self.basura_reciclable -= 1
                self.estado_actual="Objeto desechado correctamente"
                return "Objeto reciclable botado correctamente"
            elif self.estado_actual =="Robot Apagado":
                return "El robot debe estar encendido para desechar reciclaje"

            else:
                return "No hay basura reciclable para botar"
      

    """def botar_no_reciclable(self):
        if self.estado_actual == "Robot Encendido":
            if self.basura_no_reciclable > 0:
                self.basura_no_reciclable -= 1
                return "Basura no reciclable botada correctamente"
            else:
                return "No hay basura no reciclable para botar"
        else:
            return "El robot debe estar encendido para botar basura"""

    def soltar_objetos(self):
        
        if self.estado_actual=="Robot Apagado":
                return "El robot debe estar encendido para soltar objetos"
            
        elif self.estado_actual == "Robot Encendido-Posicion Home" or "El robot exploro el terreno y encontro un objeto" or "Objeto recolectado correctamente" or "Objeto desechado correctamente": #or self.basura_no_reciclable > 0:
            basura_reciclable=self.basura_reciclable
            if basura_reciclable>0:
                    self.basura_reciclable = 0
                    self.estado_actual="Objetos soltados correctamente"
                #self.basura_no_reciclable = 0
        return "Objetos soltados correctamente. Total objetos soltados: {}".format(basura_reciclable)   

    def parado_de_emergencia(self):
        if self.estado_actual=="Robot Apagado":
           
            return "El robot no esta encendido, por tanto no se puede hacer parado de emergencia ya que el robot ya esta inmovil"
        elif self.estado_actual == "Robot Encendido-Posicion Home" or "El robot exploro el terreno y encontro un objeto" or "Objeto recolectado correctamente" or "Objeto desechado correctamente" or "Objetos soltados correctamente":
            self.estado_actual = "Parado de Emergencia"
            return "Parado de emergencia. Robot apagado"
        elif self.estado_actual=="Parado de Emergencia":
            return "El robot ya esta en modo de emergencia"

    def continuar(self):
        if self.estado_actual == "Parado de Emergencia":
            self.estado_actual = "Robot Encendido"
            return "Continuando operaciones"
        else:
            return "El robot no esta en Parado de Emergencia, por ende nunca se interrumpieron las acciones del robot"