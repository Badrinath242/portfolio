from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/Badrinath", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Route to render the index.html template.
    """
    return templates.TemplateResponse("index.html", {"request": request, "title": "Badrinath"})


@app.get("/Home", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Route to render the index.html template.
    """
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})


@app.get("/About", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Route to render about.html template.
    """
    return templates.TemplateResponse("about.html", {"request": request, "title": "About"})


@app.get("/Resume", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Route to render the resume.html template.
    """
    return templates.TemplateResponse("resume.html", {"request": request, "title": "Resume"})



