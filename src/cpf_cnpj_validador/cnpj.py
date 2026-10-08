"""
Validação e formatação de CNPJ (Cadastro Nacional da Pessoa Jurídica).

O CNPJ é composto por 14 dígitos: 12 dígitos base (8 de raiz + 4 de
filial/ordem) + 2 dígitos verificadores, calculados por módulo 11
com pesos específicos.
"""

from .cpf import limpar_documento

_PESOS_PRIMEIRO_DV = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
_PESOS_SEGUNDO_DV = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def _calcular_digito_verificador(numeros: str, pesos: list) -> int:
    soma = sum(int(digito) * peso for digito, peso in zip(numeros, pesos))
    resto = soma % 11
    if resto < 2:
        return 0
    return 11 - resto


def validar_cnpj(cnpj: str) -> bool:
    """Valida um número de CNPJ.

    Aceita o CNPJ formatado (ex: "11.222.333/0001-81") ou apenas os
    dígitos (ex: "11222333000181"). Retorna True se o CNPJ é
    válido, False caso contrário.
    """
    cnpj = limpar_documento(cnpj)

    if len(cnpj) != 14:
        return False

    # CNPJs com todos os dígitos iguais nunca são válidos/emitidos.
    if cnpj == cnpj[0] * 14:
        return False

    primeiro_dv = _calcular_digito_verificador(cnpj[:12], _PESOS_PRIMEIRO_DV)
    segundo_dv = _calcular_digito_verificador(
        cnpj[:12] + str(primeiro_dv), _PESOS_SEGUNDO_DV
    )

    return cnpj[-2:] == f"{primeiro_dv}{segundo_dv}"


def formatar_cnpj(cnpj: str) -> str:
    """Formata uma string de 14 dígitos como "##.###.###/####-##".

    Lança ValueError se a entrada não tiver 14 dígitos após a
    remoção de caracteres não numéricos.
    """
    cnpj = limpar_documento(cnpj)
    if len(cnpj) != 14:
        raise ValueError("CNPJ deve conter 14 dígitos para ser formatado.")
    return f"{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
