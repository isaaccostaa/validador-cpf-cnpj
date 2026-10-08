"""
cpf_cnpj_validador
===================

Biblioteca simples para validar e formatar números de CPF e CNPJ,
dois documentos de identificação usados no Brasil.

Exemplo de uso:

    >>> from cpf_cnpj_validador import validar_cpf, formatar_cpf
    >>> validar_cpf("111.444.777-35")
    True
    >>> formatar_cpf("11144477735")
    '111.444.777-35'
"""

from .cpf import validar_cpf, formatar_cpf, limpar_documento
from .cnpj import validar_cnpj, formatar_cnpj

__all__ = [
    "validar_cpf",
    "formatar_cpf",
    "validar_cnpj",
    "formatar_cnpj",
    "limpar_documento",
]

__version__ = "1.0.0"
