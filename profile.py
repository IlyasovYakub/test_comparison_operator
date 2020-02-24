import requests, time

from pprint import pprint

endpoint_profiles = "/cxs/profiles/"


def delete_profile(base_url, username, password, profile_id):  # delete segment

    url = base_url + endpoint_profiles + profile_id

    return requests.delete(url=url, auth=(username, password))


def profile(item_id):
    profile = {
        "itemId": item_id,
        "itemType": "profile",
        "version": None,
        "properties": {
            "classification_id": "cb0ab66c-6750-1984-b7b5-d278cf60b761"
        },
        "systemProperties": {},
        "segments": [],
        "scores": {},
        "mergedWith": None,
        "consents": {}
    }

    return profile


###########################################################################################

def create_profile(base_url, username, password, item_id, property_name, property_value):  # create profile with given values
    url = base_url + endpoint_profiles

    profile_object = profile(item_id)  # get standard profile

    profile_object['properties'][property_name] = property_value  # add property

    return requests.post(url=url, auth=(username, password), json=profile_object)


###########################################################################################


def create_profile_number(base_url, username, password, item_id, nb_of_visits):  # create a profile with test values

    url = base_url + endpoint_profiles

    profile_object = profile(item_id)  # get standard profile

    profile_object['properties']["nbOfVisits"] = nb_of_visits  # add property

    return requests.post(url=url, auth=(username, password), json=profile_object)


def create_profile_word(base_url, username, password, item_id, word):  # create a profile with test values

    url = base_url + endpoint_profiles

    profile_object = profile(item_id)  # get standard profile

    profile_object['properties']["word"] = word  # add property

    return requests.post(url=url, auth=(username, password), json=profile_object)


def create_profile_list(base_url, username, password, item_id, list_values):  # create a profile with test values

    url = base_url + endpoint_profiles

    profile_object = profile(item_id)  # get standard profile

    profile_object['properties']["listValues"] = list_values  # add property

    return requests.post(url=url, auth=(username, password), json=profile_object)


def print_success_profile(response):
    print("successfuly created profile!")
    pprint(response.json())
    time.sleep(0.25)
