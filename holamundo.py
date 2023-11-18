class persona:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def suma(self):
        resultado=self.a+self.b
        return resultado
    
persona=persona(30,30)
print(persona.suma())