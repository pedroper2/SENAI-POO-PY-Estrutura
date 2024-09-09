import os 
from models.pessoa import Pessoa 
from models.enums.sexo import Sexo
from models.endereco import Endereco

os.system ("cls||clear")

pessoa_1= Pessoa("Pedro",15,Sexo.FEMININO,Endereco("Rua A","Caetano",57))
print(pessoa_1)