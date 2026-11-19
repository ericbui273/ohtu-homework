*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  eric
    Set Password  eric1234
    Set Password Confirmation  eric1234
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  eb
    Set Password  eric1234
    Set Password Confirmation  eric1234
    Click  button >> text=Register
    Register Should Fail With Message  Username must have at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  eric
    Set Password  eric123
    Set Password Confirmation  eric123
    Click  button >> text=Register
    Register Should Fail With Message  Password must have at least 8 characters

Register With Username That Is Already In Use
    Create User  eric  eric1234
    Set Username  eric
    Set Password  12345678
    Set Password Confirmation  12345678
    Click  button >> text=Register
    Register Should Fail With Message  User with username eric already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Fill Secret  id=password_confirmation  $password_confirmation

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page