import os

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}'.format(
    dbuser=os.getenv('AZURE_POSTGRESQL_USER'),
    dbpass=os.getenv('AZURE_POSTGRESQL_PASSWORD'),
    dbhost=os.getenv('AZURE_POSTGRESQL_HOST'),
    dbport=os.getenv('AZURE_POSTGRESQL_PORT', '5432'),
    dbname=os.getenv('AZURE_POSTGRESQL_DATABASE')
)