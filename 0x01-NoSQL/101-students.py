#!/usr/bin/env python3
""" script return stundent average scores """


def top_students(mongo_collection):
    """ Returns all students soreted by their average score """
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ])
