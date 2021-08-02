*** Variables ***

# Not currently used, need to remove split up IT and Workflow and other potential services that can be turned off
@{ALL_FUNCTIONAL_COMPONENTS}
...    Ontology Administration
...    Assets Administration

...    Model Editor
...    Classifications
...    Rulesets

...    User Guidance

...    Summary
...    Watch
...    Reporting
...    Compliance
...    Usage

...    Workflow Dashboard
...    Classic Workflow
...    My Tasks

# Not currently used, need to remove split up IT and Workflow and other potential services that can be turned off
@{ALL_SECURITY_COMPONENTS}
...    Public API

...    User Admin
...    Role Admin

...    User Audit

...    Action
...    Analyse

...    Create Node
...    Read Node
...    Update Node
...    Delete Node

...    Create Relationship
...    Read Relationship
...    Update Relationship
...    Delete Relationship

...    Import Manager
...    Rollback Assets
...    Export

...    Read Intelligent Tagging Model
...    Edit Intelligent Tagging Model

...    Create Classification
...    Delete Classification
...    Vote Classification
...    Run Classify Job
...    Rollback Classify Job

...    Create Ruleset
...    Read Ruleset
...    Edit Ruleset
...    Delete Ruleset
...    Export Ruleset

...    Business Glossary

...    Workflow Administration
...    View All Workflow Definitions
...    View All Workflow Instances
...    View All Workflow Tasks
...    Read Asset Workflow
...    Start Workflow

# this user has "Create Node" permission turned off
@{NO_CREATE_NODE_SECURITY_PERMISSIONS}
...    Public API
...    User Admin
...    Role Admin
...    User Audit
...    Action
...    Analyse
...    Read Node
...    Update Node
...    Delete Node
...    Create Relationship
...    Read Relationship
...    Update Relationship
...    Delete Relationship
...    Import Manager
...    Rollback Assets
...    Export
...    Business Glossary
...    Workflow Administration
...    View All Workflow Definitions
...    View All Workflow Instances
...    View All Workflow Tasks
...    Read Asset Workflow
...    Start Workflow

# this user only has permissions that are read only
@{READ_ONLY_SECURITY_PERMISSIONS}
...    Public API
...    User Admin
...    Role Admin
...    Action
...    Analyse
...    Read Node
...    Read Relationship
...    Business Glossary
...    View All Workflow Definitions
...    View All Workflow Instances
...    View All Workflow Tasks
...    Read Asset Workflow

# because IT can be turned off
@{READ_ONLY_SECURITY_PERMISSIONS_IT}
...    Read Intelligent Tagging Model
...    Read Ruleset

# this user only has permissions that are read and write only
@{READ_AND_WRITE_ONLY_SECURITY_PERMISSIONS}
...    Public API
...    User Admin
...    Role Admin
...    Action
...    Analyse
...    Create Node
...    Read Node
...    Update Node
...    Create Relationship
...    Read Relationship
...    Update Relationship
...    Import Manager
...    Business Glossary
...    View All Workflow Definitions
...    View All Workflow Instances
...    View All Workflow Tasks
...    Read Asset Workflow

# because IT can be turned off
@{READ_AND_WRITE_ONLY_SECURITY_PERMISSIONS_IT}
...    Read Intelligent Tagging Model
...    Edit Intelligent Tagging Model
...    Create Classification
...    Vote Classification
...    Create Ruleset
...    Read Ruleset
...    Edit Ruleset


# Test users

# Users with Admin Role
${USER_INIT}                  user2
# ${USER_IMPORT}                import
${USER_IMPORT}                user2

# ${USER_HOME}                  home
${USER_HOME}                  user2




# eikhan theke katchi
# creation
# creation2
# explore1
# explore2
# explore3
# explore4
# explore5
# explore6
# explore7
# explore8
# explore9
# explore10
# explore11
# explore12
# explore13
# explore14
# explore15
# explore16
# search1
#eikhan porjonto
${USER_CREATION}              user2
${USER_CREATION_2}            user2
${USER_EXPLORE_1}             user2
${USER_EXPLORE_2}             user2
${USER_EXPLORE_3}             user2
${USER_EXPLORE_4}             user2
${USER_EXPLORE_5}             user2
${USER_EXPLORE_6}             user2
${USER_EXPLORE_7}             user2
${USER_EXPLORE_8}             user2
${USER_EXPLORE_9}             user2
${USER_EXPLORE_10}            user2
${USER_EXPLORE_11}            user2
${USER_EXPLORE_12}            user2
${USER_EXPLORE_13}            user2
${USER_EXPLORE_14}            user2
${USER_EXPLORE_15}            user2
${USER_EXPLORE_16}            user2
#etotuk 2nd number

