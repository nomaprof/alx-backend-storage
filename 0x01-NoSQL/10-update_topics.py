#!/usr/bin/env python3
"""
Change school topics for a collection in MongoDB
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school
     document based on the name

    :param mongo_collection: mongo-collection
    :param name: topics
    :param topics: as decided by user
    :return: updated database
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
