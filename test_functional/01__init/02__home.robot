*** Settings ***
Suite Setup       Wait Until Keyword Succeeds    ${RETRY_INT_LOGIN}    ${SHORT_DELAY}    Open Application
Suite Teardown    Close Application
Force Tags        Search
Resource          ../../keywords.robot

*** Test Cases ***
TC08_HOME_options_Functionality_Checking
    [Documentation]    Click options on home page
    ...    Expected outcome: Menu options working properly
    Login    ${USEREMAIL}      ${PASSWORD}
    Click daraz Logo
    Scroll Bottom of the Page
    Go To About Us Page
    Click daraz Logo
    Go to Career Page
    Go to Home Page
    Go to Amar Daraz Page
    [Teardown]    Log Out

TC09_Home_Search_Option_Functionality_Checking
    [Documentation]    This will check the search function return the product based on search keyword
    Login    ${USEREMAIL}      ${PASSWORD}
    Click daraz Logo
    Search Product On Search Option    ${SearchKeyword1}
    
