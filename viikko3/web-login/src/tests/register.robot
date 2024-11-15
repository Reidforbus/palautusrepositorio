*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password    kalle123
    Set Password Confirmation    kalle123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Password
    Set Username  ka
    Set Password    kalle123
    Set Password Confirmation    kalle123
    Submit Credentials
    Page Should Contain  Username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password    kalle12
    Set Password Confirmation    kalle12
    Submit Credentials
    Page Should Contain    Password has to be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password    kallekoo
    Set Password Confirmation    kallekoo
    Submit Credentials
    Page Should Contain    Password has to contain at least one non alphabet character

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password    kalle123
    Set Password Confirmation    kalle124
    Submit Credentials
    Page Should Contain    Password and password confirmation must match

Register With Valid Username That Is Already In Use
    Set Username  kalle
    Set Password    kalle123
    Set Password Confirmation    kalle123
    Submit Credentials
    Go To Register Page
    Set Username    kalle
    Set Password    kalle234
    Set Password Confirmation    kalle234
    Submit Credentials
    Page Should Contain    User with username kalle already exists

Login After Succesful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation    kalle123
    Submit Credentials
    Click Link    Continue to main page
    Click Button    Logout
    Set Username    kalle
    Set Password    kalle123
    Click Button    Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  kalle
    Set Password    kalle123
    Set Password Confirmation    kalle124
    Submit Credentials
    Page Should Contain    Password and password confirmation must match
    Go To Login Page
    Set Username    kalle
    Set Password    kalle123
    Click Button    Login
    Page Should Contain    Invalid username or password

*** Keywords ***

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password    password_confirmation    ${password_confirmation}

Submit Credentials
    Click Button  Register
