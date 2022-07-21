from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from pydantic import BaseModel
import json
import fastapi.routing as far

app = FastAPI(version='1.0.0', title="app")
templates = Jinja2Templates(directory="templates")

class Post(BaseModel):
    title: str
    body: str
    userID: int
    postID: int

posts_db = [
    {
        "title": "Hello",
        "body": "World",
        "userID": 1,
        "postID": 1
    },
    {
        "title": "Bye",
        "body": "World",
        "userID": 1,
        "postID": 2
    }
]

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return { 'hello': "world" }

@app.post("/posts/post/")
async def create_post(post: Post):
    posts_temp = posts_db
    posts_temp.append(post)
    return posts_temp

@app.get("/posts/")
async def get_posts() -> dict:
    posts = str(posts_db).replace("'", "\"")
    json_posts = json.loads(posts)
    return json_posts

@app.get("/posts/get/{post_id}/")
async def get_posts_by_id(post_id: int) -> dict:
    posts = str(posts_db[post_id-1]).replace("'", "\"")
    post = json.loads(posts)
    return post

@app.get("/blog/{post_id}/", response_class=HTMLResponse)
async def display_posts_by_id(request: Request, post_id: int):
    post = posts_db[post_id-1]
    return templates.TemplateResponse("blog.html", {"request": request, "Title": post["title"], "Body": post["body"], "UserID": post["userID"], "PostID": post["postID"]})
