from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from modules import fetch_duckduckgo_data


app = FastAPI()
app.mount("/static", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/search", response_class=HTMLResponse)
def search_page(request: Request):
    search_question = request.query_params.get('search_question')

    answer_data = fetch_duckduckgo_data(search_question)
    url = answer_data.get('AbstractURL')
    source = answer_data.get('AbstractSource')

    return templates.TemplateResponse("index.html", {"request": request,
                                                     "url": url,
                                                     "source": source})
