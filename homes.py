from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

from starlette.responses import HTMLResponse
templates = Jinja2Templates(directory="templates/")  

@router.get("/")
async def home(request:Request):
    pass
    return templates.TemplateResponse(name="homes/standard.html"
                                      ,context={"request":request})



# /home
@router.get("/", response_class=HTMLResponse) # 들어오는 경로와 나가는 것을 지정해주는 것
async def home():
    html = '<body> <h2> It\'s Home. </h2> </body>'
    return html

# /home/list
@router.get("/list", response_class=HTMLResponse) # 어노테이션(웹에서 업무 호출)
async def home_list():
    html = "<body> <h2> It's Home List. </h2> </body>"
    return html 