# ${USER_SEARCH_1}            asif
${USER_SEARCH_1}              user2
# ${USER_SEARCH_2}              search2
${USER_SEARCH_2}              user2

# ${USER_SEARCH_4}              search4
${USER_SEARCH_4}              user2
# ${USER_SEARCH_5}              search5
${USER_SEARCH_5}              user2
#from here to
${USER_ACTION_1}              user2

${USER_ACTION_2}              user2

${USER_ACTION_3}              user2

${USER_ONTOLOGY_1}            user2

${USER_ONTOLOGY_2}            user2

${USER_ONTOLOGY_3}            user2

${USER_ONTOLOGY_4}            user2

${USER_STACKEDOPS_1}          user2

${USER_STACKEDOPS_2}          user2

${USER_COMPLIANCE}            user2

${USER_ANALYSE}               user2

${USER_USAGE}                 user2

${USER_GLOSSARY_1}            user2

${USER_GLOSSARY_2}            user2

${USER_GLOSSARY_3}            user2

${USER_GLOSSARY_4}            user2

${USER_GLOSSARY_5}            user2

${USER_GLOSSARY_6}            user2

${USER_GLOSSARY_7}            user2

${USER_GLOSSARY_8}            user2

${USER_GLOSSARY_V2_1}         user2

${USER_GLOSSARY_V2_2}         user2

${USER_GLOSSARY_V2_3}         user2

${USER_IT_1}                  user2

${USER_IT_2}                  user2

${USER_IT_3}                  user2

${USER_IT_4}                  user2

${USER_IT_5}                  user2

${USER_IT_6}                  user2

${USER_IT_7}                  user2

${USER_NULL_DISPLAY}          user2

${USER_WORKFLOW}              user2

${USER_WORKFLOW_MANAGER}      user2

${USER_WORKFLOW_MANAGER_2}    user2

${USER_WORKFLOW_MANAGER_3}    user2

${USER_WORKFLOW_NOTIFS}       user2

${USER_WORKFLOW_NOTIFS_2}     user2

${USER_WORKFLOW_DASHBOARD}    user2

${USER_WORKFLOW_DASHBOARD_2}  user2

${USER_WORKFLOW_PROP}         user2

${USER_WORKFLOW_COMMENTS}     user2

${USER_WORKFLOW_REASON}       user2

${USER_WORKFLOW_ADMIN}        user2

${USER_WORKFLOW_TRIGGERS_1}   user2

${USER_WORKFLOW_TRIGGERS_2}   user2

${USER_WORKFLOW_EMAIL_NOTIFS_1}  user2                 
${USER_WORKFLOW_EMAIL_NOTIFS_2}  user2                 
${USER_WORKFLOW_EMAIL_NOTIFS_3}  user2                 
${USER_MISC_FEATURES}             user2 
#############here
#########data of from
# action1
# action2
# action3
# ontology1
# ontology2
# ontology3
# ontology4
# stackedops1
# stackedops2
# compliance
# analyze
# usage
# glossary1
# glossary2
# glossary3
# glossary4
# glossary5
# glossary6
# glossary7
# glossary8
# glossaryV2.1
# glossaryV2.2
# glossaryV2.3
# it1
# it2
# it3
# it4
# it5
# it6
# it7
# nulldisplaytester
# workflow
# manager
# manager2
# manager3
# wf.notifs
# wf.notifs2
# wf.dashboard
# wf.dashboard2
# wf.prop
# wf.comments
# wf.reason
# wf.admin
# wf.triggers1
# wf.triggers2
#    wf.email.notifs1
#   wf.email.notifs2
#    wf.email.notifs3
# ux.miscfeatures

${USER_NOTIFICATIONS_1}       notifications1
${USER_NOTIFICATIONS_2}       notifications2
${USER_RBAC_2}                rbac2             # yes, there is no USER_RBAC_1
${USER_RBAC_3}                rbac3
${USER_RBAC_4}                steward
${USER_RBAC_6}                rbac6
${USER_RBAC_7}                rbac7         #used for robot test automation 

${USER_WORKFLOW_APPLICATION}  workflowuser      # This is the user for the workflow application to connect to Alex. Not to be used for any tests.
${USER_PROFILE_1}             profile
${USER_SWAGGER}               swagger

# Users with Custom Roles
${USER_BUS_NAME_PROTECT}      busnameprotect    # this user has "Business Name" Property set to "Protected"
${USER_NO_CREATE_NODE}        nocreatenode      # this user has "Create Node" permission turned off
${USER_READ_ONLY}             readonly          # this user has "Read Only" permission to Alex
${USER_READ_WRITE_ONLY}       readwriteonly     # this user only has permission on "Read and Write"
${USER_WORKFLOW_SETTINGS}     wf.settings       # assigned to ${UNIQUE_ROLE_NAME}

