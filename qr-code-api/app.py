from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from qr.generator import generate_qr

app = FastAPI(
    title="QR Code Generator API",
    description="Generate QR codes instantly from any text or URL",
    version="1.0.0"
)

class QRRequest(BaseModel):
    data: str
    box_size: int = 10
    border: int = 4

@app.get("/")
def home():
    return {"message": "Welcome to the QR Code Generator API"}

@app.post("/generate")
def create_qr(request: QRRequest):
    try:
        qr_base64 = generate_qr(request.data, request.box_size, request.border)
        return {
            "success": True,
            "qr_image_base64": qr_base64,
            "note": "You can render this in HTML using <img src='data:image/png;base64,...' />"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
