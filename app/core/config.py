class Config:
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
    path: str = "app.main:app"


class ConfigInverIndex:
    dir: str = "files"
    thread: int = 8
