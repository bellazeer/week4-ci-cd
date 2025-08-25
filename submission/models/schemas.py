from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime
from typing import Optional
from enum import Enum

class EmployeeStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    TERMINATED = "terminated"

class EmployeeBase(BaseModel):
    employee_id: str
    name: str
    email: EmailStr
    department: str
    position: str
    salary: float
    hire_date: datetime
    status: EmployeeStatus = EmployeeStatus.ACTIVE

class EmployeeCreate(EmployeeBase):
    @field_validator("salary")
    def salary_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Salary must be positive")
        return v

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None
    status: Optional[EmployeeStatus] = None

class EmployeeResponse(EmployeeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # tukar dari ConfigDict ke Config
