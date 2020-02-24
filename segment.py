import requests, time

endpoint_segments = "/cxs/segments/"


def metadata(segment_id):
    metadata = {
        "id": segment_id,
        "name": "Marketeer",
        "description": "A segment for the Marketeer (test comparisonOperator).",
        "scope": "1599f403-8ec9-421b-9bfe-0c8c3da2e010",
        "tags": [
            "tech",
            "work",
            "manage"
        ],
        "systemTags": [
            "manual"
        ]
    }

    return metadata


def segment(segment_id):
    segment = {
        "condition": {
            "parameterValues": {
                "operator": "and",
                "subConditions": [
                    {
                        "type": "profilePropertyCondition",
                        "parameterValues": {
                            "propertyName": "properties.classification_id",
                            "comparisonOperator": "equals",
                            "propertyValue": "cb0ab66c-6750-1984-b7b5-d278cf60b761"
                        }
                    }
                ]
            },
            "type": "booleanCondition"
        },
        "metadata": metadata(segment_id)
    }

    return segment


def delete_segment(base_url, username, password, segment_id):  # delete segment

    url = base_url + endpoint_segments + segment_id

    time.sleep(0.5)

    return requests.delete(url=url, auth=(username, password))


#################################################################################################

def create_segment_no_propertyValue(base_url, username, password, segment_id, property_name, comparison_operator):
    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": property_name,
            "comparisonOperator": comparison_operator
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    time.sleep(0.5)

    return requests.post(url=base_url + endpoint_segments, auth=(username, password), json=segment_object)


def create_segment_propertyValue(base_url, username, password, segment_id, property_name, comparison_operator, property_value):
    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": property_name,
            "comparisonOperator": comparison_operator,
            "propertyValue": property_value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    time.sleep(0.5)

    return requests.post(url=base_url + endpoint_segments, auth=(username, password), json=segment_object)


def create_segment_propertyValueInteger(base_url, username, password, segment_id, property_name, comparison_operator, property_value):
    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": property_name,
            "comparisonOperator": comparison_operator,
            "propertyValueInteger": property_value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    time.sleep(0.5)

    return requests.post(url=base_url + endpoint_segments, auth=(username, password), json=segment_object)


def create_segment_propertyValueDate(base_url, username, password, segment_id, property_name, comparison_operator, property_value):
    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": property_name,
            "comparisonOperator": comparison_operator,
            "propertyValueDate": property_value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    time.sleep(0.5)

    return requests.post(url=base_url + endpoint_segments, auth=(username, password), json=segment_object)


def create_segment_propertyValueDateExpr(base_url, username, password, segment_id, property_name, comparison_operator, property_value):
    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": property_name,
            "comparisonOperator": comparison_operator,
            "propertyValueDateExpr": property_value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    time.sleep(0.5)

    return requests.post(url=base_url + endpoint_segments, auth=(username, password), json=segment_object)


def create_segment_propertyValues(base_url, username, password, segment_id, property_name, comparison_operator, property_values):
    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": property_name,
            "comparisonOperator": comparison_operator,
            "propertyValues": property_values
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    time.sleep(0.5)

    return requests.post(url=base_url + endpoint_segments, auth=(username, password), json=segment_object)


def create_segment_propertyValuesInteger(base_url, username, password, segment_id, property_name, comparison_operator, property_values):
    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": property_name,
            "comparisonOperator": comparison_operator,
            "propertyValuesInteger": property_values
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    time.sleep(0.5)

    return requests.post(url=base_url + endpoint_segments, auth=(username, password), json=segment_object)


def create_segment_propertyValuesDate(base_url, username, password, segment_id, property_name, comparison_operator, property_values):
    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": property_name,
            "comparisonOperator": comparison_operator,
            "propertyValuesDate": property_values
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    time.sleep(0.5)

    return requests.post(url=base_url + endpoint_segments, auth=(username, password), json=segment_object)


def create_segment_propertyValuesDateExpr(base_url, username, password, segment_id, property_name, comparison_operator, property_values):
    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": property_name,
            "comparisonOperator": comparison_operator,
            "propertyValuesDateExpr": property_values
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    time.sleep(0.5)

    return requests.post(url=base_url + endpoint_segments, auth=(username, password), json=segment_object)


#################################################################################################

def create_segment_number(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.nbOfVisits",
            "comparisonOperator": comparison_operator,
            "propertyValue": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=base_url + endpoint_segments, auth=(username, password), json=segment_object)


def create_segment_between(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.nbOfVisits",
            "comparisonOperator": comparison_operator,
            "propertyValuesInteger": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_exists(base_url, username, password, segment_id, comparison_operator):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.nbOfVisits",
            "comparisonOperator": comparison_operator
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_missing(base_url, username, password, segment_id, comparison_operator):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.nbOfVisits",
            "comparisonOperator": comparison_operator
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_word(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.word",
            "comparisonOperator": comparison_operator,
            "propertyValue": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_in(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.nbOfVisits",
            "comparisonOperator": comparison_operator,
            "propertyValuesInteger": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_not_in(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.nbOfVisits",
            "comparisonOperator": comparison_operator,
            "propertyValuesInteger": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_all(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.listValues",
            "comparisonOperator": comparison_operator,
            "propertyValuesInteger": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_in_contains(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.nbOfVisits",
            "comparisonOperator": comparison_operator,
            "propertyValues": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_has_some_of(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.listValues",
            "comparisonOperator": comparison_operator,
            "propertyValuesInteger": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_has_none_of(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.listValues",
            "comparisonOperator": comparison_operator,
            "propertyValuesInteger": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_is_day(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.word",
            "comparisonOperator": comparison_operator,
            "propertyValue": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)


def create_segment_is_not_day(base_url, username, password, segment_id, comparison_operator, value):  # create a segment with test values

    url = base_url + endpoint_segments

    sub_condition = {
        "type": "profilePropertyCondition",
        "parameterValues": {
            "propertyName": "properties.word",
            "comparisonOperator": comparison_operator,
            "propertyValue": value
        }
    }

    segment_object = segment(segment_id)  # get standard segment

    segment_object['condition']['parameterValues']['subConditions'].append(sub_condition)  # add subcondition to conditions

    return requests.post(url=url, auth=(username, password), json=segment_object)
