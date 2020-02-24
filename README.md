# comparisonOperator

## source
Based on this source:
* https://github.com/apache/unomi/blob/master/plugins/baseplugin/src/main/java/org/apache/unomi/plugins/baseplugin/conditions/PropertyConditionESQueryBuilder.java

* https://github.com/apache/unomi/blob/08e36faa16bddc5a8d0c346b21286bcebe72f60d/plugins/baseplugin/src/main/java/org/apache/unomi/plugins/baseplugin/conditions/PropertyConditionEvaluator.java

## general remark
Most of the times unomi allows you to use comparisonOperators between different types of values, as you will see in the examples further ahead. However, to keep it clear for you the user, please use the same value types; if your profile property is an integer the property value in subCondition should be integer as well.

Also, there are a few comparisonOperators which I couldn't get to work. They will have no explanation and will be skipped.

## overview
* equals
* notEquals
* greaterThan
* greaterThanOrEqualTo
* lessThan
* lessThanOrEqualTo
* between
* exists
* missing
* contains
* notContains
* startsWith
* endsWith
* ~~matchesRegex~~
* in
* notIn
* all
* ~~inContains~~
* hasSomeOf
* hasNoneOf
* ~~isDay~~
* ~~isNotDay~~

## equals
Checks if the profile property value is equal to the value in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "equals",
    "propertyValue": "a"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "equals",
    "propertyValueInteger": 20
}

// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "equals",
    "propertyValueDate": "2020-04-20"
}
```

### Note
This comparisonOperator treats string "20" and integer 20 the same way.
A profile with property value "20" or 20 will be seen as "true" by both subConditions:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "equals",
    "propertyValue": "20"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "equals",
    "propertyValueInteger": 20
}
```

:::warning
This comparisonOperator does not work for values in arrays in subConditions or in profile properties. These subConditions will cause an issue:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "equals",
    "propertyValues": ["20"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "equals",
    "propertyValuesInteger": [20]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "equals",
    "propertyValuesDate": ["2020-04-20"]
}
```
:::


## notEquals
Checks if the profile property value is not equal to the value in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "notEquals",
    "propertyValue": "a"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "notEquals",
    "propertyValueInteger": 20
}

// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "notEquals",
    "propertyValueDate": "2020-04-20"
}
```

### Note
This comparisonOperator treats string "10" and integer 10 the same way.
A profile with property value "10" or 10 will be seen as "true" by both subConditions:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "notEquals",
    "propertyValue": "20"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "notEquals",
    "propertyValueInteger": 20
}
```

:::warning
This comparisonOperator does not work for values in arrays in subConditions or in profile properties. These subConditions will cause an issue:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "notEquals",
    "propertyValues": ["20"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "notEquals",
    "propertyValuesInteger": [20]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "notEquals",
    "propertyValuesDate": ["2020-04-20"]
}
```
:::


## greaterThan
Checks if the profile property value is greater than the value in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "greaterThan",
    "propertyValue": "a"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThan",
    "propertyValueInteger": 20
}

// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "greaterThan",
    "propertyValueDate": "2020-04-20"
}
```

### Note
This comparisonOperator treats string "20" and integer 20 the same way.
A profile with property value "20" or 20 will be seen as "true" by both subConditions:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThan",
    "propertyValue": "10"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThan",
    "propertyValueInteger": 10
}
```

This comparisonOperator treats string "b" as greater than string "a".
A profile with property value "b" will be seen as "true" by this subCondition:
``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "greaterThan",
    "propertyValue": "a"
}
```

This comparisonOperator treats date "2020-04-21" as greater than date "2020-04-20".
A profile with property value "2020-04-21" will be seen as "true" by this subCondition:
``` jsonc
// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "greaterThan",
    "propertyValueDate": "2020-04-20"
}
```

:::warning
This comparisonOperator does not work for values in arrays in subConditions or in profile properties. These subConditions will cause an issue:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThan",
    "propertyValues": ["20"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThan",
    "propertyValuesInteger": [20]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThan",
    "propertyValuesDate": ["2020-04-20"]
}
```
:::


## greaterThanOrEqualTo
Checks if the profile property value is greater than or equal to the value in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "greaterThanOrEqualTo",
    "propertyValue": "a"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThanOrEqualTo",
    "propertyValueInteger": 20
}

// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "greaterThanOrEqualTo",
    "propertyValueDate": "2020-04-20"
}
```

### Note
This comparisonOperator treats string "20" and integer 20 the same way.
A profile with property value "20" or 20 will be seen as "true" by both subConditions:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThanOrEqualTo",
    "propertyValue": "10"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThanOrEqualTo",
    "propertyValueInteger": 10
}
```

This comparisonOperator treats string "b" as greater than or equal to string "a".
A profile with property value "b" will be seen as "true" by this subCondition:
``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "greaterThanOrEqualTo",
    "propertyValue": "a"
}
```

This comparisonOperator treats date "2020-04-21" as greater than or equal to date "2020-04-20".
A profile with property value "2020-04-21" will be seen as "true" by this subCondition:
``` jsonc
// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "greaterThanOrEqualTo",
    "propertyValueDate": "2020-04-20"
}
```

:::warning
This comparisonOperator does not work for values in arrays in subConditions or in profile properties. These subConditions will cause an issue:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThanOrEqualTo",
    "propertyValues": ["20"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThanOrEqualTo",
    "propertyValuesInteger": [20]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "greaterThanOrEqualTo",
    "propertyValuesDate": ["2020-04-20"]
}
```
:::


## lessThan
Checks if the profile property value is less than the value in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "lessThan",
    "propertyValue": "c"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThan",
    "propertyValueInteger": 20
}

// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "lessThan",
    "propertyValueDate": "2020-04-20"
}
```

### Note
This comparisonOperator treats string "10" and integer 10 the same way.
A profile with property value "10" or 10 will be seen as "true" by both subConditions:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThan",
    "propertyValue": "20"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThan",
    "propertyValueInteger": 20
}
```

This comparisonOperator treats string "b" as less than string "c".
A profile with property value "b" will be seen as "true" by this subCondition:
``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "lessThan",
    "propertyValue": "c"
}
```

This comparisonOperator treats date "2020-04-21" as less than date "2020-04-22".
A profile with property value "2020-04-21" will be seen as "true" by this subCondition:
``` jsonc
// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "lessThan",
    "propertyValueDate": "2020-04-22"
}
```

:::warning
This comparisonOperator does not work for values in arrays in subConditions or in profile properties. These subConditions will cause an issue:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThan",
    "propertyValues": ["20"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThan",
    "propertyValuesInteger": [20]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThan",
    "propertyValuesDate": ["2020-04-20"]
}
```
:::


## lessThanOrEqualTo
Checks if the profile property value is less than or equal to the value in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "lessThanOrEqualTo",
    "propertyValue": "c"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThanOrEqualTo",
    "propertyValueInteger": 20
}

// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "lessThanOrEqualTo",
    "propertyValueDate": "2020-04-20"
}
```

### Note
This comparisonOperator treats string "10" and integer 10 the same way.
A profile with property value "10" or 10 will be seen as "true" by both subConditions:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThanOrEqualTo",
    "propertyValue": "20"
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThanOrEqualTo",
    "propertyValueInteger": 20
}
```

This comparisonOperator treats string "b" as less than or equal to string "c".
A profile with property value "b" will be seen as "true" by this subCondition:
``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "lessThanOrEqualTo",
    "propertyValue": "c"
}
```

This comparisonOperator treats date "2020-04-21" as less than or equal to date "2020-04-22".
A profile with property value "2020-04-21" will be seen as "true" by this subCondition:
``` jsonc
// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "lessThanOrEqualTo",
    "propertyValueDate": "2020-04-22"
}
```

:::warning
This comparisonOperator does not work for values in arrays in subConditions or in profile properties. These subConditions will cause an issue:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThanOrEqualTo",
    "propertyValues": ["20"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThanOrEqualTo",
    "propertyValuesInteger": [20]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "lessThanOrEqualTo",
    "propertyValuesDate": ["2020-04-20"]
}
```
:::


## between
Checks if the profile property value is between the values in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "between",
    "propertyValues": ["a", "c"]
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "between",
    "propertyValuesInteger": [10, 30]
}

// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "between",
    "propertyValuesDate": ["2020-04-20", "2020-04-22"]
}
```

### Note
This comparisonOperator does **not** treat string "20" and integer 20 the same way.

A profile with property value "20" will **not be seen as "true" by these subConditions** and a profile with property value 20 will be seen as "true" by both subConditions:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "between",
    "propertyValues": ["10", "30"]
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "between",
    "propertyValuesInteger": [10, 30]
}
```

