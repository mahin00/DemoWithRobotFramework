*** Settings ***
Suite Setup       Wait Until Keyword Succeeds    ${RETRY_INT_LOGIN}    ${SHORT_DELAY}    Open Application
Suite Teardown    Close Application
Force Tags        Login
Resource          ../../keywords.robot

*** Variables ***
${invalid_login_msg}    Incorrect username or password.

*** Test Cases ***
TC05_HOME_Check_Login_Page_Opens_and_Contains_Greetings_Message
    [Documentation]    Users are directed to login page and login page contains version number
    Set Selenium Speed    0.5 seconds
    Login Page Should Be Open
    Wait Until Page Contains Element    //h3[contains(text(),'Welcome to Daraz! Please login.')]

TC06_HOME_Invalid_Login
    [Documentation]    This is an Invalid Login scenario
    [Tags]    InvalidLogin
    Set Selenium Speed    0.2 seconds
    Input Email    ${USEREMAIL}
    Input Password    ${Invalid_Password}
    Continue
    Verify Invalid Login Message    ${invalid_login_msg}

TC_07_HOME_Log Out And Log In Again
    [Documentation]    This is a logout and login scenario
    [Tags]    Logout    ValidLogin
    Set Selenium Speed    0.2 seconds
    Go To Login Page
    Input Email    ${USEREMAIL}
    Input Password    ${PASSWORD}
    Continue
    Welcome Page Should Be Open
    Log Out
    Go To Login Page
    Input Email    ${USEREMAIL}
    Input Password    ${PASSWORD}
    Continue
    Welcome Page Should Be Open
    [Teardown]    Go To Home Page


