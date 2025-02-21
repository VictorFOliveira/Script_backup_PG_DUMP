# Backup PostgreSQL Automático

Este projeto realiza backups automáticos de um banco de dados PostgreSQL, armazenando-os em um diretório especificado. O backup é comprimido em formato `.zip` para otimizar o armazenamento. Além disso, a configuração do banco de dados é carregada a partir de um arquivo `.env` para manter as credenciais seguras.

## Funcionalidade

1. **Backup do banco de dados**: Utiliza o comando `pg_dump` para realizar o backup do banco de dados PostgreSQL.
2. **Compressão do backup**: O arquivo de backup gerado é comprimido em um arquivo `.zip`.
3. **Armazenamento do log**: Um arquivo de log é gerado para registrar todas as etapas do processo de backup.
4. **Configuração flexível**: A configuração do banco de dados, como host, porta, nome do banco de dados, usuário e senha, é carregada a partir de um arquivo `.env`.

## Tipos de Backup com `pg_dump`

O `pg_dump` é uma ferramenta poderosa que permite realizar backups completos ou parciais de um banco de dados PostgreSQL. Ele oferece diferentes opções para personalizar o que será incluído no backup. Abaixo estão os principais tipos de backup que você pode realizar com o `pg_dump`:

1. **Backup Completo**: Inclui o esquema do banco de dados (tabelas, índices, funções, etc.) e os dados (todas as linhas de todas as tabelas).
   - Utiliza o comando: `pg_dump -F c -b -v -f backup.sql nome_do_banco`

2. **Backup de Estrutura (Schema Only)**: Apenas a estrutura do banco de dados é exportada, ou seja, as definições de tabelas, índices, funções, etc., mas sem os dados das tabelas.
   - Opção: `-s` (schema only).
   - Exemplo de comando: `pg_dump -s -F c -v -f backup_schema.sql nome_do_banco`

3. **Backup de Dados (Data Only)**: Apenas os dados das tabelas são exportados, sem a definição das tabelas ou quaisquer outros objetos do banco de dados.
   - Opção: `-a` (data only).
   - Exemplo de comando: `pg_dump -a -F c -v -f backup_data.sql nome_do_banco`

4. **Backup de Tabelas Específicas**: Você pode especificar tabelas individuais para incluir no backup, usando a opção `-t`.
   - Exemplo de comando: `pg_dump -t tabela1 -t tabela2 -F c -v -f backup_tables.sql nome_do_banco`

5. **Backup de Índices, Funções e Procedimentos**: O `pg_dump` inclui, por padrão, índices, funções e outros objetos do banco de dados ao realizar o backup completo.
   - Para garantir que as funções e os índices também sejam incluídos, não é necessário usar opções adicionais, pois eles são incluídos no backup por padrão.

6. **Backup de Grandes Objetos**: O `pg_dump` pode ser configurado para incluir grandes objetos (LOBs), como arquivos binários ou dados de imagem.
   - Opção: `-b` (incluir grandes objetos).
   - Exemplo de comando: `pg_dump -b -F c -v -f backup_with_large_objects.sql nome_do_banco`

## Requisitos

Antes de executar este script, certifique-se de ter os seguintes requisitos:

- **Python 3.x**: Para rodar o script Python.
- **pg_dump**: O utilitário de backup do PostgreSQL deve estar instalado e acessível no PATH.
- **Pacotes Python**:
  - `python-dotenv`: Para carregar as variáveis de ambiente do arquivo `.env`.
  - `shutil`, `subprocess`, `datetime`, `os`, `logging`: Bibliotecas padrão do Python usadas para manipulação de arquivos, logs e execução de comandos.

Você pode instalar o pacote necessário com:

```bash
pip install python-dotenv
