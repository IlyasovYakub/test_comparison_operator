import requests, time, traceback

from pprint import pprint

from test_comparison_operator.segment import *
from test_comparison_operator.profile import *

base_url = "http://127.0.0.1:8181"
auth_username = "karaf"
auth_password = "karaf"

if __name__ == '__main__':
    try:
        property_number = "number"
        property_word = "word"
        property_date = "date"
        property_date_expr = "date_expr"
        property_list = "list"

        properties_number = "properties." + property_number
        properties_word = "properties." + property_word
        properties_date = "properties." + property_date
        properties_date_expr = "properties." + property_date_expr
        properties_list = "properties." + property_list

        lst_segments = []
        lst_profiles = []

        # create segments #

        segment_name = "test-property_number-equals-string-20"
        pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "equals", "20"))
        lst_segments.append(segment_name)

        segment_name = "test-property_number-equals-integer-20"
        pprint(create_segment_propertyValueInteger(base_url, auth_username, auth_password, segment_name, properties_number, "equals", 20))
        lst_segments.append(segment_name)

        # doesn't work with lists
        # segment_name = "test-property_number-equals-list-integer-40-50-60"
        # pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_number, "equals", [40, 50, 60]))
        # lst_segments.append(segment_name)

        segment_name = "test-property_number-notEquals-string-20"
        pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "notEquals", "20"))
        lst_segments.append(segment_name)

        segment_name = "test-property_number-notEquals-integer-20"
        pprint(create_segment_propertyValueInteger(base_url, auth_username, auth_password, segment_name, properties_number, "notEquals", 20))
        lst_segments.append(segment_name)

        segment_name = "test-property_number-greaterThan-string-20"
        pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "greaterThan", "20"))
        lst_segments.append(segment_name)

        segment_name = "test-property_number-greaterThan-integer-20"
        pprint(create_segment_propertyValueInteger(base_url, auth_username, auth_password, segment_name, properties_number, "greaterThan", 20))
        lst_segments.append(segment_name)

        segment_name = "test-property_number-greaterThanOrEqualTo-string-20"
        pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "greaterThanOrEqualTo", "20"))
        lst_segments.append(segment_name)

        segment_name = "test-property_number-greaterThanOrEqualTo-integer-20"
        pprint(create_segment_propertyValueInteger(base_url, auth_username, auth_password, segment_name, properties_number, "greaterThanOrEqualTo", 20))
        lst_segments.append(segment_name)

        # segment_name = "test-property_number-lessThan-string-20"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "lessThan", "20"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-lessThan-integer-20"
        # pprint(create_segment_propertyValueInteger(base_url, auth_username, auth_password, segment_name, properties_number, "lessThan", 20))
        # lst_segments.append(segment_name)

        # segment_name = "test-property_number-lessThanOrEqualTo-string-20"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "lessThanOrEqualTo", "20"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-lessThanOrEqualTo-integer-20"
        # pprint(create_segment_propertyValueInteger(base_url, auth_username, auth_password, segment_name, properties_number, "lessThanOrEqualTo", 20))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-between-string-10-and-string-30"
        # pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_number, "between", ["10", "30"]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-between-int-10-and-int-30"
        # pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_number, "between", [10, 30]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-exists"
        # pprint(create_segment_no_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "exists"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-missing"
        # pprint(create_segment_no_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "missing"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-contains-string-20"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "contains", "20"))
        # lst_segments.append(segment_name)
        #
        # doesn't work with integers
        # segment_name = "test-property_number-contains-int-20"
        # pprint(create_segment_propertyValueInteger(base_url, auth_username, auth_password, segment_name, properties_number, "contains", 20))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-notContains-string-20"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "notContains", "20"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-startsWith-string-2"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "startsWith", "2"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-endsWith-string-0"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_number, "endsWith", "0"))
        # lst_segments.append(segment_name)
        #
        segment_name = "test-property_number-in-string-list-10-20-30"
        pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_number, "in", ["10", "20", "30"]))
        lst_segments.append(segment_name)

        segment_name = "test-property_number-in-int-list-10-20-30"
        pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_number, "in", [10, 20, 30]))
        lst_segments.append(segment_name)

        segment_name = "test-property_number-notIn-string-list-10-20-30"
        pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_number, "notIn", ["10", "20", "30"]))
        lst_segments.append(segment_name)

        segment_name = "test-property_number-notIn-int-list-10-20-30"
        pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_number, "notIn", [10, 20, 30]))
        lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-hasSomeOf-string-list-40-50-60"
        # pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_number, "hasSomeOf", ["40", "50", "60"]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-hasSomeOf-int-list-40-50-60"
        # pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_number, "hasSomeOf", [40, 50, 60]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-hasNoneOf-string-list-40-50-60"
        # pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_number, "hasNoneOf", ["40", "50", "60"]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_number-hasNoneOf-int-list-40-50-60"
        # pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_number, "hasNoneOf", [40, 50, 60]))
        # lst_segments.append(segment_name)

        ####

        # segment_name = "test-property_word-equals-string-b"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_word, "equals", "b"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_word-equals-integer-20"
        # pprint(create_segment_propertyValueInteger(base_url, auth_username, auth_password, segment_name, properties_word, "equals", 20))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_word-greaterThanOrEqualTo-string-a"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_word, "greaterThanOrEqualTo", "a"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_word-lessThanOrEqualTo-string-c"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_word, "lessThanOrEqualTo", "c"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_word-contains-string-a"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_word, "contains", "a"))
        # lst_segments.append(segment_name)

        ####

        # segment_name = "test-property_date-equals-date-2020-02-20"
        # pprint(create_segment_propertyValueDate(base_url, auth_username, auth_password, segment_name, properties_date, "equals", "2020-02-20"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_date-greaterThanOrEqualTo-date-2020-02-19"
        # pprint(create_segment_propertyValueDate(base_url, auth_username, auth_password, segment_name, properties_date, "greaterThanOrEqualTo", "2020-02-19"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_date-lessThanOrEqualTo-date-2020-02-21"
        # pprint(create_segment_propertyValueDate(base_url, auth_username, auth_password, segment_name, properties_date, "lessThanOrEqualTo", "2020-02-21"))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_date-between-date-2020-02-19-and-date-2020-02-21"
        # pprint(create_segment_propertyValuesDate(base_url, auth_username, auth_password, segment_name, properties_date, "between", ["2020-02-19", "2020-02-21"]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_date-in-date-list-2020-02-19_2020-02-20_2020-02-21"
        # pprint(create_segment_propertyValuesDate(base_url, auth_username, auth_password, segment_name, properties_date, "in", ["2020-02-19", "2020-02-20", "2020-02-21"]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_date-notIn-date-list-2020-02-19_2020-02-20_2020-02-21"
        # pprint(create_segment_propertyValuesDate(base_url, auth_username, auth_password, segment_name, properties_date, "notIn", ["2020-02-19", "2020-02-20", "2020-02-21"]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_date-hasSomeOf-date-list-2020-02-21_2020-02-22_2020-02-23"
        # pprint(create_segment_propertyValuesDate(base_url, auth_username, auth_password, segment_name, properties_date, "hasSomeOf", ["2020-02-21", "2020-02-22", "2020-02-23"]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_date-hasNoneOf-date-list-2020-02-21_2020-02-22_2020-02-23"
        # pprint(create_segment_propertyValuesDate(base_url, auth_username, auth_password, segment_name, properties_date, "hasNoneOf", ["2020-02-21", "2020-02-22", "2020-02-23"]))
        # lst_segments.append(segment_name)
        #
        # does not work with date as date or string
        # segment_name = "test-property_date-contains-string-2020-02-22"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_date, "contains", "2020-02-22"))
        # lst_segments.append(segment_name)

        # segment_name = "test-property_date-contains-string-22"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_date, "contains", "20"))
        # lst_segments.append(segment_name)

        # segment_name = "test-property_date-contains-string-2020-02-22"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_date, "contains", "2020-02-22"))
        # lst_segments.append(segment_name)

        # does not work with dates
        # segment_name = "test-property_date-startsWith-string-2020"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_date, "startsWith", "2020"))
        # lst_segments.append(segment_name)

        # does not work with dates
        # segment_name = "test-property_date-startsWith-string-22"
        # pprint(create_segment_propertyValue(base_url, auth_username, auth_password, segment_name, properties_date, "startsWith", "22"))
        # lst_segments.append(segment_name)

        ####

        # segment_name = "test-property_list-between-string-10-and-string-30"
        # pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_list, "between", ["10", "30"]))
        # lst_segments.append(segment_name)
        #
        segment_name = "test-property_list-between-int-10-and-int-30"
        pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_list, "between", [10, 30]))
        lst_segments.append(segment_name)

        segment_name = "test-property_list-in-string-list-10-20-30"
        pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_list, "in", ["10", "20", "30"]))
        lst_segments.append(segment_name)

        segment_name = "test-property_list-in-int-list-10-20-30"
        pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_list, "in", [10, 20, 30]))
        lst_segments.append(segment_name)

        segment_name = "test-property_list-notIn-string-list-10-20-30"
        pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_list, "notIn", ["10", "20", "30"]))
        lst_segments.append(segment_name)

        segment_name = "test-property_list-notIn-int-list-10-20-30"
        pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_list, "notIn", [10, 20, 30]))
        lst_segments.append(segment_name)
        #
        # segment_name = "test-property_list-hasSomeOf-string-list-40-50-60"
        # pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_list, "hasSomeOf", ["40", "50", "60"]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_list-hasSomeOf-int-list-40-50-60"
        # pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_list, "hasSomeOf", [40, 50, 60]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_list-hasNoneOf-string-list-40-50-60"
        # pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_list, "hasNoneOf", ["40", "50", "60"]))
        # lst_segments.append(segment_name)
        #
        # segment_name = "test-property_list-hasNoneOf-int-list-40-50-60"
        # pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_list, "hasNoneOf", [40, 50, 60]))
        # lst_segments.append(segment_name)

        segment_name = "test-property_list-all-string-list-40-50-60"
        pprint(create_segment_propertyValues(base_url, auth_username, auth_password, segment_name, properties_list, "all", ["40", "50", "60"]))
        lst_segments.append(segment_name)

        segment_name = "test-property_list-all-int-list-40-50-60"
        pprint(create_segment_propertyValuesInteger(base_url, auth_username, auth_password, segment_name, properties_list, "all", [40, 50, 60]))
        lst_segments.append(segment_name)

        # process time #

        time.sleep(3)
        print("successfuly created segments!")
        print("-------------------------------------------------------------------------------------")

        # create profiles #

        response = create_profile(base_url, auth_username, auth_password, "test-01", property_number, "20")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-02", property_number, 20)

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-03", property_number, "19")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-04", property_number, 19)

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-05", property_number, "25")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-06", property_number, 25)

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-07", property_word, "b")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-17", property_word, "a")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-18", property_word, "ab")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-08", property_date, "2020-02-20")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-09", property_date, "2020-02-18")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-10", property_date, "2020-02-22")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-11", property_date, "2020-02-23")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-12", property_date, "2020-02-24")

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-13", property_list, [10, 20, 30, 40])

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-14", property_list, ["10", "20", "30", "40"])

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-15", property_list, [30, 40, 50])

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-21", property_list, ["30", "40", "50"])

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-16", property_list, [40, 50, 60])

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-19", property_list, [15])

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        response = create_profile(base_url, auth_username, auth_password, "test-20", property_list, ["40", "50", "60"])

        lst_profiles.append(response.json())

        print_success_profile(response)
        print("-------------------------------------------------------------------------------------")

        # process time #

        time.sleep(3)

        # clean up #

        for item in lst_segments:
            pprint(delete_segment(base_url, auth_username, auth_password, item))

        print("successfuly deleted test segments")

        # process time #

        time.sleep(3)

        # clean up #

        for item in lst_profiles:
            pprint(delete_profile(base_url, auth_username, auth_password, item['itemId']))

        print("successfuly deleted test profiles")

    except Exception:
        print(traceback.format_exc())

        # clean up #

        for item in lst_segments:
            pprint(delete_segment(base_url, auth_username, auth_password, item))

        print("successfuly deleted test segments")

        # process time #

        time.sleep(3)

        # clean up #

        for item in lst_profiles:
            pprint(delete_profile(base_url, auth_username, auth_password, item['itemId']))

        print("successfuly deleted test profiles")
