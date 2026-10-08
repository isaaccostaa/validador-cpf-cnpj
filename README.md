# Validador de CPF e CNPJ

Aplicação em Python para validar e formatar números de **CPF** e
**CNPJ**, desenvolvida para a atividade *"Criar Aplicação de Validar
CPF e CNPJ Válido"* da disciplina de Teste de Software.

O foco da atividade é a implementação de **testes unitários**, por
isso o projeto traz uma suíte de testes organizada por técnicas de
teste de caixa-preta (particionamento em classes de equivalência e
análise de valor limite), além do código da aplicação em si.

## Estrutura do projeto

```
cpf-cnpj-validador/
├── src/
│   └── cpf_cnpj_validador/
│       ├── __init__.py     # exporta as funções públicas
│       ├── cpf.py          # validação e formatação de CPF
│       ├── cnpj.py         # validação e formatação de CNPJ
│       └── cli.py          # aplicação de linha de comando (menu)
├── tests/
│   ├── test_cpf.py
│   ├── test_cnpj.py
│   └── test_cli.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Como funciona a validação

CPF e CNPJ têm, cada um, dois **dígitos verificadores** calculados a
partir dos demais dígitos usando o algoritmo de **módulo 11**. A
aplicação:

1. remove qualquer formatação (pontos, traço, barra, espaços);
2. verifica se a quantidade de dígitos está correta (11 para CPF, 14
   para CNPJ);
3. rejeita sequências de dígitos repetidos (`111.111.111-11`,
   `00.000.000/0000-00`, etc.), que "passam" no cálculo matemático
   mas nunca são documentos realmente emitidos;
4. recalcula os dois dígitos verificadores e compara com os dígitos
   informados.

## Como executar a aplicação

Requer apenas Python 3.8+ (não há dependências externas para rodar
a aplicação, só para os testes, se quiser usar o `pytest`).

Modo interativo (menu):

```bash
cd src
python -m cpf_cnpj_validador.cli
```

Validando diretamente por argumento:

```bash
cd src
python -m cpf_cnpj_validador.cli "111.444.777-35" "11.222.333/0001-81"
```

Exemplo de saída:

```
CPF válido: 111.444.777-35
CNPJ válido: 11.222.333/0001-81
```

## Como rodar os testes unitários

Com `unittest` (não precisa instalar nada):

```bash
python -m unittest discover -s tests -t . -v
```

Ou, se preferir instalar o `pytest` (`pip install -r requirements.txt`):

```bash
pytest -v
```

A suíte cobre:

- CPFs e CNPJs válidos, formatados e não formatados;
- dígito verificador incorreto;
- todos os dígitos iguais (ex: `111.111.111-11`);
- entradas com letras/símbolos inválidos;
- entradas vazias ou `None`;
- valores limite de tamanho (um dígito a menos / a mais que o
  esperado);
- a função de formatação (`formatar_cpf` / `formatar_cnpj`),
  incluindo o caso de erro quando o tamanho é inválido.

## Uso como biblioteca

```python
from cpf_cnpj_validador import validar_cpf, validar_cnpj, formatar_cpf

validar_cpf("111.444.777-35")   # True
validar_cpf("111.111.111-11")   # False
formatar_cpf("11144477735")     # "111.444.777-35"
```

## Autor

Isaac Costa — atividade da disciplina de Teste de Software.
