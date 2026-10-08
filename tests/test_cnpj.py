"""
Testes unitários para o módulo cpf_cnpj_validador.cnpj

Mesma estratégia de particionamento em classes de equivalência e
valor limite usada em test_cpf.py, adaptada para o formato de CNPJ
(14 dígitos, com pesos de cálculo diferentes do CPF).
"""

import unittest

from cpf_cnpj_validador.cnpj import validar_cnpj, formatar_cnpj


class TestValidarCnpj(unittest.TestCase):
    # ---- Classes de equivalência válidas -----------------------------
    def test_cnpj_valido_sem_formatacao(self):
        self.assertTrue(validar_cnpj("11222333000181"))

    def test_cnpj_valido_com_formatacao(self):
        self.assertTrue(validar_cnpj("11.222.333/0001-81"))

    def test_cnpj_valido_filial_diferente_de_0001(self):
        self.assertTrue(validar_cnpj("11.222.333/0002-62"))

    # ---- Classes de equivalência inválidas ---------------------------
    def test_cnpj_com_digito_verificador_incorreto(self):
        self.assertFalse(validar_cnpj("11.222.333/0001-82"))

    def test_cnpj_todos_digitos_iguais(self):
        for digito in "0123456789":
            with self.subTest(digito=digito):
                self.assertFalse(validar_cnpj(digito * 14))

    def test_cnpj_com_caracteres_invalidos(self):
        self.assertFalse(validar_cnpj("AB.CDE.FGH/IJKL-MN"))

    def test_cnpj_vazio(self):
        self.assertFalse(validar_cnpj(""))

    def test_cnpj_none(self):
        self.assertFalse(validar_cnpj(None))

    # ---- Análise de valor limite (tamanho) ---------------------------
    def test_cnpj_com_13_digitos_e_invalido(self):
        self.assertFalse(validar_cnpj("1122233300018"))

    def test_cnpj_com_15_digitos_e_invalido(self):
        self.assertFalse(validar_cnpj("112223330001811"))


class TestFormatarCnpj(unittest.TestCase):
    def test_formata_cnpj_sem_pontuacao(self):
        self.assertEqual(formatar_cnpj("11222333000181"), "11.222.333/0001-81")

    def test_formata_cnpj_ja_formatado_idempotente(self):
        self.assertEqual(formatar_cnpj("11.222.333/0001-81"), "11.222.333/0001-81")

    def test_formatar_cnpj_tamanho_invalido_lanca_excecao(self):
        with self.assertRaises(ValueError):
            formatar_cnpj("123")


if __name__ == "__main__":
    unittest.main()
