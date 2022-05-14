from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from first import do_request

app = FastAPI()
app.mount("/static", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse(
        'index.html', {"request": request}
    )


@app.get("/search", response_class=HTMLResponse)
def search_page(request: Request):
    search_request = request.query_params.get('search')
    duck_request = do_request(search_request)
    abstract_source = duck_request.get('AbstractSource')
    abstract_url = duck_request.get('AbstractURL')
    return templates.TemplateResponse(
        'index.html', context={"request": request,
                               "abstract_source": abstract_source,
                               "abstract_url": abstract_url}
    )
