from fastapi import FastAPI

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
from fastapi import Request
from starlette.responses import HTMLResponse
main_tem = Jinja2Templates(directory='templates/')

@app.get("/", response_class=HTMLResponse)
async def main(request:Request):
    return main_tem.TemplateResponse(name="main.html"
                                 ,context={'request':request})

from gadgets import gadget_router as main_gadget_router
app.include_router(main_gadget_router, prefix='/gadgets') # 이 아이의 이름이 기본값으로 됨


from positionings import positioning_router as main_positioning_router
app.include_router(main_positioning_router, prefix='/positionings')

from routes.users import router as users_router
app.include_router(users_router, prefix='/users')


# from fastapi import Request
# from fastapi.templating import Jinja2Templates # html을 모아서 어떤 파일을 나오게 함

# #html틀이 있는 폴더 위치
# templates = Jinja2Templates(directory="templates/")  

# @app.get("/") # 이것과 이 아래 root 부분이 상대의 값을 받아들이는 부분 @는 '얘를 어느식으로 호출해야하는 지 설정할 수 있게 만들어주는 부분임 / : 업무에 따라 동작하도록 만들어둠
# async def root(request:Request): #이 변수는 type이 request라는 것을 알려주는 것
#     # return {"message": "SKY WORLD"} 
#     #html틀로 호출(미리 만들어져 있어야 함)
#     return templates.TemplateResponse('index.html'
#                                       ,{'request':request})