# Roles
${ROLE_ADMIN}                 Admin             # this is the name of the default admin role
${ROLE_BUS_NAME_PROTECT}      busnameprotect    # this is the name of the role that has "Business Name" Property set to "Protected"
${ROLE_NO_CREATE_NODE}        nocreatenode      # this is the name of the role that has "Create Node" permission turned off
${ROLE_READ_ONLY}             readonly          # this is the name of the role that only have permission on read in Alex
${ROLE_READ_WRITE_ONLY}       readwriteonly     # this is the name of the role that have permission on read and write in Alex
${UNIQUE_ROLE_NAME}           unique_role_name  # used as userWhitelist chosen role
${ROLE_BG_CONSUMER}           BG Consumer       # Business Glossary Read Only role

${DEFAULT_INTELLIGENT_TAGGING_FEEDBACK_WEIGHTING}    1



@{NORMAL_USERS}
...    ${USER_INIT}
...    ${USER_IMPORT}
...    ${USER_HOME}
...    ${USER_CREATION}
...    ${USER_EXPLORE_1}
...    ${USER_EXPLORE_2}
...    ${USER_EXPLORE_3}
...    ${USER_EXPLORE_4}
...    ${USER_EXPLORE_5}
...    ${USER_EXPLORE_6}
...    ${USER_EXPLORE_7}
...    ${USER_EXPLORE_8}
...    ${USER_EXPLORE_9}
...    ${USER_EXPLORE_10}
...    ${USER_EXPLORE_11}
...    ${USER_EXPLORE_12}
...    ${USER_EXPLORE_13}
...    ${USER_EXPLORE_14}
...    ${USER_EXPLORE_15}
...    ${USER_EXPLORE_16}
...    ${USER_SEARCH_1}
...    ${USER_SEARCH_2}
...    ${USER_SEARCH_4}
...    ${USER_SEARCH_5}
...    ${USER_ACTION_1}
...    ${USER_ACTION_2}
...    ${USER_ACTION_3}
...    ${USER_ONTOLOGY_1}
...    ${USER_ONTOLOGY_2}
...    ${USER_ONTOLOGY_3}
...    ${USER_ONTOLOGY_4}
...    ${USER_STACKEDOPS_1}
...    ${USER_STACKEDOPS_2}
...    ${USER_COMPLIANCE}
...    ${USER_ANALYSE}
...    ${USER_USAGE}
...    ${USER_GLOSSARY_1}
...    ${USER_GLOSSARY_2}
...    ${USER_GLOSSARY_3}
...    ${USER_GLOSSARY_4}
...    ${USER_GLOSSARY_5}
...    ${USER_GLOSSARY_6}
...    ${USER_GLOSSARY_7}
...    ${USER_GLOSSARY_8}
...    ${USER_GLOSSARY_V2_1}
...    ${USER_GLOSSARY_V2_2}
...    ${USER_GLOSSARY_V2_3}
...    ${USER_IT_1}
...    ${USER_IT_2}
...    ${USER_IT_3}
...    ${USER_IT_4}
...    ${USER_IT_5}
...    ${USER_IT_6}
...    ${USER_IT_7}
...    ${USER_NULL_DISPLAY}
...    ${USER_WORKFLOW}
...    ${USER_WORKFLOW_MANAGER}
...    ${USER_WORKFLOW_MANAGER_2}
...    ${USER_WORKFLOW_MANAGER_3}
...    ${USER_WORKFLOW_NOTIFS}
...    ${USER_WORKFLOW_NOTIFS_2}
...    ${USER_WORKFLOW_DASHBOARD}
...    ${USER_WORKFLOW_DASHBOARD_2}
...    ${USER_WORKFLOW_PROP}
...    ${USER_WORKFLOW_COMMENTS}
...    ${USER_WORKFLOW_REASON}
...    ${USER_WORKFLOW_ADMIN}
...    ${USER_WORKFLOW_TRIGGERS_1}
...    ${USER_WORKFLOW_TRIGGERS_2}
...    ${USER_WORKFLOW_EMAIL_NOTIFS_1}
...    ${USER_WORKFLOW_EMAIL_NOTIFS_2}
...    ${USER_WORKFLOW_EMAIL_NOTIFS_3}
...    ${USER_MISC_FEATURES}
...    ${USER_NOTIFICATIONS_1}
...    ${USER_NOTIFICATIONS_2}
...    ${USER_RBAC_2}
...    ${USER_RBAC_3}
...    ${USER_RBAC_4}
...    ${USER_WORKFLOW_APPLICATION}
...    ${USER_PROFILE_1}
...    ${USER_SWAGGER}

