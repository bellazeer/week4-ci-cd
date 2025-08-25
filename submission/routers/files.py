from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from services.file_processor import FileProcessor

router = APIRouter(prefix="/files", tags=["files"])
file_processor = FileProcessor()

@router.post("/upload-excel")
async def upload_excel_file(file: UploadFile = File(...)):
    """Upload and process Excel/CSV file containing employee data"""
    
    # Validate file type
    if not file.filename.endswith((".xlsx", ".xls", ".csv")):
        raise HTTPException(status_code=400, detail="Only Excel and CSV files are allowed")
    
    try:
        # Ensure uploads folder exists
        os.makedirs("uploads", exist_ok=True)
        file_path = os.path.join("uploads", file.filename)

        # Save uploaded file
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # Process file
        result = file_processor.process_file(file_path)  # ⚡ kalau process_file biasa (sync)

        return {
            "filename": file.filename,
            "message": "File processed successfully",
            "processed_records": result.get("processed_count", 0),
            "errors": result.get("errors", [])
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
