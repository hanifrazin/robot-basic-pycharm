*** Settings ***
Resource    keyword.resource
Resource    variables.resource
Library     PythonVariables.py


*** Test Cases ***
Test Case 1
    Say Hello World

Test Case 2
    Call A Library Keyword

Test Case 3
    FOR    ${key}    ${value}    IN    &{python_dict}
        Log   \nkey: ${key}
        Log    value: ${value}          
    END