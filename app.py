from fastapi import FastAPI, Request, Response, Header, status, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

from logger import custom_log as clog #for logging error
from model import CRUD
from db.user import User
from db.schemas import UserIn, UserOut
from db.db import Base, engine
from typing import List

import config as conf
import os, time, json

def create_app():
    # Init the database once when the app init
    Base.metadata.create_all(engine)

    app = FastAPI(
        title='FastAPI',
        description=conf.DESC
    )
    app.mount("/static", StaticFiles(directory="static"), name="static") # prod use (directory="/home/restapi/target-api-tnt-fastapi/static")
    app.add_middleware(
        CORSMiddleware,
        allow_origins =conf.CORS['ORIGINS'],
        allow_methods =conf.CORS['METHODS'],
        allow_headers =conf.CORS['HEADERS'],
    )

    # middleware for API timing (before/after request)
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.time()
        try:
            # Search.ping()
            pass
        except Exception as e:
            clog('error', str(e))
            print(str(e))
            return Response('Error : '+str(e))

        response = await call_next(request)
        process_time = time.time() - start_time
        print('Time taken to execute code: '+str(process_time)+' sec' )
        response.headers["Execution-Time"] = str(process_time)
        return response

    # @app.exception_handler(Exception)
    # async def validation_exception_handler(request, err):
    #     base_error_message = f"Failed to execute: {request.method}: {request.url}"
    #     # Change here to LOGGER
    #     print(base_error_message)
    #     return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

    summ = 'Test API'
    @app.get('/', tags=["Stable Version"], summary=summ)
    async def root(request : Request):
        ''' 
        Return string & ES Index if API is running
        '''
        return JSONResponse("Hello FastAPI!")

    summ = 'Create user'
    @app.post('/add', tags=["Stable Version"], summary=summ, status_code=status.HTTP_201_CREATED)
    async def create_user(request : Request, user : UserIn):
        ''' 
        Create new user and return status
        '''
        try:
            # user = User(name, phoneno)
            result = CRUD.create_user(user)  

        except Exception as e:
            clog('error', str(e))
            return JSONResponse('Error : '+str(e))

        return JSONResponse(result)

    summ = 'Read user'
    @app.get('/view/{id}', tags=["Stable Version"], response_model=UserOut, summary=summ)
    async def read_user(request : Request, id : int):
        ''' 
        Return 1 user
        '''
        try:
            result = CRUD.read_user(id)

            if not result:
                raise HTTPException(status_code=404, detail=f"ID {id} does not exist!")

        except Exception as e:
            clog('error', str(e))
            raise HTTPException(status_code=404, detail=f"ID {id} does not exist!")

        return JSONResponse(jsonable_encoder(result))

    summ = 'Read all user'
    @app.get('/viewall', tags=["Stable Version"], response_model=List[UserOut], summary=summ)
    async def read_all_user(request : Request):
        ''' 
        Return list of user
        '''
        try:
            result = CRUD.read_all_user()  

        except Exception as e:
            clog('error', str(e))
            return JSONResponse('Error : '+str(e))

        return JSONResponse(jsonable_encoder(result))

    summ = 'Update API'
    @app.put('/edit/{id}', tags=["Stable Version"], summary=summ, response_model=UserOut)
    async def update_user(request : Request, id: int, name: str = None, phoneno: str = None):
        ''' 
        Update user details and return status 
        '''
        try:
            result = CRUD.edit_user(id, name, phoneno)

            if not result:
                raise HTTPException(status_code=404, detail=f"ID {id} does not exist!")

        except Exception as e:
            clog('error', str(e))
            raise HTTPException(status_code=404, detail=f"ID {id} does not exist!")

        return JSONResponse(jsonable_encoder(result))

    summ = 'Delete API' 
    @app.delete('/delete/{id}', tags=["Stable Version"], summary=summ)
    async def root(request : Request, id : int):
        ''' 
        Delete user. \n
        In prod, dont delete user, just disable from view. We still save user details(or archive).\n
        For the sake of this assignment, `delete` will PERMANENTLY delete user
        '''
        try:
            print(id)
            result = CRUD.delete_user(id)
            
            if not result:
                raise HTTPException(status_code=404, detail=f"ID {id} does not exist!")

        except Exception as e:
            clog('error', str(e))
            raise HTTPException(status_code=404, detail=f"ID {id} does not exist!")

        return JSONResponse(jsonable_encoder(result))

    return app