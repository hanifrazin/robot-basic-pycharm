*** Settings ***
Library    Collections


*** Variables ***
&{SPIDERMAN}    login=spider      password=123spiderman321   name=Peter Parker    right=user     active=${True}
&{IRONMAN}      login=ironman    # the three dots (...) are line continuations...
...             password=1234567890  # looks sometimes better ;)
...             name=Tony Stark
...             right=admin
...             active=${False}


*** Test Cases ***
Test that accesses Dictionaries using Log To Console
    Log To Console    \nLogs Spiderman
    Log To Console    ${SPIDERMAN}
    Log To Console    Login: ${SPIDERMAN}[login]
    Log To Console    Name: ${SPIDERMAN}[name]
    Log To Console    Right: ${SPIDERMAN.right}
    ${var}=    Set Variable    active
    Log To Console    Active: ${SPIDERMAN}[${var}]  # you may use variable content as keys as well.

Test that accesses Dictionaries using Log
    Log    \nLogs Spiderman
    Log    ${SPIDERMAN}
    Log    Login: ${SPIDERMAN}[login]
    Log    Name: ${SPIDERMAN}[name]
    Log    Right: ${SPIDERMAN.right}
    ${var}=    Set Variable    active
    Log    Active: ${SPIDERMAN}[${var}]  # you may use variable content as keys as well.

Test with Dictionaries as Arguments
    Log A Person    ${SPIDERMAN}
    Log A Person    ${IRONMAN}

Test with Dictionaries as Arguments using Log
    Log Person    ${SPIDERMAN}
    Log Person    ${IRONMAN}

Dictionaries for named arguments
    Log To Console    \n Multiple arguments
    Log Dictionary    Bruce Banner    hulk                # positional arguments
    ...                     HULK...SMASH!!!    user    ${True}
    Log Dictionary    password=123456    active=${True}   # vs named arguments
    ...                     login=ant    name=Scott Lang
    ...                     right=guest
    Log Dictionary    &{IRONMAN}                          # vs unpacked dictionary as multiple named args

Test with FOR loops and Dictionaries
    Log To Console    \n---- Logs the keys: ----
    FOR    ${key}    IN    @{IRONMAN}    # unpacked as list (of keys)
        Log To Console    key: ${key}
        Log To Console    dict[key]: ${IRONMAN}[${key}]
    END
    Log To Console     ---- Logs Keys & Values ----
    FOR    ${key}    ${value}    IN    &{SPIDERMAN}
        Log To Console    ${key} : ${value}
    END

*** Keywords ***
Log A Person
    [Arguments]    ${person}
    Log To Console    \n The User "${person.login}" belongs to ${person.name} and the password is "${person.password}"

Log Dictionary
    [Arguments]    ${name}    ${login}    ${password}    ${right}    ${active}
    Log To Console    ${name} | ${login} | ${password} | ${right} | ${active}
    Log    ${name} | ${login} | ${password} | ${right} | ${active}
Log Person
    [Arguments]    ${person}
    Log    \n The User "${person.login}" belongs to ${person.name} and the password is "${person.password}"