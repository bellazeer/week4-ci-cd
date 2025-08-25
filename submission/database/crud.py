from typing import List, Optional
from sqlalchemy.orm import Session
from database.config import SessionLocal
from models.employee import Employee as EmployeeORM  # ORM model
from models.schemas import EmployeeCreate, EmployeeUpdate  # Pydantic schemas

def create_employee(emp: EmployeeCreate, db: Optional[Session] = None):
    """Create a new employee record."""
    close_db = False
    if db is None:
        db = SessionLocal()
        close_db = True
    try:
        db_emp = EmployeeORM(**emp.model_dump())
        db.add(db_emp)
        db.commit()
        db.refresh(db_emp)
        return db_emp
    finally:
        if close_db:
            db.close()

def create_employee_if_not_exists(data: dict) -> EmployeeORM:
    """Create employee only if employee_id or email not already in DB."""
    db: Session = SessionLocal()
    try:
        existing = db.query(EmployeeORM).filter(
            (EmployeeORM.employee_id == data['employee_id']) | (EmployeeORM.email == data['email'])
        ).first()
        if existing:
            return existing
        emp = EmployeeORM(**data)
        db.add(emp)
        db.commit()
        db.refresh(emp)
        return emp
    finally:
        db.close()

def get_employee(emp_id: int) -> Optional[EmployeeORM]:
    db: Session = SessionLocal()
    try:
        return db.query(EmployeeORM).filter(EmployeeORM.id == emp_id).first()
    finally:
        db.close()

def list_employees(skip: int = 0, limit: int = 100) -> List[EmployeeORM]:
    db: Session = SessionLocal()
    try:
        return db.query(EmployeeORM).offset(skip).limit(limit).all()
    finally:
        db.close()

def update_employee(emp_id: int, payload: EmployeeUpdate) -> Optional[EmployeeORM]:
    db: Session = SessionLocal()
    try:
        emp = db.query(EmployeeORM).filter(EmployeeORM.id == emp_id).first()
        if not emp:
            return None
        for key, value in payload.model_dump(exclude_unset=True).items():
            setattr(emp, key, value)
        db.commit()
        db.refresh(emp)
        return emp
    finally:
        db.close()

def delete_employee(emp_id: int) -> bool:
    db: Session = SessionLocal()
    try:
        emp = db.query(EmployeeORM).filter(EmployeeORM.id == emp_id).first()
        if not emp:
            return False
        db.delete(emp)
        db.commit()
        return True
    finally:
        db.close()
