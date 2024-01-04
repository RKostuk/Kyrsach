import json
import os
import time

from fastapi import APIRouter

from app.services.file_controller import FileController
from app.services.index_procesor import InvertedIndexProcessor
from app.services.structure import LargeJsonHandler

file_cont = FileController('files')
structure_index = LargeJsonHandler()
router = APIRouter()


@router.get("/")
async def start_container():
    return {"message": f"Nice it's work"}

@router.get("/check_index")
async def check_index():
    if structure_index.data is None:
        status = False
    else:
        status = True
    return {"status": status}


@router.get("/search_info_word")
async def search_info_word(word: str):
    data = structure_index.get_value(word)
    return data


@router.get("/search_text_all")
async def search_text_all(word: str):
    info = structure_index.get_value(word)
    if info is None:
        return {"Error": "Not found word"}
    data = info.get("data").copy()
    for i in range(len(data)):
        data[i]["content"] = file_cont.read_file(data[i]["dir"], data[i]["file"])
    return {word: data}


@router.get("/search_text")
async def search_text(word: str, index: int):
    info = structure_index.get_value(word)
    if info is None:
        return {"Error": "Not found word"}
    data = info.get("data")[index]
    content = file_cont.read_file(data["dir"], data["file"])
    return content


@router.get("/refresh_index")
async def refresh_index():
    index_processor = InvertedIndexProcessor()
    # start_time = time.time()
    index_processor.process_directory()
    # end_time = time.time()
    inverted_index = index_processor.get_inverted_index()
    structure_index.write_json(inverted_index)

    # elapsed_time = end_time - start_time
    # print(f"Час виконання: {elapsed_time} секунд")

    return {"message": f"Success"}
