#!/usr/bin/env python3
""" Script that update db"""


def update_topics(mongo_collection, name, topics):
    """ Updates the databse """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
