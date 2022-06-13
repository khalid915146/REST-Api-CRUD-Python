from fastapi import APIRouter
from models.model import Address 
from config.connection import conn
from schemas.schema import addressEntity, addressesEntity
from bson import ObjectId
AddressBook = APIRouter() 


#get
@AddressBook.get('/')
async def find_all_addresses():
    print(conn.local.address.find())
    print (addressesEntity(conn.local.address.find()))
    return addressesEntity(conn.local.address.find())


#findbyid
@AddressBook.get('/{id}')
async def find_one_address(id):
    return addressEntity(conn.local.address.find_one({"_id":ObjectId(id)}))


#post
@AddressBook.post('/')
async def create_address(address: Address):
    conn.local.address.insert_one(dict(address))
    return addressesEntity(conn.local.address.find())


#update
@AddressBook.put('/{id}')
async def update_address(id,address: Address):
    conn.local.address.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(address)
    })
    return addressEntity(conn.local.address.find_one({"_id":ObjectId(id)}))


#delete
@AddressBook.delete('/{id}')
async def delete_address(id,address: Address):
    return addressEntity(conn.local.address.find_one_and_delete({"_id":ObjectId(id)}))