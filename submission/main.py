import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Database
from database.config import Base, engine
from models import employee  # penting untuk register model

# Pastikan table SQLAlchemy dibuat masa startup
Base.metadata.create_all(bind=engine)

# Init app
app = FastAPI(
    title="Employee Data Management API",
    description="API for processing Excel files and managing employee data",
    version="1.0.0"
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow semua origin (boleh ketatkan nanti)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Root + Health Check
# =========================
@app.get("/")
async def root():
    return {
        "message": "Employee Data Management API",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# =========================
# Excel API
# =========================
EXCEL_FILE = "sample_employees.xlsx"

@app.get("/employees")
async def get_employees():
    """Return senarai semua employees dari Excel"""
    try:
        df = pd.read_excel(EXCEL_PATH)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Excel file not found")

@app.get("/employee/{emp_id}")
async def get_employee(emp_id: int):
    """Return detail seorang employee ikut ID"""
    try:
        df = pd.read_excel(EXCEL_PATH)
        employee = df[df["id"] == emp_id]
        if not employee.empty:
            return employee.to_dict(orient="records")[0]
        raise HTTPException(status_code=404, detail="Employee not found")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Excel file not found")
