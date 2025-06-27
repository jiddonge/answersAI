from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse, FileResponse
import uuid, csv, os

app = FastAPI()

class LogData(BaseModel):
    session_id: str
    사용자유형: str
    선택항목: str
    추천정책: str
    추천날짜: str
    정책최종수정일: str

def save_to_csv(log_data, file_path='chat_log.csv'):
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=log_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(log_data)

@app.post("/log")
async def log_handler(data: LogData):
    log_dict = data.dict()
    save_to_csv(log_dict)
    print("✅ Webhook 수신됨:", log_dict)
    return {"message": "로그 저장 완료"}

@app.get("/log-file")
async def get_log_file():
    file_path = "chat_log.csv"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='text/csv')
    return JSONResponse(content={"message": "chat_log.csv가 아직 없습니다."}, status_code=404)

@app.get("/")
async def root():
    return {"message": "FastAPI Webhook 서버 작동 중 ✅"}
