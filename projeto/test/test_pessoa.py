import pytest # type: ignore
from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.sexo import Sexo

# Modelo.
@pytest.fixture
def cria_pessoa():
    pessoa_1= Pessoa ("Pedro",15,Sexo.FEMININO,Endereco("Rua A","Caetano",57))
    return pessoa_1
def test_pessoa_valido(cria_pessoa):
    assert cria_pessoa.nome == "Pedro"

def test_pesssoa_atributo_idade(cria_pessoa):
    assert cria_pessoa.idade == 15

def test_endereco_logradoouro_de_pessoa(cria_pessoa):
    assert cria_pessoa.endereco.logradouro == "Rua A"