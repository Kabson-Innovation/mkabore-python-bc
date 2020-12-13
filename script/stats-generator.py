#!/usr/bin/env python3
"""
Service to generate stats of persons
"""

import requests
import pickle
import statistics
from mkabore.person import Person

REQ_URL = "https://pipl.ir/v1/getPerson"
TOTAL_COUNT = 10
person_data = []


def script_runner():
    for person in pickled_items('persons_data.pkl'):
        person_data.append(person)
    if len(person_data) == 0:
        with open('persons_data.pkl', 'wb') as output:
            for i in range(TOTAL_COUNT):
                result = requests.get(REQ_URL)
                data = result.json()
                a_person = Person(data)
                print(a_person.education)
                pickle.dump(a_person, output, pickle.HIGHEST_PROTOCOL)
                person_data.append(a_person)

    find_youngest_oldest()


def pickled_items(filename):
    """ Unpickle a file of pickled data. """
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break

def find_youngest_oldest():
    age_list = []
    for person in person_data:
        age = person.personal['age']
        print(age)
        age_list.append(age)
    age_list = sorted(age_list)
    average = statistics.mean(age_list)
    print("Average Age :", average)
    print(age_list)
    youngest = age_list[:5]
    oldest = age_list[-5:]
    for person in person_data:
        age = person.personal['age']
        if age in youngest:
            print("youngest ", person.personal['last_name'])
        elif age in oldest:
            print('oldest ', person.personal['last_name'])


if __name__ == '__main__':
    script_runner()