#!/usr/bin/env python3
"""
List all students in a MongoDB database by their average score
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    :param mongo_collection:
    :return: ordered list of students
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
