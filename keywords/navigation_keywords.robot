*** Settings ***
Resource          ../settings/common_settings.robot

*** Keywords ***
Go To Login Page
    Go To    ${URL}
    Login Page Should Be Open
    Sleep     ${SHORT_DELAY}

Scroll Bottom of the Page
    Execute JavaScript    window.scrollTo(0, document.body.scrollHeight)
    Sleep    3

Click daraz Logo
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Page Should Contain Element    ${logo}
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Click Element    ${logo}

Go To Home Page
    Go To    ${HomePage}
    Sleep    ${SHORT_DELAY}

Go To About Us Page
     Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Click Element       ${AboutUS}
     Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    title should be     ${AboutUsTitle}
     Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Page Should Contain Element    xpath=//body[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[1]/p[1]/img[1]
Go to Career Page
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Click Element    ${CareerPage} 
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    title should be  ${CareerTitle}

Go to Amar Daraz Page
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Click Element    ${AmarDaraz}
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    title should be  ${AmarDarazTitle}
    
Scroll Page To Location
    [Arguments]    ${x_location}=0    ${y_location}=0
    [Documentation]    Scrolls to a particular location on the page, by default this is the top of the page
    Execute JavaScript    window.scrollTo(${x_location},${y_location})

Scroll To Bottom Of Page
    Execute JavaScript    window.scrollTo(0,document.body.scrollHeight);
