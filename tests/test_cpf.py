"""
Testes unitários para o módulo cpf_cnpj_validador.cpf

Os casos de teste foram organizados usando as técnicas de
particionamento em classes de equivalência e análise de valor
limite, comuns na disciplina de Teste de Software:

  - classes válidas: CPFs reais, com e sem formatação;
  - classes inválidas: dígito verificador errado, tamanho errado,
    todos os dígitos iguais, caracteres não numéricos, entrada
    vazia/None;
  - valores limite: string com 10 e com 12 dígitos (um a menos e um
    a mais que o tamanho válido de 11).
"""

import unittest

from cpf_cnpj_validador.cpf import validar_cpf, formatar_cpf, limpar_documento


class TestLimparDocumento(unittest.TestCase):
    def test_remove_pontuacao(self):
        self.assertEqual(limpar_documento("111.444.777-35"), "11144477735")

    def test_mantem_apenas_digitos_ja_limpos(self):
        self.assertEqual(limpar_documento("11144477735"), "11144477735")

    def test_remove_espacos_e_outros_simbolos(self):
        self.assertEqual(limpar_documento(" 111 444 777 35 "), "11144477735")

    def test_entrada_none_retorna_vazio(self):
        self.assertEqual(limpar_documento(None), "")


class TestValidarCpf(unittest.TestCase):
    # ---- Classes de equivalência válidas -----------------------------
    def test_cpf_valido_sem_formatacao(self):
        self.assertTrue(validar_cpf("11144477735"))

    def test_cpf_valido_com_formatacao(self):
        self.assertTrue(validar_cpf("111.444.777-35"))

    def test_cpf_valido_outro_numero(self):
        # 529.982.247-25 é um CPF classicamente usado em exemplos
        # didáticos por satisfazer o algoritmo de módulo 11.
        self.assertTrue(validar_cpf("529.982.247-25"))

    # ---- Classes de equivalência inválidas ---------------------------
    def test_cpf_com_digito_verificador_incorreto(self):
        self.assertFalse(validar_cpf("111.444.777-36"))

    def test_cpf_todos_digitos_iguais(self):
        for digito in "0123456789":
            with self.subTest(digito=digito):
                self.assertFalse(validar_cpf(digito * 11))

    def test_cpf_com_letras_e_simbolos_invalidos(self):
        self.assertFalse(validar_cpf("abc.def.ghi-jk"))

    def test_cpf_vazio(self):
        self.assertFalse(validar_cpf(""))

    def test_cpf_none(self):
        self.assertFalse(validar_cpf(None))

    # ---- Análise de valor limite (tamanho) ---------------------------
    def test_cpf_com_10_digitos_e_invalido(self):
        self.assertFalse(validar_cpf("1114447773"))

    def test_cpf_com_12_digitos_e_invalido(self):
        self.assertFalse(validar_cpf("111444777351"))


class TestFormatarCpf(unittest.TestCase):
    def test_formata_cpf_sem_pontuacao(self):
        self.assertEqual(formatar_cpf("11144477735"), "111.444.777-35")

    def test_formata_cpf_ja_formatado_idempotente(self):
        self.assertEqual(formatar_cpf("111.444.777-35"), "111.444.777-35")

    def test_formatar_cpf_tamanho_invalido_lanca_excecao(self):
        with self.assertRaises(ValueError):
            formatar_cpf("123")


if __name__ == "__main__":
    unittest.main()
