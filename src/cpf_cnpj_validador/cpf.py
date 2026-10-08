"""
Validação e formatação de CPF (Cadastro de Pessoas Físicas).

O CPF é composto por 11 dígitos: 9 dígitos base + 2 dígitos
verificadores, calculados a partir de um algoritmo de módulo 11.
"""

import re


def limpar_documento(documento: str) -> str:
    """Remove qualquer caractere que não seja dígito.

    >>> limpar_documento("111.444.777-35")
    '11144477735'
    """
    if documento is None:
        return ""
    return re.sub(r"\D", "", documento)


def _calcular_digito_verificador(numeros: str, peso_inicial: int) -> int:
    """Calcula um dígito verificador de CPF pelo algoritmo de módulo 11."""
    soma = 0
    peso = peso_inicial
    for digito in numeros:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11
    if resto < 2:
        return 0
    return 11 - resto


def validar_cpf(cpf: str) -> bool:
    """Valida um número de CPF.

    Aceita o CPF formatado (ex: "111.444.777-35") ou apenas os
    dígitos (ex: "11144477735"). Retorna True se o CPF é válido,
    False caso contrário.

    Regras verificadas:
      - deve conter exatamente 11 dígitos numéricos;
      - não pode ser uma sequência de dígitos repetidos
        (ex: "111.111.111-11"), pois esses números "passam" no
        cálculo do módulo 11 mas não são CPFs válidos emitidos;
      - os dois dígitos verificadores devem bater com o cálculo
        oficial do módulo 11.
    """
    cpf = limpar_documento(cpf)

    if len(cpf) != 11:
        return False

    # CPFs com todos os dígitos iguais (111.111.111-11, 000.000.000-00, etc.)
    # são matematicamente "válidos" no cálculo, mas nunca são emitidos.
    if cpf == cpf[0] * 11:
        return False

    primeiro_dv = _calcular_digito_verificador(cpf[:9], 10)
    segundo_dv = _calcular_digito_verificador(cpf[:9] + str(primeiro_dv), 11)

    return cpf[-2:] == f"{primeiro_dv}{segundo_dv}"


def formatar_cpf(cpf: str) -> str:
    """Formata uma string de 11 dígitos como "###.###.###-##".

    Lança ValueError se a entrada não tiver 11 dígitos após a
    remoção de caracteres não numéricos.
    """
    cpf = limpar_documento(cpf)
    if len(cpf) != 11:
        raise ValueError("CPF deve conter 11 dígitos para ser formatado.")
    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
