#!/usr/bin/env python3
""" function lists Documents  """


def list_all(mongo_collection):
    """ lits docs in collection """

    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
