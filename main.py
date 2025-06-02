# -------------------------------
# Basic FastAPI Example with CRUD Scaffold
# -------------------------------
# This app allows creation, listing, and retrieval of simple "Record" items.
# 
# Future Commands for Extension:
# - PUT /records/{record_id}            → Update an existing record
# - DELETE /records/{record_id}         → Delete a record by ID
# - PATCH /records/{record_id}/toggle   → Toggle the 'is_done' status of a record
# - Add data persistence (e.g., DB)
# - Add authentication (e.g., OAuth2, API keys)
# -------------------------------

from fastapi import FastAPI, HTTPException  # Import FastAPI and exception tools
from pydantic import BaseModel              # Import for data validation

# Initialize FastAPI app
app = FastAPI()

# Define data model using Pydantic
class Record(BaseModel):
    text: str = None      # Optional text field (default: None)
    is_done: bool = False # Boolean flag to track completion (default: False)

# In-memory list to store records (acts like a fake database)
records = []

# Root endpoint to confirm the app is running
@app.get("/")
def root():
    return {"message": "Hello, World"}  # Simple hello message

# Endpoint to create a new record (POST /records)
@app.post("/records")
def create_record(record: Record):
    records.append(record)  # Add new record to the in-memory list
    return records           # Return the updated list

# Endpoint to list records with optional limit (GET /records)
@app.get("/records", response_model=list[Record])
def list_records(limit: int = 10):
    return records[0:limit]  # Return up to 'limit' number of records

# Endpoint to get a specific record by its ID (GET /records/{record_id})
@app.get("/records/{record_id}", response_model=Record)
def get_record(record_id: int) -> Record:
    if record_id < len(records):        # Check if record exists
        return records[record_id]       # Return the requested record
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Record {record_id} not found"
        )  # Raise 404 if not found
