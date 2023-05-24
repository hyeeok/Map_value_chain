bind = "0.0.0.0:8050"  # 바인딩할 IP 및 포트
workers = 4  # 워커(worker) 프로세스 수
timeout = 60  # 요청 타임아웃 (초)

# 로깅 설정
accesslog = "/var/log/gunicorn_access.log"  # 액세스 로그 파일 경로
errorlog = "/var/log/gunicorn_error.log"  # 에러 로그 파일 경로
loglevel = "info"  # 로그 레벨 ('debug', 'info', 'warning', 'error', 'critical')

# Keep-alive 설정
keepalive = 2  # 연결 유지 시간 (초)
keepalive_timeout = 120  # keep-alive 타임아웃 (초)
