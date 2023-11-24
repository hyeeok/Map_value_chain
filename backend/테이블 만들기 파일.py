import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL 연결 정보
db_user = "root"
db_password = "admin123"
db_host = "localhost"
db_port = "5432"
db_name = "mvc_db"

# 엑셀 파일 경로
excel_file_path = "/Users/greta/MVC/backend/MVC_가상데이터.xlsx"

# 엑셀 파일을 DataFrame으로 읽기 (세 번째 행부터 컬럼으로, 네 번째 행부터 데이터 로드)
df = pd.read_excel(excel_file_path, header=2, skiprows=[0, 1])

# PostgreSQL 데이터베이스 연결 설정
db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

# DataFrame을 PostgreSQL 데이터베이스에 저장
df.to_sql("company_detail", engine, if_exists="replace", index=True)
