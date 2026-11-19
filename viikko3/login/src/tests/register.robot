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

Register With Password Containing Letters And Numbers
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Letters And Special Character
    Set Username  kalle
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Password Consisting Of Lowercase Letters
    Set Username  kalle
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one number or special character

Register With Password Consisting Of Mixed-Case Letters
    Set Username  kalle
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one number or special character

Register With Unmatched Password Confirmation
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle4321
    Click  button >> text=Register
    Register Should Fail With Message  Passwords do not match

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