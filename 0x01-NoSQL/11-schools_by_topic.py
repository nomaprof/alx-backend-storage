#!/usr/bin/env python3
"""
Where can I learn Python? find the schools from a MongoDB database
"""


def schools_by_topic(mongo_collection, topic):
    """
     returns the list of school having a specific topic

    :param mongo_collection: Schools_by_topic
    :param topic: topic selected
    :return: the available schools
    """
    return mongo_collection.find({"topics": topic})
