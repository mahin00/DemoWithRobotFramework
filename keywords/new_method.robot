*** Settings ***
Resource          ../settings/common_settings.robot

*** Variables ***
${Succees}        Successfully
*** Keywords ***
Search Bar Is Visible
    [Documentation]    Passes if search bar is visible
    Page Should Contain Element    ${SearchField}

Click Search Field
    [Documentation]    Click on the search Field from the search box
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Click Element    xpath=${SearchField}  
    Sleep    ${DELAY}

Click Search Button
    [Documentation]    Click on the search Field from the search box
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Click Element    ${XP_SEARCH_BUTTON}
    Sleep    ${DELAY}

Search Product On Search Option
    [Arguments]       ${SearchKeyword}
    [Documentation]    Input SearchKeyword
    Search Bar Is Visible
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Input Text       ${SearchField}    ${SearchKeyword1}
    Click Search Button
    Sleep    ${DELAY}