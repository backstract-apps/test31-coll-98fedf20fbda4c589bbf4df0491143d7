from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - test31-coll-98fedf20fbda4c589bbf4df0491143d7',debug=False,docs_url='/funny-lovelace-883f4b60b30611ef94ff0242ac1a000357/docs',openapi_url='/funny-lovelace-883f4b60b30611ef94ff0242ac1a000357/openapi.json')

app.include_router(router, prefix='/funny-lovelace-883f4b60b30611ef94ff0242ac1a000357/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()