
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import create_database, SessionLocal
from database.models import Draft
from schemas.draft import DraftCreate, DraftUpdate, DraftResponse


app = FastAPI(
    title="DraftMaster API",
    description="API для анализа драфтов Dota 2",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    create_database()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "DraftMaster API is running"}


@app.get("/api/v1/health")
def health():
    return {"status": "ok"}


@app.get(
    "/api/v1/drafts",
    response_model=list[DraftResponse]
)
def get_drafts(db: Session = Depends(get_db)):
    return db.query(Draft).all()


@app.get(
    "/api/v1/drafts/{draft_id}",
    response_model=DraftResponse
)
def get_draft(draft_id: int, db: Session = Depends(get_db)):
    draft = db.query(Draft).filter(Draft.id == draft_id).first()

    if draft is None:
        raise HTTPException(
            status_code=404,
            detail="Draft not found"
        )

    return draft


@app.post(
    "/api/v1/drafts",
    response_model=DraftResponse,
    status_code=status.HTTP_201_CREATED
)
def create_draft(data: DraftCreate, db: Session = Depends(get_db)):
    draft = Draft(
        user_id=data.user_id,
        title=data.title
    )

    db.add(draft)
    db.commit()
    db.refresh(draft)

    return draft


@app.put(
    "/api/v1/drafts/{draft_id}",
    response_model=DraftResponse
)
def update_draft(
    draft_id: int,
    data: DraftUpdate,
    db: Session = Depends(get_db)
):
    draft = db.query(Draft).filter(Draft.id == draft_id).first()

    if draft is None:
        raise HTTPException(
            status_code=404,
            detail="Draft not found"
        )

    update_data = data.model_dump(exclude_unset=True)

    if "user_id" in update_data and update_data["user_id"] is not None:
        draft.user_id = update_data["user_id"]

    if "title" in update_data:
        draft.title = update_data["title"]

    db.commit()
    db.refresh(draft)

    return draft


@app.delete(
    "/api/v1/drafts/{draft_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_draft(draft_id: int, db: Session = Depends(get_db)):
    draft = db.query(Draft).filter(Draft.id == draft_id).first()

    if draft is None:
        raise HTTPException(
            status_code=404,
            detail="Draft not found"
        )

    db.delete(draft)
    db.commit()