@{SPECIAL_USERS}
...    ${USER_BUS_NAME_PROTECT}
...    ${USER_NO_CREATE_NODE}
...    ${USER_READ_ONLY}
...    ${USER_READ_WRITE_ONLY}
...    ${USER_WORKFLOW_SETTINGS}

@{SPECIAL_ROLES}
...    ${ROLE_BUS_NAME_PROTECT}
...    ${ROLE_NO_CREATE_NODE}
...    ${ROLE_READ_ONLY}
...    ${ROLE_READ_WRITE_ONLY}
...    ${UNIQUE_ROLE_NAME}

@{EXPLORE_USERS}
...    ${USER_EXPLORE_1}
...    ${USER_EXPLORE_2}
...    ${USER_EXPLORE_3}
...    ${USER_EXPLORE_4}
...    ${USER_EXPLORE_5}
...    ${USER_EXPLORE_6}
...    ${USER_EXPLORE_7}
...    ${USER_EXPLORE_8}
...    ${USER_EXPLORE_9}
...    ${USER_EXPLORE_10}
...    ${USER_EXPLORE_11}
...    ${USER_EXPLORE_12}
...    ${USER_EXPLORE_13}
...    ${USER_EXPLORE_14}
...    ${USER_EXPLORE_15}
...    ${USER_EXPLORE_16}

@{SEARCH_USERS}
...    ${USER_SEARCH_1}
...    ${USER_SEARCH_2}
...    ${USER_SEARCH_4}
...    ${USER_SEARCH_5}

    

@{MISC_USERS_ONE}
...    ${USER_INIT}
...    ${USER_IMPORT}
...    ${USER_HOME}
...    ${USER_CREATION}
...    ${USER_CREATION_2}
...    ${USER_MISC_FEATURES}
...    ${USER_GLOSSARY_4}


@{MISC_USERS_TWO}
...    ${USER_ACTION_1}
...    ${USER_ACTION_2}
...    ${USER_ACTION_3}
...    ${USER_ONTOLOGY_1}
...    ${USER_ONTOLOGY_2}
...    ${USER_ONTOLOGY_3}
...    ${USER_ONTOLOGY_4}

@{MISC_USERS_FOUR}
...    ${USER_STACKEDOPS_1}
...    ${USER_STACKEDOPS_2}
...    ${USER_COMPLIANCE}
...    ${USER_ANALYSE}
...    ${USER_USAGE}

@{MISC_USERS_THREE}
...    ${USER_MISC_FEATURES}
...    ${USER_RBAC_2}
...    ${USER_RBAC_3}
...    ${USER_RBAC_4}
...    ${USER_NULL_DISPLAY}
...    ${USER_PROFILE_1}
...    ${USER_SWAGGER}

@{WF_USERS}
...    ${USER_WORKFLOW}
...    ${USER_WORKFLOW_MANAGER}
...    ${USER_WORKFLOW_MANAGER_2}
...    ${USER_WORKFLOW_MANAGER_3}
...    ${USER_WORKFLOW_DASHBOARD}
...    ${USER_WORKFLOW_DASHBOARD_2}
...    ${USER_WORKFLOW_PROP}
...    ${USER_WORKFLOW_COMMENTS}
...    ${USER_WORKFLOW_REASON}
...    ${USER_WORKFLOW_ADMIN}
...    ${USER_WORKFLOW_TRIGGERS_1}
...    ${USER_WORKFLOW_TRIGGERS_2}
...    ${USER_WORKFLOW_APPLICATION}

@{BG_USERS}
...    ${USER_GLOSSARY_1}
...    ${USER_GLOSSARY_2}
...    ${USER_GLOSSARY_3}
...    ${USER_GLOSSARY_4}
...    ${USER_GLOSSARY_5}
...    ${USER_GLOSSARY_6}
...    ${USER_GLOSSARY_7}
...    ${USER_GLOSSARY_8}

@{BG_V2_USERS}
...    ${USER_GLOSSARY_V2_1}
...    ${USER_GLOSSARY_V2_2}
...    ${USER_GLOSSARY_V2_3}

@{IT_USERS}
...    ${USER_IT_1}
...    ${USER_IT_2}
...    ${USER_IT_3}
...    ${USER_IT_4}
...    ${USER_IT_5}
...    ${USER_IT_6}
...    ${USER_IT_7}

@{NOTIF_USERS}
...    ${USER_NOTIFICATIONS_1}
...    ${USER_NOTIFICATIONS_2}
...    ${USER_WORKFLOW_NOTIFS}
...    ${USER_WORKFLOW_NOTIFS_2}
