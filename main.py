from fastapi import FastAPI

from routers.studentRouter import router as student_router

app = FastAPI(title="Student API")

app.include_router(student_router)


@app.get("/")
def read_root():
    return {"message": "backend is running !!!"}
