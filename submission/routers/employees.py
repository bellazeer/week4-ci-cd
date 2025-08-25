from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.schemas import EmployeeCreate, EmployeeResponse, EmployeeUpdate  # ✅ ambil dari schemas
from services import employee_service

router = APIRouter(prefix="/employees", tags=["employees"])

@router.get("/", response_model=List[EmployeeResponse])
async def list_employees():
    return employee_service.list_all()

@router.post("/", response_model=EmployeeResponse)
async def create_employee(payload: EmployeeCreate):
    created = employee_service.create(payload)
    return created

@router.get("/{emp_id}", response_model=EmployeeResponse)
async def get_employee(emp_id: int):
    found = employee_service.get(emp_id)
    if not found:
        raise HTTPException(status_code=404, detail="Employee not found")
    return found

@router.put("/{emp_id}", response_model=EmployeeResponse)
async def update_employee(emp_id: int, payload: EmployeeUpdate):
    updated = employee_service.update(emp_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated

@router.delete("/{emp_id}")
async def delete_employee(emp_id: int):
    removed = employee_service.remove(emp_id)
    if not removed:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "deleted"}
