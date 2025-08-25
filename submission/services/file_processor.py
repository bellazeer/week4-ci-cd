from database.config import SessionLocal
from database.crud import create_employee
from models.schemas import EmployeeCreate
import pandas as pd
from typing import Dict, List, Any


class FileProcessor:
    def __init__(self):
        self.required_columns = [
            "employee_id", "name", "email", "department",
            "position", "salary", "hire_date", "status"
        ]

    def process_file(self, file_path: str) -> Dict[str, Any]:
        """Process Excel/CSV file and save to database"""
        try:
            # Read file
            if file_path.endswith(".csv"):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            # Validate required columns
            missing_columns = set(self.required_columns) - set(df.columns)
            if missing_columns:
                return {
                    "processed_count": 0,
                    "errors": [f"Missing required columns: {missing_columns}"]
                }

            # Clean and validate
            cleaned_data, errors = self._clean_data(df)

            processed_count = 0
            db = SessionLocal()
            try:
                for emp_data in cleaned_data:
                    emp = EmployeeCreate(**emp_data)
                    create_employee(emp, db=db)
                    processed_count += 1
                db.commit()
            except Exception as e:
                db.rollback()
                errors.append(f"Database error: {str(e)}")
            finally:
                db.close()

            return {
                "processed_count": processed_count,
                "errors": errors
            }

        except Exception as e:
            return {
                "processed_count": 0,
                "errors": [f"Error reading file: {str(e)}"]
            }

    def _clean_data(self, df: pd.DataFrame) -> tuple[List[Dict], List[str]]:
        """Clean and validate dataframe data"""
        cleaned_data = []
        errors = []

        for index, row in df.iterrows():
            try:
                hire_date = pd.to_datetime(row["hire_date"]).date()
                employee_data = {
                    "employee_id": str(row["employee_id"]),
                    "name": str(row["name"]).strip(),
                    "email": str(row["email"]).strip().lower(),
                    "department": str(row["department"]).strip(),
                    "position": str(row["position"]).strip(),
                    "salary": float(row["salary"]),
                    "hire_date": hire_date,
                    "status": str(row["status"]).lower()
                }
                # Validate with Pydantic
                employee = EmployeeCreate(**employee_data)
                cleaned_data.append(employee.model_dump())
            except Exception as e:
                errors.append(f"Row {index + 1}: {str(e)}")

        return cleaned_data, errors


