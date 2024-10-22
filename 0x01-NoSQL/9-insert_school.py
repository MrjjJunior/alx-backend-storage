#!/usr/bin/env python3
""" Script that insersts in DB """


def insert_school(mongo_collection, **kwargs):
    """ inserts in DB  """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
