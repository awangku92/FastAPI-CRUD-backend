from app import create_app
from logger import custom_log as clog
import config as conf
import uvicorn, os

os.system("cls") #remove ANSI char in cmd

app = create_app()

if __name__ == "__main__":
    clog('info', 'Starting API service')

    uvicorn.run("run:app", host=conf.APP['APP_IP'], port=conf.APP['API_PORT'], workers=4, reload=True, log_level="info")