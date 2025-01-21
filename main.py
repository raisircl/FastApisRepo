from typing import Union
import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class MediaType(BaseModel):
    mtid: int
    mtname: str | None = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/media_types/")
def create_item(data: MediaType):
    """
    Create a new media type in the database.
    """
    try:
        with sqlite3.connect("chinook.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO media_types (MediaTypeId, Name) VALUES (?, ?)", (data.mtid, data.mtname))
            conn.commit()
    except sqlite3.Error as e:
        raise Exception(f"Error creating media type: {e}")
    return {"message": "Media type created successfully."}
    
@app.put("/media_types/{media_type_id}")
def update_media_type(media_type_id: int, data: MediaType):
    """
    Update a media type in the database.
    """
    try:
        with sqlite3.connect("chinook.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE media_types SET Name = ? WHERE MediaTypeId = ?", (data.mtname, media_type_id))
            conn.commit()
    except sqlite3.Error as e:
        raise Exception(f"Error updating media type: {e}")
    return {"message": "Media type updated successfully."}  

@app.delete("/media_types/{media_type_id}")
def delete_media_type(media_type_id: int):
    """
    Delete a media type from the database.
    """
    try:
        with sqlite3.connect("chinook.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM media_types WHERE MediaTypeId = ?", (media_type_id,))
            conn.commit()
    except sqlite3.Error as e:
        raise Exception(f"Error deleting media type: {e}")
    return {"message": "Media type deleted successfully."}

@app.get("/media_types")
def get_all_media_types():
        """
        Fetch all media types from the database.
        """
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT MediaTypeId, Name FROM media_types")
                for row in cursor:
                    mt={"media_type_id":row[0], "media_type_name":row[1]}
                    data_list.append(mt)
        except sqlite3.Error as e:
            raise Exception(f"Error fetching all media types: {e}")
        return data_list