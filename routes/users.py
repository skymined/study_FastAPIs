from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

from starlette.responses import HTMLResponse
templates = Jinja2Templates(directory="/templates/")  

# 이미 해당 폴더에 들어가는 모든 요소들은 "/users"가 기본으로 들어감

# 회원 가입
@router.get("/inserts", response_class=HTMLResponse) # 어노테이션(웹에서 업무 호출)
async def insert(request:Request):
    return templates.TemplateResponse(name="users/inserts.html",
                                      context={'request':request})
