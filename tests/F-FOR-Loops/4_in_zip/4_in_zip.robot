*** Variables ***
@{First Name}    Bruce     Steve     Peter
@{Last Name}     Banner    Rogers    Parker


*** Test Cases ***
Combine Two Loops
    Log To Console    Full Names:
    FOR    ${first}    ${last}    IN ZIP    ${First Name}    ${Last Name}
        Log To Console    \t${first} ${last}  
    END