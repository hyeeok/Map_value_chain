import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL 연결 정보
db_user = "root"
db_password = "admin123"
db_host = "localhost"
db_port = "5432"
db_name = "mvc_db"

# 엑셀 파일 경로
excel_file_path = "/Users/greta/MVC/backend/반도체하위분류.xlsx"

# PostgreSQL 데이터베이스 연결 설정
db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

# 엑셀 파일을 DataFrame으로 읽기
df = pd.read_excel(excel_file_path)

# DataFrame을 PostgreSQL 데이터베이스에 저장
df.to_sql("deps", engine, if_exists="replace", index=True)
