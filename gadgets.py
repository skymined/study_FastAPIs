from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

gadget_router = APIRouter()

from starlette.responses import HTMLResponse
gadget_template = Jinja2Templates(directory='templates/gadgets/')

@gadget_router.get('/buttons', response_class=HTMLResponse)
async def gadget_button(request:Request) :
    return gadget_template.TemplateResponse(name='buttons.html'
                                        ,context={'request':request})

@gadget_router.get('/cards', response_class=HTMLResponse)
async def gadget_card(request:Request):
    return gadget_template.TemplateResponse(name='cards.html'
                                            ,context={'request':request})

@gadget_router.get('/colors', response_class=HTMLResponse)
async def gadget_color(request:Request):
    return gadget_template.TemplateResponse(name='colors.html'
                                            ,context={'request':request})

@gadget_router.get('/containers', response_class=HTMLResponse)
async def gadget_container(request:Request):
    return gadget_template.TemplateResponse(name='containers.html'
                                            ,context={'request':request})

