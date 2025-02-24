*** Variables ***
@{mammals}    cat    dog        cow
@{birds}    eagle   falcon     ladybird

${user1}    peter
${user2}    bruce
${user3}    tony


*** Test Cases ***
Loop over list
    Log To Console    Four mamals:
    FOR    ${var}    IN    @{mammals}
        Log To Console    \t${var}
    END

Loop over two lists after each other
    Log To Console    Four mamals & four birds:
    FOR    ${var}    IN    @{mammals}    @{birds}
        Log To Console    \t${var}
    END

Loop over multiple values
    Log To Console    Four users:
    FOR    ${var}    IN   ${user1}    ${user2}    ${user3}
        Log To Console    \t${var}
    END