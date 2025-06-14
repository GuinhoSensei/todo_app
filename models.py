from bson import ObjectId
from db_config import db

users_collection = db["users"]
tasks_collection = db["tasks"]

# User operations
def create_user(username, email):
    result = users_collection.insert_one({
        "username": username,
        "email": email
    })
    return result.inserted_id

def get_user_by_username(username):
    return users_collection.find_one({"username": username})

# Task operations
def create_task(user_id, title, due_date):
    return tasks_collection.insert_one({
        "title": title,
        "due_date": due_date,
        "user_id": ObjectId(user_id)
    }).inserted_id

def get_tasks_for_user(user_id):
    return list(tasks_collection.find({"user_id": ObjectId(user_id)}))

def update_task(task_id, new_title):
    return tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"title": new_title}}
    )

def delete_task(task_id):
    return tasks_collection.delete_one({"_id": ObjectId(task_id)})
