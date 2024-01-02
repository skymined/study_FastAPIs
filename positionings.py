from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

positioning_router = APIRouter()

from starlette.responses import HTMLResponse
positioning_template = Jinja2Templates(directory='templates/positionings/')

@positioning_router.get('/forms', response_class=HTMLResponse)
async def positioning_form(request:Request) :
    return positioning_template.TemplateResponse(name='forms.html'
                                        ,context={'request':request})

@positioning_router.get('/grids', response_class=HTMLResponse)
async def positioning_grid(request:Request):
    return positioning_template.TemplateResponse(name='grids.html'
                                            ,context={'request':request})

@positioning_router.get('/standard', response_class=HTMLResponse)
async def positioning_standard(request:Request):
    return positioning_template.TemplateResponse(name='standard.html'
                                            ,context={'request':request})

@positioning_router.get('/tables', response_class=HTMLResponse)
async def positioning_table(request:Request):
    return positioning_template.TemplateResponse(name='tables.html'
                                            ,context={'request':request})
