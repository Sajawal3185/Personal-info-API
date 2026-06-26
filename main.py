from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
 return {"Hello": "World"}

@app.get("/about")
def about():
 return {"Name": "Sajawal" , "Age" : 20 , "Location" : "Pakistan"}
    
@app.get("/hobbies")
def hobbies():
 return {"Hobbies": ["Games","Reading","Documentary","Music"]}