import uvicorn
from app.core.config import Config

if __name__ == "__main__":
    uvicorn.run(
        Config.path,
        host=Config.host,
        port=Config.port,
        reload=Config.reload
    )
