*** Settings ***
Library    ../../venv/lib/python3.12/site-packages/robot/libraries/DateTime.py


*** Test Cases ***
Simple IF
    ${random_number}    Evaluate    random.randint(0,10)
    IF    ${random_number} % 2
        Log    ${random_number} % 2
        Console    ${random_number} is odd!
    END

IF Expression
    FOR    ${i}    IN RANGE    10
        IF    ${i} <= 3
            Console Log    ${i} <= 3
            Console    Low ${i} 
        ELSE IF    ${i} > 3 and ${i} < 7
            Console Log    ${i} > 3 and ${i} < 7
            Console    Medium ${i}
        ELSE
            Console    High ${i}
        END
        
    END

*** Keywords ***
Console
    [Arguments]        ${output}
    Log To Console     ${output}

Console Log
    [Arguments]        ${hasil}
    Log                ${hasil}    
    ${result}=          Evaluate    ${hasil}
    
