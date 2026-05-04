import pytest
from app import validar_edad

# 🔹 Partición de equivalencia
def test_edad_valida():
    assert validar_edad(30) == True

def test_edad_invalida_menor():
    assert validar_edad(10) == False

def test_edad_invalida_mayor():
    assert validar_edad(70) == False


# 🔥 Valores límite
def test_limite_inferior_invalido():
    assert validar_edad(18) == False

def test_limite_inferior_valido():
    assert validar_edad(19) == True

def test_limite_superior_valido():
    assert validar_edad(68) == True

def test_limite_superior_invalido():
    assert validar_edad(69) == False


# 🚀 Parametrizado (forma profesional)
@pytest.mark.parametrize("edad,esperado", [
    (30, True),
    (10, False),
    (70, False),
    (18, False),
    (19, True),
    (68, True),
    (69, False),
])
def test_edades_parametrizadas(edad, esperado):
    assert validar_edad(edad) == esperado