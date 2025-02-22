*** Settings ***
Library    Collections


*** Variables ***
@{LETTERS}    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
@{POKEMON}    Pikachu    Eevee    Charizard    Bulbasaur    Squirtle    Jigglypuff    Snorlax    Butterfree


*** Test Cases ***
List Variables unpacked
    Log To Console    Lists the Alphabeth
    Log Many    @{LETTERS}    # unpacks the list and hands over 26 arguments
    Log Many    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z  # same result as before
    Log    ${LETTERS}    # a single variable as argument
    Log    @{LETTERS}    # This fails because LOG has only 6 possible arguments (message, level, html, console, repr, formatter)
#    Log    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z

List Variables unpacked modify by me
    Log Many    @{POKEMON}
    Log Many    ${POKEMON}
    Log    ${POKEMON}
    Log    @{POKEMON}

Test with Keywords and a list
    Print All Entries Of A List To Console    ${LETTERS}         # a single scalar value
    Print All Entries Of A List To Console    ${POKEMON}
    Print All Entries Of A List To Console    @{POKEMON}         # akan menjadi error karena argumen dalam bentuk scalar

Test with a Keyword that accepts multiple arguments
    Print All Arguments To Console    @{LETTERS}    # unpacke to 26 values
    Print All Arguments To Console    arg1    arg2    arg3    arg4
    Print All Arguments To Console    ${LETTERS}    # just one value...
    Print All Arguments To Console    @{POKEMON}    # value akan di loop menjadi baris baru
    Print All Arguments To Console    ${POKEMON}    # value akan ditampilkan dalam bentuk list ['a','b','dst'] dan tidak ada baris baru

Test with some Collections keywords using scalar
    ${list}=    Create List    1    2    3
    Append To List    ${list}    4    5    6
    ${list2}=    Create List    7    8    9
    ${new_list}=    Combine Lists    ${list}    ${list2}
    Reverse List    ${new_list}
    Log Many   ${new_list}

Test with some Collection keywords using list
    ${list3}=    Create List    Squirtle    Bulbasaur    Charmender
    Append To List    ${list3}    Torchick    Totodile    Cyndaquil
    ${list4}=    Create List    Pokabu    Blacky    Vaporeon
    ${new_list2}=    Combine Lists    ${list3}    ${list4}
    Log Many    ${new_list2}[::-1]     # cara reverse


Test to access list entries
    Log To Console    index 18 & 6 => ${LETTERS}[18] ${LETTERS}[6]
    Log To Console    index 5 to 10 => ${LETTERS}[5:10]   # is a list again
    Log To Console    index start to 5 => ${LETTERS}[:5]   # same as [0:5]
    Log To Console    index 20 to end => ${LETTERS}[20:]
    Log To Console    Last 5 to end => ${LETTERS}[-5:]


*** Keywords ***
Print All Entries Of A List To Console
    [Arguments]    ${list}    # list as a single scalar variable
    FOR    ${element}    IN    @{list}    # unpacked here. see FOR LOOP example
        Log To Console    ${element}
    END

Print All Arguments To Console
    [Arguments]    @{all_args}
    FOR    ${arg}    IN    @{all_args}    # unpacked here. see FOR LOOP example
        Log To Console    ${arg}
    END
