from fastapi import FastAPI
from routes.routes import AddressBook
app=FastAPI()

app.include_router(AddressBook)