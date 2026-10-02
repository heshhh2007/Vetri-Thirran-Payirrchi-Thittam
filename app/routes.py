from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserPlan
from app.ai.gemini_generator import generate_base_plan

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@router.post("/generate", response_class=HTMLResponse)
def create_plan(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    goal: str = Form(...),
    dietary_pref: str = Form(...),
    db: Session = Depends(get_db)
):
    plan_text = generate_base_plan(name, age, goal, dietary_pref)
    
    new_user = UserPlan(
        name=name,
        age=age,
        goal=goal,
        dietary_pref=dietary_pref,
        workout_plan=plan_text
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={"user": new_user}
    )

@router.get("/users", response_class=HTMLResponse)
def list_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(UserPlan).order_by(UserPlan.created_at.desc()).all()
    return templates.TemplateResponse(
        request=request,
        name="all_users.html",
        context={"users": users}
    )