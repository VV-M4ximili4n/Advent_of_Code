from sqlalchemy import create_engine, text
import pandas as pd


class DatabaseConn:
    def __init__(self, user, password, account_identifier, database_name):
        self.user = user
        self.password = password
        self.account_identifier = account_identifier
        self.database_name = database_name

    def snowflake_conn(self):
        try:
            engine = create_engine(
                f'snowflake://{self.user}:{self.password}@{self.account_identifier}/{self.database_name}'
            )
            with engine.connect() as connection:
                results = connection.execute(text('select current_version()')).fetchone()
                print(results[0])
        finally:
            return engine


db = DatabaseConn(user = 'MSTOLLE', password = 'vamaJan1552!', account_identifier = 'hk85236.west-europe.azure', database_name = 'VV_TEST')
conn = db.snowflake_conn()

result = pd.read_sql_query("select * from information_schema.columns where table_schema = 'DM_KUNDE' ", conn)

print(result['table_name'].unique())
