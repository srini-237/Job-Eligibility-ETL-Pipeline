import pymysql
import pandas as pd
from datetime import datetime
import os

def fetch_data_from_mysql():
    mysql_config = {
        'host': 'localhost',
        'user': 'username',
        'password': 'your_password',
        'database': 'job_portal'
    }

    connection = pymysql.connect(**mysql_config)
    query = 'SELECT * FROM applicants'
    df = pd.read_sql(query, connection)
    connection.close()
    return df

def check_eligibility(row):
    allowed_degrees = ['B.Sc', 'B.E', 'B.Com']
    if row['age'] >= 18 and row['degree'] in allowed_degrees:
        return 'Qualified'
    else:
        return 'Not Eligible'

def write_data_to_file(df):
    output_dir = '/home/srinivasan/extract1'
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f'etl_output_{timestamp}.csv'
    file_path = os.path.join(output_dir, file_name)
    df.to_csv(file_path, index=False)
    print(f'Data written to {file_path}')

def etl_process():
    df = fetch_data_from_mysql()
    df['status'] = df.apply(check_eligibility, axis=1)
    shortlisted_df = df[df['status'] == 'Qualified'].copy()
    shortlisted_df['shortlist_date'] = datetime.now()
    write_data_to_file(shortlisted_df)

if __name__ == "__main__":
    etl_process()
