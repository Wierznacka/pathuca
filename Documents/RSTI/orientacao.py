
class Calculadora:
    def _init_(self):
        self.soma
        self.divisao 
    def somar(self,a,b):
        self.soma = a + b
        print(f'O resultado da soma é: {self.soma}')
  
    def dividir(self,e,f):
        
        try:
            self.divida = e / f
            self.divida = 6 /"B"
            print(f"O resultado da divisão é: {self.divida}")
            
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
                 
c = Calculadora()
c.somar(1,2)
print
c.dividir(3,0)
print
c.dividir(6,"B") 
print      