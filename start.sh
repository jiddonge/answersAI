#!/bin/bash
# FastAPI 백그라운드 실행
uvicorn server:app --host 0.0.0.0 --port 8000 &

# Streamlit 포어그라운드 실행 (Render는 포그라운드 프로세스가 종료되면 서비스 종료됨)
streamlit run app.py --server.port 10000 --server.enableCORS false
