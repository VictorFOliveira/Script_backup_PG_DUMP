import subprocess
import datetime
import os
import logging
import shutil
import dotenv

# Carregar variáveis de ambiente do arquivo .env
dotenv.load_dotenv()

# Caminho do diretório de logs
log_dir = os.path.join(os.getcwd(),'logs_backup')

# Verificar se o diretório de logs existe, senão criar
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'backup_postgresql.log')

logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Início do processo de backup')

# Configurações do banco de dados a partir do .env
db_config = {
    'host': os.getenv('db_host'),  # Valor padrão 'localhost' caso não encontre no .env
    'port': os.getenv('port'),
    'dbname': os.getenv('dbname'),
    'user': os.getenv('user'),
    'password': os.getenv('password')
}

backup_dir = 'C:\\Users\\User\\Desktop\\ws-banco_de_dados\\backups'

# Gerar o nome do arquivo de backup com data e hora
data_atual = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
backup_filename = f'{db_config["dbname"]}_backup_{data_atual}.sql'
backup_path = os.path.join(backup_dir, backup_filename)

# Caminho para o arquivo compactado
backup_zip = f'{backup_path}.zip'

# Comando para executar o pg_dump
comando_pg_dump = [
    "pg_dump",
    "-h", db_config['host'],
    "-p", db_config['port'],
    "-U", db_config['user'],
    "-F", "c",
    "-b",
    "-v",
    "-f", backup_path,
    db_config['dbname']
]

# Definir a senha do banco de dados a partir da variável de ambiente
os.environ["PGPASSWORD"] = db_config['password']

try:
    # Executar o comando pg_dump para realizar o backup
    subprocess.run(comando_pg_dump, check=True)
    logging.info(f'Backup do banco {db_config["dbname"]} foi realizado com sucesso! Arquivo: {backup_path}')

    # Compactar o backup gerado em formato zip
    shutil.make_archive(backup_path, 'zip', os.path.dirname(backup_path), os.path.basename(backup_path))
    logging.info(f'Backup comprimido com sucesso! Arquivo: {backup_zip}')

    # Remover o arquivo de backup não comprimido
    os.remove(backup_path)

except subprocess.CalledProcessError as e:
    logging.ERROR(f'Erro ao realizar o backup: {e}')
    print(f'Erro ao criar um backup')
