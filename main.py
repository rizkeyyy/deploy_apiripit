# import library
from fastapi import FastAPI, HTTPException, Header
import pandas as pd

# create object/instance
app = FastAPI()

# create api key
API_Key = "DarthWijay"

# @app.get("/protected")
# def protect(api_key: str = Header(None)):

#   if api_key is None or api_key != API_Key:
#         raise HTTPException(status_code=401, detail="ANTUM TEH SAHA")

# create endpoint
@app.get("/") # gaboleh make spasi ato jeda 1 baris sama bawahnya dari yg @app sama yg def
def home():
    return{"message": "jiah dia lagi balik kesini"}

# create endpoint data
@app.get("/produk")
def produk():
    # read data from file csv
    df = pd.read_csv("data.csv")
    # mengembalikan data dalam bentuk dataframe
    # merubah dataframenya yg dari berantakan dengan orient="records" untuk setiap baris
    return df.to_dict(orient="records")

# create endpoint data with number of parameter id
@app.get("/produk/{number_id}")
def read_items(number_id: int):
    # read data from file csv
    df = pd.read_csv("data.csv")

    # filter data by id
    filtered_data = df[df["id"] == number_id]

    # kalo misalnya ngga ada datanya
    if len(filtered_data) == 0:
        raise HTTPException(status_code=404, detail="ngga ada dimarih bang barangnya, ke toko belah coba dah")

    # convert 
    return filtered_data.to_dict(orient="records")

# create endpoint update file csv data
@app.put("/items/{number_id}")
def update_items(number_id: int, nama_barang: str, harga: float):
    # read data from csv
    df = pd.read_csv("data.csv")
    # create df for updating data
    updated_df = pd.DataFrame([{
        "id":number_id,
        "nama_barang":nama_barang,
        "harga":harga
    }])

    # merge dataframe dari yg lama gabungin sama yg udh diapdet
    df = pd.concat([df, updated_df], ignore_index=True)

    # nyimpen df baru ke csv
    df.to_csv("data.csv", index=False)

    # mengembalikan dengan pesan apabila berhasil
    return {"message": f"item yg antum tambahin {nama_barang} udh di masukkin nih. aman bang"}

# @app.get("/darkness")
# def read_darkness(api_key: str = Header(None)):

#     # read data from file csv
#     darkness_df= pd.read_csv("darkness_data.csv")
#     # check if api key is valid 
#     if api_key != API_Key or api_key == None:
#         # kalo misalnya ngga valid bakalan keluar "raise"
#         raise HTTPException (status_code=401, detail="ANTUM TEH SAHA ?!")
#     return darkness_df.to_dict(orient="records")
#     #return{"message": "welcome to the darkness"}

@app.get("/secret")
def read_darkness(api_key: str = Header(None)):

    # read data from file csv
    df= pd.read_csv("data.csv")
    # check if api key is valid 
    if api_key != API_Key or api_key == None:
        # kalo misalnya ngga valid bakalan keluar "raise"
        raise HTTPException (status_code=401, detail="ANTUM TEH SAHA ?!")
    return df.to_dict(orient="records")
    #return{"message": "welcome to the darkness"}