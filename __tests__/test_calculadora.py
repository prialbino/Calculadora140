# 1 - bibliotecas, frameworks e referencias externas 
import pytest  # framework de teste de unidade 

# funcoes que serao testadas
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

from utils.utils import ler_csv   # leitura do arq csv

# 2 - Testes
def test_somar_dois_numeros():
    # padrao Triple A - IEEE - Arrange / Act / Assert

    # Arrange / Prepara/ Configura
    # Dados de entrada e saida
    num1 = 5
    num2 = 7
    resultado_esperado = 12

    # Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # assert / valida
    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():
    # configura
    num1 = 10 
    num2 = 6
    resultado_esperado = 4

    # executa 
    resultado_obtido = subtrair_dois_numeros(num1, num2)

    # valida    
    assert resultado_esperado == resultado_obtido

def test_multiplicar_dois_numeros():
    num1 = 3
    num2 = 9
    resultado_esperado = 27

    resultado_obtido = multiplicar_dois_numeros(num1, num2)
    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros():
    num1 = 64
    num2 = 4
    resultado_esperado = 16

    resultado_obtido = dividir_dois_numeros(num1, num2)
    assert resultado_esperado == resultado_obtido

def test_dividir_por_zero():
    num1 = 64
    num2 = 0
    resultado_esperado = 'Não é possível dividir por zero'

    resultado_obtido = dividir_dois_numeros(num1, num2)
    assert resultado_esperado == resultado_obtido

#Test baseado em dados = Data Driven Tests (DDT) >> Massa de teste
    # Dados em lista
    # Dados em arquivo (CSV, json, XML, Dat, etc)

@pytest.mark.parametrize('num1, num2, resultado_esperado', 
                         [ # array / matriz
                            (5, 7, 12),  # tupla, registro                            
                            (0, 8, 8),
                            (10, -15, -5),
                            (6, 0.75, 6.75)
                         ]
                         )    
def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):
    # padrao Triple A - IEEE - Arrange / Act / Assert

    # Arrange / Prepara/ Configura
    # Dados de entrada e saida fornecidos pela massa de teste em formato de lista 

    # Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # assert / valida
    assert resultado_esperado == resultado_obtido


@pytest.mark.parametrize('num1, num2, resultado_esperado',
                            ler_csv('./fixtures/massa_somar.cvs')                     
                         )

def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):
    # padrao Triple A - IEEE - Arrange / Act / Assert

    # Arrange / Prepara/ Configura
    # Dados de entrada e saida fornecidos pela massa de teste em formato csv 

    # Act / Executa
    resultado_obtido = somar_dois_numeros(float(num1), float(num2))

    # assert / valida
    assert float(resultado_esperado) == resultado_obtido