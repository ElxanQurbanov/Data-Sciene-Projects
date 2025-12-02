from fastapi import FastAPI, HTTPException
from models import User
from User_DB import users

app = FastAPI()

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to User API"}

# Get all users
@app.get("/users")
def get_users():
    return users

# Get single user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Add new user
@app.post("/users")
def add_user(user: User):
    # Check duplicate ID
    for u in users:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User ID already exists")
    users.append(user)
    return {"message": "User added successfully"}
