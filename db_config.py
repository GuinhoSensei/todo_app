from pymongo import MongoClient

# Your MongoDB Atlas URI
MONGO_URI = "mongodb+srv://patobranco:patobranco@cluster0.oswnu7j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create the client and connect
client = MongoClient(MONGO_URI)

# Access the database
db = client["todo_database"]
