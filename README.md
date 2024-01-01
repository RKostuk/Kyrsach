# API Invert Index

The invert index object represents information about teams with the following attributes:

- **INVER INDEX** Models:
    - **word**: str
    - **count**: int
    - **data**: list[dict]
        - **dir**: str
        - **file**: str
        - **count**: int
        - **positions**: list[int] 

The structure is as follows:

```json
{
  "word": {
    "count": 1,
    "data": [
      {
        "dir": "dir_name",
        "file": "file_name",
        "count": 1,
        "positions": [
          1
        ]
      }
    ]
  }
}
```
## Testing the API

To test this API, you can use the interactive Swagger documentation. To do this, click on the following link:

[Swagger Documentation and API Testing](http://127.0.0.1:8000/docs#/)

Swagger provides a convenient interface to make requests to the API. You can check available endpoints, see what parameters they expect, and even try out real requests.

# Getting Started
**Clone the project from GitHub**:
   ```bash
   git clone https://github.com/RKostuk/Kyrsach.git
   ```
To run the project, follow these steps:

1. **Create a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    ```

    - **Activate the virtual environment**:

      - For Windows:

        ```bash
        .\venv\Scripts\activate
        ```

      - For Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

2. **Install project dependencies**:

    ```bash
    pip install -r requirements.txt
    ```
   
3. **Run the project**:

    ```bash
    python run.py
    ```

    If using a virtual environment, make sure it's activated before running the project.

4. **Deactivate the virtual environment (if used)**:

    ```bash
    deactivate
    ```

The API server will start locally at `http://localhost:8000/`.

## API Endpoints

### Checking the performance
Endpoint: `http://localhost:8000/`  
Method: `GET`

Response:
```json
{
  "message": "Nice it's work"
}
```

### Where this word is found
Endpoint: `http://localhost:8000/search_info_word`
Method: `GET`
Request query params:
```
    word="str"
```

Response:
```json
{
  "count": "int",
  "data": [
    {
      "dir": "str",
      "file": "str",
      "count": "int",
      "positions": [
        "int"
      ]
    }
  ]
}
```

### Where this word is found and their texts
Endpoint: `http://localhost:8000/search_text_all`
Method: `GET`
Request query params:
```
    word="str"
```

Response:
```json
{
  "count": "int",
  "data": [
    {
      "dir": "str",
      "file": "str",
      "count": "int",
      "positions": [
        "int"
      ],
      "content": "str"
    }
  ]
}
```

### Search for text by index
Endpoint: `http://localhost:8000/search_text`
Method: `GET`
Request query params:
```
    word="str"&index: "int"
```

Response:
```
    "str"
```

### Search for text by index
Endpoint: `http://localhost:8000/refresh_index`
Method: `GET`
Response:
```json
{
  "message": "str"
}
```
