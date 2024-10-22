#!/usr/bin/env python3
""" Lists schools that have a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ lists schools by topic """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
