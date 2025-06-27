#!/bin/bash
streamlit run app.py --server.port 10000 --server.enableCORS false &
uvicorn server:app --host 0.0.0.0 --port 8000
