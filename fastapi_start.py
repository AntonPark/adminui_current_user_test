import uvicorn

uvicorn.run("fapi:fastapi_app", host='0.0.0.0', port=5500, reload=False, log_level="debug",
            workers=1, limit_concurrency=100, limit_max_requests=100)
