
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 4

        # example list of members
        self._members = [
            {
            "id": 1,
            "first_name": "John",
            "last_name": "Jackson",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
        {   
            "id": 2,
            "first_name": "Jane",
            "last_name": "Jackson",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id": 3,
            "first_name": "Jimmy",
            "last_name": "Jackson",
            "age": 5,
            "lucky_numbers": [1]
        }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        id = self._next_id
        self._next_id += 1
        return id

    def add_member(self, member):
        # fill this method and update the return
        new_member = {
            **member,
            "id": self._generateId(),
            "last_name": self.last_name
        }
        self._members.append(new_member)
        return new_member

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return member
        return None

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members