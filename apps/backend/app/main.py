from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Info": "Credit Risk backend app"}


@app.get("/health")
def health():
    return {"status": "ok"}
