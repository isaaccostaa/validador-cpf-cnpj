"""
Testes unitários para a camada de CLI (cpf_cnpj_validador.cli),
garantindo que a função que identifica automaticamente se a entrada
é um CPF ou um CNPJ se comporta corretamente.
"""

import unittest

from cpf_cnpj_validador.cli import identificar_e_validar


class TestIdentificarEValidar(unittest.TestCase):
    def test_identifica_cpf_valido(self):
        resultado = identificar_e_validar("111.444.777-35")
        self.assertIn("CPF válido", resultado)
        self.assertIn("111.444.777-35", resultado)

    def test_identifica_cpf_invalido(self):
        resultado = identificar_e_validar("111.444.777-00")
        self.assertIn("CPF inválido", resultado)

    def test_identifica_cnpj_valido(self):
        resultado = identificar_e_validar("11.222.333/0001-81")
        self.assertIn("CNPJ válido", resultado)

    def test_identifica_cnpj_invalido(self):
        resultado = identificar_e_validar("11.222.333/0001-00")
        self.assertIn("CNPJ inválido", resultado)

    def test_entrada_com_tamanho_nao_reconhecido(self):
        resultado = identificar_e_validar("12345")
        self.assertIn("Entrada inválida", resultado)


if __name__ == "__main__":
    unittest.main()
