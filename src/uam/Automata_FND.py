class Automata(object):
    #Estado Q0
    def q0(self,cadena,contador,estados):
        #si es el ultimo digito a leer y se encuentra en este estado, no debe de aceptar la cadena
        if(len(cadena)==contador):
            return 1
        #Si no es el ultimo digito y es un uno se va a si mismo
        if(cadena[contador]=="1"):
            contador = contador+1
            return self.q0(cadena,contador,estados)
        #Si no es el ultimo digito y es un cero se va al estado q1
        if(cadena[contador]=="0"):
            self.q0(cadena,contador,estados)
            contador = contador+1
            return self.q1(cadena,contador,estados)
    #Estado Q1
    def q1(self, cadena, contador,estados):
        #Si no es el ultimo digito y se encuentra en ese estado no lodebe de reconocer la cadena
        if(len(cadena)==contador):
            return 1
        #Si no es el ultimo digito y es un uno se va a q0
        elif(cadena[contador]=="1"):
            contador = contador+1
            return self.q2(cadena,contador,estados)
    
    def q2(self, cadena, contador,estados):
        return 0
