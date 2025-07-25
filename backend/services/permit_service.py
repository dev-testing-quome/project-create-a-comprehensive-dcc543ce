from sqlalchemy.orm import Session
from schemas import PermitCreate, Permit
from models import Permit as PermitModel

def create_permit(db: Session, permit: PermitCreate):
    db_permit = PermitModel(user_id=permit.user_id, permit_type=permit.permit_type, description=permit.description)
    db.add(db_permit)
    db.commit()
    db.refresh(db_permit)
    return Permit.from_orm(db_permit)

def get_permit(db: Session, permit_id: int):
    db_permit = db.query(PermitModel).filter(PermitModel.id == permit_id).first()
    if not db_permit:
        raise HTTPException(status_code=404, detail="Permit not found")
    return Permit.from_orm(db_permit)
