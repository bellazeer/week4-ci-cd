from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from models.employee import EmployeeStatus


Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(20), unique=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    department = Column(String(50), index=True)
    position = Column(String(50), nullable=False)
    salary = Column(Float)
    hire_date = Column(DateTime)
    status = Column(Enum(EmployeeStatus), default=EmployeeStatus.ACTIVE)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
