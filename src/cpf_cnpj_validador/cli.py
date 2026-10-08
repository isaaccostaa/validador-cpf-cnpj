"""
Aplicação de linha de comando para validar CPF e CNPJ.

Uso:
    python -m cpf_cnpj_validador.cli

Também é possível validar diretamente por argumento:
    python -m cpf_cnpj_validador.cli 111.444.777-35
    python -m cpf_cnpj_validador.cli 11.222.333/0001-81
"""

import sys

from .cpf import validar_cpf, formatar_cpf, limpar_documento
from .cnpj import validar_cnpj, formatar_cnpj


def identificar_e_validar(documento: str) -> str:
    """Identifica se é CPF (11 dígitos) ou CNPJ (14 dígitos), valida
    e devolve uma mensagem amigável com o resultado."""
    numeros = limpar_documento(documento)

    if len(numeros) == 11:
        if validar_cpf(numeros):
            return f"CPF válido: {formatar_cpf(numeros)}"
        return f"CPF inválido: {documento}"

    if len(numeros) == 14:
        if validar_cnpj(numeros):
            return f"CNPJ válido: {formatar_cnpj(numeros)}"
        return f"CNPJ inválido: {documento}"

    return (
        f"Entrada inválida: '{documento}' tem {len(numeros)} dígito(s). "
        "Um CPF tem 11 dígitos e um CNPJ tem 14 dígitos."
    )


def menu() -> None:
    print("=" * 50)
    print(" Validador de CPF e CNPJ")
    print("=" * 50)
    print("Digite um CPF ou CNPJ (com ou sem pontuação).")
    print("Digite 'sair' para encerrar.\n")

    while True:
        entrada = input("CPF/CNPJ: ").strip()
        if entrada.lower() in ("sair", "exit", "quit"):
            print("Encerrando. Até mais!")
            break
        if not entrada:
            continue
        print(identificar_e_validar(entrada))
        print()


def main() -> None:
    argumentos = sys.argv[1:]
    if argumentos:
        for documento in argumentos:
            print(identificar_e_validar(documento))
    else:
        menu()


if __name__ == "__main__":
    main()
