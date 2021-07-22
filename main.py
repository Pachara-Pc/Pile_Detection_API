from fastapi import FastAPI, File, UploadFile
from typing import List, Tuple
import shutil
import cv2
import numpy as np
import glob
import random

import yolo_object_detection
from fastapi.middleware.cors import CORSMiddleware

import base64
app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.get("/test", )
async def read() :
    return {"message": "test"}

@app.post("/files")
async def create_file(file: bytes = File(...)):
    print(file)
    # return {"file_size": len(file),
    #         "file": len(file)
    #         }
    # return {"file_size": len(file),
    #         "file": len(file)
    #         }

@app.post("/image")
async def image(image: List[UploadFile]= File(...)):
    # print(image)
    allResult = []
    for image in image:
        # print(image.filename)
        with open(f"./write/{image.filename}", "wb") as buffer:
            result = shutil.copyfileobj(image.file, buffer)
            # print(image)
            pile = yolo_object_detection.predict(image.filename,allResult)

    
    return  pile

