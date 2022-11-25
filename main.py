from fastapi import FastAPI

from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

from classify import NudenyClassify
from detect import NudenyDetect

app = FastAPI()
classification_model = NudenyClassify()
detection_model = NudenyDetect()


@app.post("/classify/")
async def create_upload_files(files: list[UploadFile]):
    return {"predictions": [classification_model.classify(await file.read(), file.filename) for file in files]}

@app.post("/draw_bounding_box/")
async def create_upload_files(files: list[UploadFile]):
    return {"predictions": [detection_model.draw_bounding_box(await file.read(), file.filename) for file in files]}


@app.post("/censor/")
async def create_upload_files(files: list[UploadFile]):
    return {"predictions": [detection_model.censor_exposed_part(await file.read(), file.filename) for file in files]}