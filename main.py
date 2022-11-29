from fastapi import FastAPI

from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles

from typing import List
from pydantic import BaseModel
from urllib.request import urlopen

from classify import NudenyClassify
from detect import NudenyDetect

classification_model = NudenyClassify()
detection_model = NudenyDetect()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


class Image(BaseModel):
    filename: str
    url: str


@app.post("/classify/")
async def create_upload_files(files: list[UploadFile]):
    return {"predictions": [classification_model.classify(await file.read(), file.filename) for file in files]}

@app.post("/classifyUrl/")
async def create_upload_files(images: List[Image]):
    return {"predictions": [classification_model.classify(urlopen(image.url).read(), image.filename) for image in images]}

@app.post("/draw_bounding_box/")
async def create_upload_files(files: list[UploadFile]):
    return {"predictions": [detection_model.draw_bounding_box(await file.read(), file.filename) for file in files]}


@app.post("/draw_bounding_boxUrl/")
async def create_upload_files(images: List[Image]):
    return {"predictions": [detection_model.draw_bounding_box(urlopen(image.url).read(), image.filename) for image in images]}


@app.post("/censor/")
async def create_upload_files(files: list[UploadFile]):
    return {"predictions": [detection_model.censor_exposed_part(await file.read(), file.filename) for file in files]}


@app.post("/censorUrl/")
async def create_upload_files(images: List[Image]):
    return {"predictions": [detection_model.censor_exposed_part(urlopen(image.url).read(), image.filename) for image in images]}