This comparisonOperator treats string "b" as between string "a" and string "c".
A profile with property value "b" will be seen as "true" by this subCondition:
``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "between",
    "propertyValues": ["a", "c"]
}
```

A subCondition treats date "2020-04-21" as between date "2020-04-20" and date "2020-04-22".
A profile with property value "2020-04-21" will be seen as "true" by this subCondition:
``` jsonc
// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "between",
    "propertyValuesDate": ["2020-04-20", "2020-04-22"]
}
```

:::warning
This comparisonOperator does not work for values in arrays in profile properties.
:::


## exists
Checks if the profile property exists.

``` jsonc
// property value
{
    "propertyName": "properties.word",
    "comparisonOperator": "exists"
}
```


## missing
Checks if the profile property is missing.

``` jsonc
// property value
{
    "propertyName": "properties.word",
    "comparisonOperator": "missing"
}
```


## contains
Checks if the profile property value contains the value in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "contains",
    "propertyValue": "a"
}
```

### Note
This comparisonOperator treats string "1020" and integer 1020 the same way.
A profile with property value "1020" or 1020 will be seen as "true" by this subCondition:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "contains",
    "propertyValue": "20"
}
```

This comparisonOperator treats string "ab" as containing string "a".
A profile with property value "ab" will be seen as "true" by this subCondition:
``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "contains",
    "propertyValue": "a"
}
```

:::warning
This comparisonOperator does not work for integer values in subConditions.
:::

:::warning
This comparisonOperator does not work for date values in subConditions or in profile properties.
:::

:::warning
This comparisonOperator does not work for values in arrays in subConditions or in profile properties. These subConditions will cause an issue:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "contains",
    "propertyValues": ["20"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "contains",
    "propertyValuesInteger": [20]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "contains",
    "propertyValuesDate": ["2020-04-20"]
}
```
:::


## notContains
Checks if the profile property value does not contain the value in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "notContains",
    "propertyValue": "a"
}
```

### Note
This comparisonOperator treats string "1020" and integer 1020 the same way.
A profile with property value "1020" or 1020 will be seen as "true" by this subCondition:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "notContains",
    "propertyValue": "30"
}
```

This comparisonOperator treats string "ab" as not containing string "c".
A profile with property value "ab" will be seen as "true" by this subCondition:
``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "notContains",
    "propertyValue": "c"
}
```

:::warning
This comparisonOperator does not work for integer values in subConditions.
:::

:::warning
This comparisonOperator does not work for date values in subConditions or in profile properties.
:::

:::warning
This comparisonOperator does not work for values in arrays in subConditions or in profile properties. These subConditions will cause an issue:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "notContains",
    "propertyValues": ["20"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "notContains",
    "propertyValuesInteger": [20]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "notContains",
    "propertyValuesDate": ["2020-04-20"]
}
```
:::


## startsWith
Checks if the profile property value starts with the value in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "startsWith",
    "propertyValue": "a"
}
```

### Note
This comparisonOperator treats string "20" and integer 20 the same way.
A profile with property value "20" or 20 will be seen as "true" by this subCondition:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "startsWith",
    "propertyValue": "2"
}
```

:::warning
This comparisonOperator does not work for integer values in subConditions.
:::

:::warning
This comparisonOperator does not work for date values in subConditions or in profile properties.
:::

:::warning
This comparisonOperator does not work for values in arrays in subConditions or in profile properties. These subConditions will cause an issue:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "startsWith",
    "propertyValues": ["20"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "startsWith",
    "propertyValuesInteger": [20]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "startsWith",
    "propertyValuesDate": ["2020-04-20"]
}
```
:::


## endsWith
Checks if the profile property value ends with the value in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "endsWith",
    "propertyValue": "a"
}
```

### Note
This comparisonOperator treats string "20" and integer 20 the same way.
A profile with property value "20" or 20 will be seen as "true" by this subCondition:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "endsWith",
    "propertyValue": "0"
}
```

:::warning
This comparisonOperator does not work for integer values in subConditions.
:::

:::warning
This comparisonOperator does not work for date values in subConditions or in profile properties.
:::

:::warning
This comparisonOperator does not work for values in arrays in subConditions or in profile properties. These subConditions will cause an issue:
``` jsonc
// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "endsWith",
    "propertyValues": ["20"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "endsWith",
    "propertyValuesInteger": [20]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "endsWith",
    "propertyValuesDate": ["2020-04-20"]
}
```
:::


