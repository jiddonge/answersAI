#!/bin/bash
# FastAPI 서버와 Streamlit 서버를 동시에 실행

uvicorn main:app --host 0.0.0.0 --port 8000 &
streamlit run app.py --server.port 10000 --server.enableCORS false
