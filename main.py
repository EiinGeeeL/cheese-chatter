#!/usr/bin/env python
import uvicorn
from app import app

#%%
## Main Execution
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)