from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas import PermitCreate, Permit
from services import permit_service

router = APIRouter()

@router.post("/", response_model=Permit, status_code=status.HTTP_201_CREATED)
def create_permit(permit: PermitCreate, db: Session = Depends(get_db)):
    return permit_service.create_permit(db, permit)

@router.get("/{permit_id}", response_model=Permit)
def get_permit(permit_id: int, db: Session = Depends(get_db)):
    return permit_service.get_permit(db, permit_id)
