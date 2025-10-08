# QR Code Generator API

A simple FastAPI-based service to generate QR codes from any text or URL.  
Deployable on Render and monetizable on RapidAPI.

## Features
- Generate QR codes instantly
- Returns Base64 encoded PNG image
- Adjustable box size and border

## API Usage

**POST** `/generate`

### Request:
```json
{
  "data": "https://example.com",
  "box_size": 10,
  "border": 4
}
Response:
{
  "success": true,
  "qr_image_base64": "iVBORw0KGgoAAAANSUhEUgAA...",
  "note": "Use <img src='data:image/png;base64,...' />"
}
