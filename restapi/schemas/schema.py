def addressEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "HouseNumber":item["HouseNumber"],
        "Locality":item["Locality"],
        "AreaCode":item["AreaCode"],
        "CityName":item["CityName"],
        "State":item["State"],
        "Country":item["Country"],
        "ContactNumber":item["ContactNumber"]
    }

def addressesEntity(entity) -> list:
    return [addressEntity(item) for item in entity]