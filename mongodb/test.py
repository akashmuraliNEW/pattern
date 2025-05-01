from pymongo import MongoClient

# Connect to your MongoDB (replace with your URI)
client = MongoClient("mongodb+srv://telegram:telegramfiles@cluster0.piabe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Replace with your URI if different

# List all databases
# db_names = client.list_database_names()
# def check_db_stats():
#     for db_name in db_names:
#         db = client[db_name]
#         print(f"\nStats for Database: {db_name}")
        
#         # Get stats for the database
#         db_stats = db.command("dbStats")
#         print(f"Storage Size: {db_stats['storageSize']} bytes")
#         print(f"Data Size: {db_stats['dataSize']} bytes")
#         print(f"Index Size: {db_stats['indexSize']} bytes")
#         print(f"Number of Collections: {db_stats['collections']}")
#         print(f"Number of Documents: {db_stats['objects']}")

#         # Get stats for each collection in the database
#         for collection_name in db.list_collection_names():
#             collection = db[collection_name]
#             collection_stats = collection._command()
#             print(f"\n  Collection: {collection_name}")
#             print(f"    Documents: {collection_stats['count']}")
#             print(f"    Collection Size: {collection_stats['storageSize']} bytes")
#             print(f"    Index Size: {collection_stats['totalIndexSize']} bytes")

# # Run the stats checker
# if __name__ == "__main__":
#     check_db_stats()


old_db = client['telegram']
old_collection = old_db['users']
users = old_collection.find()
# Connect to new MongoDB instance
# new_client = MongoClient("mongodb://new_user:new_password@new_mongo_url:27017/new_db_name")
# new_db = new_client['new_db_name']
# new_collection = new_db['users']  # Replace 'users' with your actual collection name
j=0
for i in users:
    print(i)
    print('''''''''''''''''''''''''''''''''''''''''''''''')
    if j>100:
        break

    j+=1
    