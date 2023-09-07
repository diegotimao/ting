# Ting

Este pacote fornece funcionalidades para gerenciar e processar arquivos de texto. Ele inclui uma fila FIFO chamada Queue, funções para importar notícias de um arquivo TXT, processar arquivos, remover arquivos da fila e obter metadados de arquivos processados.

## Documentação

#### Queue: 

Implementação de uma fila FIFO que suporta operações de inserção, remoção, busca e exposição do tamanho.
txt_importer: Função para importar notícias a partir de um arquivo TXT, usando "\n" como separador. Lida com casos de arquivo inexistente ou formato inválido.

#### process: 

Função para processar um arquivo TXT, transformando seu conteúdo em um dicionário que é armazenado na fila. Ignora arquivos já processados e mostra os dados processados.

#### remove: 

Função para remover o primeiro arquivo processado da fila. Exibe uma mensagem se a fila estiver vazia.
file_metadata: Função para obter informações superficiais de um arquivo processado. Exibe uma mensagem se a posição for inválida.

### Testes: 

Testes para a classe PriorityQueue, que armazena arquivos pequenos de forma prioritária.

#### Pacote ting_word_searches:

Este pacote oferece funcionalidades para buscar palavras em arquivos processados. Inclui funções para verificar a existência de uma palavra em todos os arquivos processados e buscar uma palavra, incluindo o conteúdo das linhas onde a palavra foi encontrada.

### funcionalidades

#### exists_word: 

Função para verificar a existência de uma palavra em todos os arquivos processados. Retorna informações sobre os arquivos e as linhas onde a palavra foi encontrada, com busca case insensitive. Se a palavra não for encontrada, retorna uma lista vazia. A fila não é modificada.

#### search_by_word: 

Função para buscar uma palavra em todos os arquivos processados, incluindo o conteúdo das linhas onde a palavra foi encontrada. Mantém a mesma lógica do requisito seis.

## Instalação 

Para instalar os pacotes ting_file_management e ting_word_searches, você pode seguir as etapas abaixo:

1. Clone o repositório do GitHub:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```
Substitua seu-usuario pelo seu nome de usuário do GitHub e seu-repositorio pelo nome do repositório onde os pacotes estão localizados.

2. Acesse o diretório do pacote desejado:

Navegue até o diretório onde os pacotes estão localizados. Por exemplo, para acessar o pacote ting_file_management:

```
cd seu-repositorio/ting_file_management
```

3. Instale as dependências:

Dentro do diretório do pacote, você pode instalar as dependências usando pip. Certifique-se de ter o Python e o pip instalados em seu sistema. Execute o seguinte comando:

```
pip install -r requirements.txt
```

Isso instalará as dependências necessárias para o pacote.

4. Execute o pacote:

Depois de instalar as dependências, você pode executar o pacote usando o seguinte comando:

```
python main.py
```

Siga as instruções específicas do pacote para usar suas funcionalidades.

Repita as etapas 2 a 4 para o outro pacote, se desejar instalá-lo e usá-lo.

OBS: Certifique-se de substituir seu-usuario e seu-repositorio pelos detalhes reais do seu repositório GitHub. Se os pacotes estiverem em repositórios separados, você precisará navegar para o diretório correto de cada pacote e instalar suas dependências individualmente.

Certifique-se também de ter o Python e o pip instalados e configurados corretamente em seu sistema antes de executar esses comandos.

## Executar o projeto

OBS: Certifique-se de que os pré-requisitos para a execução deste pacote estejam instalados e configurados corretamente.

Para executar o pacote ting_file_management, siga as instruções abaixo:

- Abra o terminal.

- Navegue até o diretório do pacote ting_file_management.
- Execute o comando ```python main.py```.

*Para executar o pacote ting_word_searches, siga as instruções abaixo:*
- Navegue até o diretório do pacote ```ting_word_searches```.
- Execute o comando ```python main.py```.

## Dependências

```
-r requirements.txt

pytest==7.1.1
pytest-json==0.4.0
flake8==3.8.4
black==20.8b1
pytest-cov==2.10.1
git+https://github.com/betrybe/pytest-dependency

```