## matchesRegex
Cannot get this to work.

## in
Checks if the profile property value is in the values in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "in",
    "propertyValues": ["a", "b", "c"]
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "in",
    "propertyValuesInteger": [10, 20, 30]
}

// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "in",
    "propertyValuesDate": ["2020-04-20", "2020-04-21", "2020-04-22"]
}
```

### Note
This comparisonOperator does not treat string "20" and integer 20 the same way.

A profile with property value "20" will be seen as "true" by this subCondition:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "in",
    "propertyValues": ["10", "20", "30"]
}
```

A profile with property value 20 will be seen as "true" by this subCondition:
``` jsonc
// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "in",
    "propertyValuesInteger": [10, 20, 30]
}
```

**This comparisonOperator works for arrays in subconditions, but only if all values are of the same type!**

A profile with property value ["10", "40", "50"] will be seen as "true" by this subCondition:
``` jsonc
// property value is a list of strings
{
    "propertyName": "properties.number",
    "comparisonOperator": "in",
    "propertyValues": ["10", "20", "30"]
}
```

A profile with property value [10, 40, 50] will be seen as "true" by this subCondition:
``` jsonc
// property value is a list of integers
{
    "propertyName": "properties.number",
    "comparisonOperator": "in",
    "propertyValuesInteger": [10, 20, 30]
}
```

## notIn
Checks if the profile property value is not in the values in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "notIn",
    "propertyValues": ["a", "b", "c"]
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "notIn",
    "propertyValuesInteger": [10, 20, 30]
}

// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "notIn",
    "propertyValuesDate": ["2020-04-20", "2020-04-21", "2020-04-22"]
}
```

### Note
This comparisonOperator treats string "40" and integer 40 the same way in the following situation.

A profile with property value "40" or 40 will be seen as "true" by both subConditions:
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "notIn",
    "propertyValues": ["10", "20", "30"]
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "notIn",
    "propertyValuesInteger": [10, 20, 30]
}
```

**However**, in the following situation the comparisonOperator will not treat the values the same way!

A profile with property value "20" will **only** be seen as "true" by this subConditions (and not the one below):
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "notIn",
    "propertyValuesInteger": [10, 20, 30]
}
```

A profile with property value 20 will **only** be seen as "true" by this subConditions (and not the one above):
``` jsonc
// property value is a string
{
    "propertyName": "properties.number",
    "comparisonOperator": "notIn",
    "propertyValues": ["10", "20", "30"]
}
```

**This comparisonOperator works with lists!**

A profile with property value ["10", "40", "50"] will be seen as "true" by both subConditions, with the second being a special case as described in the example above:
``` jsonc
// property value is list of strings
{
    "propertyName": "properties.number",
    "comparisonOperator": "notIn",
    "propertyValues": ["20", "30", "60"]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "notIn",
    "propertyValuesInteger": [10, 30, 60]
}
```

A profile with property value [10, 40, 50] will be seen as "true" by this subCondition, with the second being a special case as described in the example above:
``` jsonc
// property value is list of integers
{
    "propertyName": "properties.number",
    "comparisonOperator": "notIn",
    "propertyValuesInteger": [20, 30, 60]
}

// property value
{
    "propertyName": "properties.number",
    "comparisonOperator": "notIn",
    "propertyValuesInteger": ["10", "30", "60"]
}
```

## all
Checks if the profile property value has all the values (in the same type) in the subCondition.

``` jsonc
// property value is a string
{
    "propertyName": "properties.word",
    "comparisonOperator": "all",
    "propertyValues": ["a", "b", "c"]
}

// property value is an integer
{
    "propertyName": "properties.number",
    "comparisonOperator": "all",
    "propertyValuesInteger": [10, 20, 30]
}

// property value is a date (yyyy-mm-dd)
{
    "propertyName": "properties.date",
    "comparisonOperator": "all",
    "propertyValuesDate": ["2020-04-20", "2020-04-21", "2020-04-22"]
}
```

## inContains
Cannot get this to work.

## hasSomeOf
Does the same as comparisonOperator "in".

## hasNoneOf
Does the same as comparisonOperator "notIn".

## isDay
Cannot get this to work.

## isNotDay
Cannot get this to work.
