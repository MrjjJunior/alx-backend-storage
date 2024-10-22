#!/usr/bin/env python3
""" Script provides Nginx stats """
from pymongo import MongoClient


def log_stats():
    """ Provides stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    log_count = nginx_collection.count_documents({})
    print(f"{log_count} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({"methods": method})
        print(f"\tmethod {method}: {method_count}")

    methods = {"method": "GET", "path": "/status"}
    status_count = nginx_collection.count_documents(methods)
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats()
