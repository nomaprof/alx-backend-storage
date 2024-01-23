#!/usr/bin/env python3
"""
Insert a document in Python into a database in MongoDB
"""


def insert_school(mongo_collection, **kwargs):
    """
     inserts a new document in a
      collection based on kwargs

    :param mongo_collection: school collection
    :param kwargs:
    :return: data inserted
    """
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
