class Endereco:
    def __init__(self,logradouro:str,bairro:str,numero:int) -> None:
        self.logradouro = logradouro
        self.bairro= bairro
        self.numero = numero

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nbairro: {self.bairro}"
                f"\nnumero: {self.numero}")
        
        
        