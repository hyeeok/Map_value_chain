
# MVC Backend
MVC 애플리케이션의 백엔드입니다.


## 기술 스택
- Python 3.10
- FastAPI 0.104.0
- PostgreSQL


## 테스트 실행
테스트를 실행하려면 다음 명령을 실행하세요.

### docker-compose를 사용해 실행

```bash
docker-compose up -d --build
```
사용 가능한 엔드포인트는 http://localhost:8000/docs에서 확인할 수 있습니다.


### 로컬 실행

```bash
virtualenv venv -p python3.10
source venv/Script/activate

pip install -r requirements.txt
uvicorn main:app --reload
```
로컬에서 백엔드 서버를 시작할 경우 별도로 DB 서버를 시작해야 합니다.
이에 대한 대안으로 docker-compose를 사용해 시작한 DB 컨테이너를 사용하는 방법이 있습니다.

1. docker-compose를 사용해 앱 실행
```bash
docker-compose up -d --build
```
2. 백엔드 컨테이너만 정지

3. `.env` 주석처리 혹은 삭제
  - **데이터베이스 URL이 "postgresql://root:admin123@localhost/mvc_db"인 것을 확인**

4. 백엔드 앱 로컬 실행
```bash
virtualenv venv -p python3.10
source venv/Script/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

5. http://localhost:8000/docs 접속해 확인


## Third Party Licenses

...


## Support

...

