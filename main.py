from typing import Union
import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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