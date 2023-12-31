import json
import os

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


@router.get("/search_info_word")
async def start_container(word: str):
    data = structure_index.get_value(word)
    return data


@router.get("/search_text_all")
async def start_container(word: str):
    info = structure_index.get_value(word)
    if info is None:
        return {"Error": "Not found word"}
    data = info.get("data").copy()
    for i in range(len(data)):
        data[i]["content"] = file_cont.read_file(data[i]["dir"], data[i]["file"])
    return {word: data}


@router.get("/search_text")
async def start_container(word: str, index: int):
    info = structure_index.get_value(word)
    if info is None:
        return {"Error": "Not found word"}
    data = info.get("data")[index]
    content = file_cont.read_file(data["dir"], data["file"])
    return content


@router.get("/refresh_index")
async def start_container():
    index_processor = InvertedIndexProcessor('files')
    index_processor.process_directory()
    inverted_index = index_processor.get_inverted_index()
    structure_index.write_json(inverted_index)
    return {"message": f"Success"}
