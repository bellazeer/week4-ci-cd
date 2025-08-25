from typing import Optional
from database.crud import (
    get_employee,
    list_employees,
    create_employee,
    update_employee,
    delete_employee
)
from models.schemas import EmployeeCreate, EmployeeUpdate  # ✅ ambil dari schemas

# Thin wrapper to keep business logic separate

def create(emp: EmployeeCreate):
    return create_employee(emp)

def get(emp_id: int):
    return get_employee(emp_id)

def list_all(skip: int = 0, limit: int = 100):
    return list_employees(skip=skip, limit=limit)

def update(emp_id: int, payload: EmployeeUpdate):
    return update_employee(emp_id, payload)

def remove(emp_id: int):
    return delete_employee(emp_id)
