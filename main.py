from fastapi import FastAPI

from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles

from classify import NudenyClassify
from detect import NudenyDetect

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
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