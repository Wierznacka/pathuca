#caneta.py

class Caneta:
    def __init__(self,cor):
       self.cor = cor 
       self.tampada = True
       
    def destampar(self):  
        if self.tampada:
            self.tampada = False
            print("A caneta foi destampada")
            
        else:
            print(" A caneta já está destampada")
            
    def tampar(self): 
        if not self.tampada:
                self.tampada = False 
                print("A caneta já está tampada") 
        else:
            print("Ops! A caneta já está tampada") 
            
    def escrever(self):
        if not self.tampada and self.carga >0:
            self.carga -= 50
            print("Escrevendo")
            
                            
        else:
            print("A caneta está tampada ou sem carga")
     
    def get_carga(self):
            print ("f{self.carga}")                 
            
caneta_azul = Caneta ("Azul")
caneta_preta = Caneta ("Preta")
print (caneta_azul.cor)
print (caneta_azul.tampada)
caneta_azul.destampar()
caneta_azul.destampar()
print(caneta_azul.tampada)
caneta_azul.tampar()
caneta_azul.tampar()
print(caneta_azul.tampada)
caneta_azul.escrever()
caneta_azul. get_carga()
caneta_azul.escrever()
caneta_azul. get_carga()
    
