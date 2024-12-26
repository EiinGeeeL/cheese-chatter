#!/usr/bin/env python
import subprocess

#%%
## Main Execution
if __name__ == "__main__":
    command = ["langgraph", "dev", "--port", "8000", "--host", "0.0.0.0"]
    subprocess.run(command, check=True)