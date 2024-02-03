from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import debugpy
from typing import List
from tempfile import NamedTemporaryFile
import whisper
import torch

app = FastAPI()
# Allow all origins for CORS (you can customize this based on your requirements)
origins = ["*"]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
debugpy.listen(("0.0.0.0", 5678))

torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model = whisper.load_model("base", device=DEVICE)


@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Read the content of your HTML file
    with open("./src/index.html", "r") as file:
        html_content = file.read()

    return HTMLResponse(content=html_content)


@app.post("/transcribe", response_class=JSONResponse)
async def handler(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=404, detail='No files were provided')


    results = []
    for file in files:
        with NamedTemporaryFile(delete=True) as temp:
            with open(temp.name, "wb") as temp_file:
                temp_file.write(file.file.read())
            result = model.transcribe(temp.name)
            results.append(
                {
                    "filename": file.filename,
                    "transcript": result["text"]
                }
            )
    return JSONResponse(content={"results": results})
