#!/usr/bin/env python3

class Person:
    approved_jobs = [
        "Teacher",
        "Engineer",
        "Doctor",
        "Artist",
        "Writer",
        "Chef",
        "Athlete",
        "Lawyer",
        "Designer",
        "Scientist",
        "Entrepreneur",
        "Musician",
    ]

    def __init__(self, name, job=None):
        self._name = None
        self._job = None
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 0 < len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value is None or value in self.approved_jobs:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")
