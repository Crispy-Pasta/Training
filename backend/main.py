from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import os

##### TEST 12345
app = FastAPI()

# Load DB credentials from environment
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "test")

@app.get("/api/ping")
def ping_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        conn.close()
        return {"status": "connected"}
    except mysql.connector.Error as e:
        return {"status": "error", "details": str(e)}

# Define request body model for POST /api/display
class DisplayTextRequest(BaseModel):
    text: str

@app.post("/api/output")
def display_text(request: DisplayTextRequest):
    print(f"Received text: {request.text}")
    return {"message": request.text}
