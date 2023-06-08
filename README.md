# 실행 방법
```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python app.py
```

# MVC App
본 애플리케이션은 python dash 프레임워크를 기반으로 합니다.

## 설치
본 애플리케이션 실행에 필요한 구성요소는 다음과 같습니다.
- Python 3.8
- Docker (선택)

### 로컬 설치

1. 리포지토리를 복제합니다:
```bash
git clone https://github.com/... .
```

2. 가상 환경을 생성하고 활성화합니다.

```bash
python -m venv venv
source venv/bin/activate
```

3. 필요한 패키지를 설치합니다:
```bash
cd dash

pip install -r requirements.txt
```
4. 애플리케이션을 실행합니다:
```bash
# gunicorn 미사용
python app.py

# gunicorn 사용 (linux에서만 가능)
gunicorn -c gunicorn_config.py app:server
```

5. 브라우저에서 http://localhost:8050으로 접속하여 애플리케이션을 확인합니다.


### Docker 설치
1. 리포지토리를 다운로드 하고 해당 위치로 이동합니다:
```bash
git clone https://github.com/... .
```

2. Docker Compose를 사용하여 애플리케이션을 실행합니다:
```bash
docker-compose build
docker-compose up -d
```

3. 브라우저에서 http://localhost:8050으로 접속하여 애플리케이션을 확인합니다.

## 사용법
본 애플리케이션은 다음 엔드포인트를 제공합니다:

- `/scatter`
- `/ridgeline`


## 개발
본 애플리케이션은 다음 기술 스택으로 개발되었습니다:
- Python
- Dash
- gunicorn
- nginx

개발을 진행 시 다음 사항을 유의하시기 바랍니다:

- 적절한 환경 설정 파일 (예: .env)을 사용하여 환경변수를 관리하세요.
- 적절한 유닛 테스트를 작성하여 코드의 정확성을 검증하세요.
- 개발을 시작하기 전에 의존성을 설치하고 환경을 설정하세요.
- 코드를 변경한 경우, 변경 사항을 깃에 커밋하고 관리하세요.


## 라이선스
이 프로젝트는 *** 라이선스 하에 배포되었습니다. 라이선스 전문은 LICENSE 파일을 참조하세요.
