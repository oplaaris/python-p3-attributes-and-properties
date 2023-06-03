#!/usr/bin/env python3
class Dog:
    approved_breeds = [
        "Labrador Retriever",
        "German Shepherd",
        "Golden Retriever",
        "Bulldog",
        "Beagle",
        "Poodle",
        "Rottweiler",
        "Yorkshire Terrier",
        "Boxer",
        "Dachshund",
        "Siberian Husky",
        "Great Dane",
    ]

    def __init__(self, name, breed="Mutt"):
        self._name = None
        self._breed = None
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")
