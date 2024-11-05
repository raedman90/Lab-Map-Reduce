
# MapReduce

Este é um projeto de contagem de frequência de palavras implementado com um framework básico de MapReduce em Python. O projeto utiliza threads para processar arquivos de texto em paralelo e conta a frequência de palavras em vários arquivos, divididos pelo `FileGenerator`.

## Funcionalidades

1. **FileGenerator**: Gera um arquivo de texto dividido em várias partes, com palavras aleatórias.
2. **MapReduceController**: Controla o processamento dos arquivos em duas fases:
   - **Map Phase**: Conta as palavras em cada arquivo, cada um processado em uma thread separada.
   - **Reduce Phase**: Consolida a contagem total de cada palavra em threads separadas para cada palavra.
3. **main.py**: Arquivo principal que executa a geração dos arquivos e o processo de contagem de palavras com MapReduce.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.8+
- VS Code ou outro editor de código de sua escolha
- Dependências (não há bibliotecas externas obrigatórias, mas é recomendado o uso de um ambiente virtual)

### Passos

1. Clone este repositório e abra a pasta no VS Code:

   ```bash
   git clone <https://github.com/raedman90/Lab-Map-Reduce>
   cd Lab-Map-Reduce
   ```

2. No terminal, execute o arquivo principal `main.py` para gerar arquivos e realizar a contagem de palavras:

   ```bash
   python main.py
   ```

### Estrutura do Código

#### `file_generator.py`

Classe responsável por gerar palavras aleatórias e dividir o texto em arquivos.

- Parâmetros:
  - **split**: número de arquivos em que o texto será dividido.
  - **N**: número total de palavras a serem geradas.
  - **alphabet**: lista de caracteres permitidos para criar as palavras.
  - **min_size**: tamanho mínimo das palavras.
  - **max_size**: tamanho máximo das palavras.

#### `map_reduce_controller.py`

Controlador que implementa as fases Map e Reduce em threads.

- **Map Phase**: Processa cada arquivo e conta a frequência das palavras.
- **Reduce Phase**: Consolida os resultados da fase Map, somando as frequências de cada palavra.

#### `main.py`

Executa o fluxo do programa:
1. Gera arquivos com `FileGenerator`.
2. Executa o processamento MapReduce com `MapReduceController`.
3. Exibe o resultado da contagem de palavras.

## Exemplo de Saída

Após a execução, você verá a contagem de frequência de cada palavra gerada:

```
Contagem de frequência de palavras:
abc: 3
abcd: 1
deds: 1
```