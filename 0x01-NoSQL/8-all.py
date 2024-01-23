#!/usr/bin/env python3
"""
List all documents in Python from MongoDB database
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection

    :param mongo_collection: from school collection
    :return: all documents with a match
    """
    return mongo_collection.find()
