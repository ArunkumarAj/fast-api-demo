from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Record(BaseModel):
    text: str = None
    is_done: bool = False


records = []


@app.get("/")
def root():
    return {"message": "Hello, World"}


@app.post("/records")
def create_record(record: Record):
    records.append(record)
    return records


@app.get("/records", response_model=list[Record])
def list_records(limit: int = 10):
    return records[0:limit]


@app.get("/records/{record_id}", response_model=Record)
def get_record(record_id: int) -> Record:
    if record_id < len(records):
        return records[record_id]
    else:
        raise HTTPException(status_code=404, detail=f"Record {record_id} not found")