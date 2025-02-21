import subprocess
import datetime
import os
import logging
import shutil
import dotenv


dotenv.load_dotenv()

def create_path_logs():
    log_dir = os.path.join(os.getcwd(),'logs_backup')

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, 'logs_postgresql.sql')
    
    logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Inicio do processo de backup')


def configuration_enviroment():
    db_config = {
    'host': os.getenv('db_host'), 
    'port': os.getenv('port'),
    'dbname': os.getenv('dbname'),
    'user': os.getenv('user'),
    'password': os.getenv('password')
}
    
    for key, value in db_config.items():
        if not value:
            logging.error(f'Falha na configuração da variável de ambiente {key} não está definida')
            raise ValueError(f'A variável de ambiente {key}, não está definida corretamente')
        else:
            logging.info(f'Configuração verificada com sucesso: {key}={value}')
    
    return db_config


def executeBackup(db_config):

    data_atual = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f'{db_config['dbname']}_backup_{data_atual}.sql'
    backup_dir = 'C:\\Users\\User\\Desktop\\ws-banco_de_dados\\backups'
    backup_path = os.path.join(backup_dir, backup_filename)

    backup_zip = f'{backup_path}'

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

    os.environ["PGPASSWORD"] = db_config['password']

    try:
        subprocess.run(comando_pg_dump, check=True)
        logging.info(f'Backup do banco {db_config['dbname']} foi realizado com sucesso! Arquivo: {backup_path}')

        shutil.make_archive(backup_path, 'zip', os.path.dirname(backup_path), os.path.basename(backup_path))
        logging.info(f'Backup comprimido com sucesso! Arquivo{backup_zip}')    

        os.remove(backup_path)

    except subprocess.CalledProcessError as e:
        logging.error(f'Erro ao realizar backup: {e}' )
        print('Erro ao criar backup')


def main():
    create_path_logs()
    db_config = configuration_enviroment()
    executeBackup(db_config)

if __name__ == '__main__':
    main()

    