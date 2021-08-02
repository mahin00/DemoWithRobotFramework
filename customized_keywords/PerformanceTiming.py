from robot.libraries.BuiltIn import BuiltIn
import csv
import datetime
import time
from os import path


class PerformanceTiming:


    def __init__(self, filename='resource_output.csv'):
        self.filename = filename

    def Measure_Time(self, function, type_operation,test_type,nfr,user_type,user_name):

        for loop_count in range(60):
            if  function ==  "login":
                load_time = self.Measure_Login(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Home_Search":
                load_time = self.Measure_Home_Search(type_operation ,test_type,loop_count,nfr,user_type,user_name)
            elif function == "Home_Search_All":
                load_time = self.Measure_Home_Search_All(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Home_Facets_Apply":
                load_time = self.Measure_Home_Facets(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Home_Facets_Clear":
                load_time = self.Measure_Home_Facets_Clear(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Home_Bar_Chart":
                load_time = self.Measure_Home_Bar_Chart(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "List_View_Search":
                load_time = self.Measure_List_View_Search(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "List_View_Facets_Apply":
                load_time = self.Measure_List_View_Facets(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "List_View_Facets_Clear":
                load_time = self.Measure_List_View_Facets_Clear(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "List_View_Pagination":
                load_time = self.Measure_List_View_Pagination(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Traversal":
                load_time = self.Measure_Traversal(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Neighbours":
                load_time = self.Measure_Neighbours(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Map_View_Switch":
                load_time = self.Measure_Map_View_Switch(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Map_View_Search":
                load_time = self.Measure_Map_View_Search(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Map_View_Facets_Apply":
                load_time = self.Measure_Map_View_Facets(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Map_View_Facets_Clear":
                load_time = self.Measure_Map_View_Facets_Clear(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Analyse_Summary_Assets":
                load_time = self.Measure_Analyse_Summary_Assets_Under_Analysis(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Analyse_Summary_Relationships":
                load_time = self.Measure_Analyse_Summary_Relationships(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Analyse_Usage_Switch":
                load_time = self.Measure_Analyse_Usage_Switch(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Analyse_Usage_Search":
                load_time = self.Measure_Analyse_Usage_Search(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Analyse_Usage_Search_All":
                load_time = self.Measure_Analyse_Usage_Search_All(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Analyse_Compliance_Switch":
                load_time = self.Measure_Analyse_Compliance_Switch(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Analyse_Compliance_Search":
                load_time = self.Measure_Analyse_Compliance_Search(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Analyse_Compliance_Search_All":
                load_time = self.Measure_Analyse_Compliance_Search_All(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Legacy_Workflow_Switch":
                load_time = self.Measure_Action_Workflow_Switch(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Legacy_Workflow_Search":
                load_time = self.Measure_Action_Workflow_Search(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Legacy_Workflow_Search_All":
                load_time = self.Measure_Action_Workflow_Search_All(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Execute_Report":
                load_time = self.Measure_Action_Execute_Report(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Measure_Glossary_Tab_Search":
                load_time = self.Measure_Glossary_Tab_Search(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Glossary_Tab_Facets_Apply":
                load_time = self.Measure_Glossary_Tab_Facets(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Glossary_Tab_Facets_Clear":
                load_time = self.Measure_Glossary_Tab_Facets_Clear(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Switch_To_Glossary_Tab_From_List_View":
                load_time = self.Measure_Switch_To_Glossary_Tab_From_List_View(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Switch_To_List_View_From_Glossary_Tab":
                load_time = self.Measure_Switch_To_List_View_From_Glossary_Tab(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Measure":
                load_time = self.Measure_All_Resources(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Enrich_Open":
                load_time = self.Measure_Enrich_Open(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Enrich_Edit":
                load_time = self.Measure_Enrich_Edit(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Change_Workflow_Dashboard_Type":
                load_time = self.Measure_Action_Workflow_Type_Change(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Change_Compliance_Dashboard_Type":
                load_time = self.Measure_Analyse_Compliance_Dashboard_Type_Change(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "Change_Usage_Dashboard_Type":
                load_time = self.Measure_Analyse_Usage_Dashboard_Type_Change(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "List_View_Sorting":
                load_time = self.Measure_List_View_Sorting(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "List_View_Keep_Only":
                load_time = self.Measure_Keep_Only(type_operation , test_type,loop_count,nfr,user_type,user_name)
            elif function == "List_View_Bulk_Edit":
                load_time = self.Measure_Bulk_Edit(type_operation , test_type,loop_count,nfr,user_type,user_name)

            if  load_time > 0.001:
                break
            time.sleep(10)
            print("sleep for 10 seconds")
            print("Loop Number",loop_count)
        return load_time



    # Below public method names are used as keywords
    def Measure_Login(self,type_operation , test_type,loop_count,nfr,user_type,user_name):
        checked_resources = ['favouriteQueries','viewUserActionHistory', 'chartStats']
        return self.Measure_Resources("main.css", "chartStats",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Home_Search(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['checkQueryComplexity','search','facets','fullContext', 'chartStats']
        return self.Measure_Resources("checkQueryComplexity", "chartStats", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Home_Search_All(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['checkQueryComplexity','search','facets','fullContext', 'chartStats']
        return self.Measure_Resources("checkQueryComplexity", "chartStats", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Home_Facets(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['query','chartStats']
        return self.Measure_Resources("query", "chartStats",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Home_Facets_Clear(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['query','chartStats']
        return self.Measure_Resources("query", "chartStats", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_List_View_Search(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['search','fullContext','datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("checkQueryComplexity", "datatableAjax?dataTableName=EXPLORE",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Home_Bar_Chart(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['queryBarChart','datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("queryBarChart","datatableAjax?dataTableName=EXPLORE",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_List_View_Pagination(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("csrf","datatableAjax?dataTableName=EXPLORE",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_List_View_Facets(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['query','datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("query", "datatableAjax?dataTableName=EXPLORE",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_List_View_Facets_Clear(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['query','datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("query", "datatableAjax?dataTableName=EXPLORE",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Traversal(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("validateGovernanceSettingsCompliance", "datatableAjax?dataTableName=EXPLORE", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Neighbours(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("validateGovernanceSettingsCompliance", "datatableAjax?dataTableName=EXPLORE", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Map_View_Switch(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['visualizeNodes', 'getRotationList']
        return self.Measure_Resources("visualizeNodes", "getRotationList", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Map_View_Search(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['visualizeNodes', 'getRotationList']
        return self.Measure_Resources("checkQueryComplexity", "getRotationList",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Map_View_Facets(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['visualizeNodes', 'getRotationList']
        return self.Measure_Resources("query", "getRotationList", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Map_View_Facets_Clear(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['visualizeNodes', 'getRotationList']
        return self.Measure_Resources("query", "getRotationList", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Analyse_Summary_Assets_Under_Analysis(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['activeNodeSummary']
        return self.Measure_Resources("activeNodeSummary", "activeNodeSummary",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Analyse_Summary_Relationships(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['relationshipSummary']
        return self.Measure_Resources("relationshipSummary", "relationshipSummary",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Analyse_Usage_Switch(self,type_operation ,test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['matrix?rowLabel']
        return self.Measure_Resources("matrixControls", "matrix?rowLabel",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Analyse_Usage_Search(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['fullContext','search', 'matrix','facets']
        return self.Measure_Resources("checkQueryComplexity", "fullContext",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Analyse_Usage_Search_All(self,type_operation ,test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['search', 'matrix','facets','fullContext']
        return self.Measure_Resources("checkQueryComplexity", "fullContext",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Analyse_Compliance_Switch(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['scatterChart','pivotTable']
        return self.Measure_Resources("scatterChart", "pivotTable", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Analyse_Compliance_Search(self,type_operation ,test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['scatterChart','pivotTable','facets']
        return self.Measure_Resources("checkQueryComplexity", "pivotTable",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Analyse_Compliance_Search_All(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['scatterChart','pivotTable','facets']
        return self.Measure_Resources("checkQueryComplexity", "pivotTable",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Action_Workflow_Switch(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = [ 'workflow']
        return self.Measure_Resources("workflow", "workflow", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Action_Workflow_Search(self,type_operation ,test_type, loop_count,nfr,user_type, user_name):
        checked_resources = [ 'search','fullContext','facets']
        return self.Measure_Resources("checkQueryComplexity", "fullContext", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Action_Workflow_Search_All(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['facets','fullContext','search']
        return self.Measure_Resources("checkQueryComplexity", "fullContext",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Action_Execute_Report(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['report','datatableAjax']
        return self.Measure_Resources("report", "datatableAjax",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Glossary_Tab_Search(self, type_operation ,test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['datatableAjax?dataTableName=GLOSSARY']
        return self.Measure_Resources("checkQueryComplexity", "datatableAjax?dataTableName=GLOSSARY",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Glossary_Tab_Facets(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['query','datatableAjax?dataTableName=GLOSSARY']
        return self.Measure_Resources("query", "datatableAjax?dataTableName=GLOSSARY", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Glossary_Tab_Facets_Clear(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['query','datatableAjax?dataTableName=GLOSSARY']
        return self.Measure_Resources("query", "datatableAjax?dataTableName=GLOSSARY", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Switch_To_Glossary_Tab_From_List_View(self, type_operation ,test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['filterContext?dataTableName=GLOSSARY','datatableAjax?dataTableName=GLOSSARY']
        return self.Measure_Resources("filterContext?dataTableName=GLOSSARY", "datatableAjax?dataTableName=GLOSSARY", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Switch_To_List_View_From_Glossary_Tab(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['filterContext?dataTableName=EXPLORE','datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("filterContext?dataTableName=EXPLORE", "datatableAjax?dataTableName=EXPLORE", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Enrich_Open(self, type_operation ,test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['enrich?id','discussion?subject=node']
        return self.Measure_Resources("enrich?id", "discussion?subject=node",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Enrich_Edit(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['submit','discussion?subject=node']
        return self.Measure_Resources("submit", "discussion?subject=node",type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Action_Workflow_Type_Change(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = [ 'workflow']
        return self.Measure_Resources("workflow", "workflow", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Analyse_Usage_Dashboard_Type_Change(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = [ 'matrix']
        return self.Measure_Resources("matrix", "matrix", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Analyse_Compliance_Dashboard_Type_Change(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = [ 'pivotTable']
        return self.Measure_Resources("pivotTable", "pivotTable", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_List_View_Sorting(self,type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = [ 'datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("datatableAjax?dataTableName=EXPLORE", "datatableAjax?dataTableName=EXPLORE", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Keep_Only(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['multiKeepOnly','datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("validateGovernanceSettingsCompliance", "datatableAjax?dataTableName=EXPLORE", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Measure_Bulk_Edit(self, type_operation , test_type, loop_count,nfr,user_type, user_name):
        checked_resources = ['update','datatableAjax?dataTableName=EXPLORE']
        return self.Measure_Resources("update", "datatableAjax?dataTableName=EXPLORE", type_operation ,test_type, checked_resources, loop_count,nfr,user_type,user_name)

    def Clear_Resources(self):
        self.Clear_API_Cache()

    def Measure_All_Resources(self, type_operation, test_type,loop_count,nfr,user_type,user_name):
        return self.All_Resources(type_operation , test_type, loop_count,nfr,user_type,user_name)

    # Below private methods are used by above public methods

    def Measure_Resources(self, start_resource, end_resource, operation_type,  test_type, checked_resources, loop_count,nfr,user_type,user_name):
        sl = BuiltIn().get_library_instance('SeleniumLibrary')
        driver = sl.driver

        ''' Use Resource Timing  API to calculate the timings that matter the most '''
        resource_timing = driver.execute_script('''
            let resourceList = window.performance.getEntriesByType("resource");
            let resourceLength = 0;
            let completeResourceLoad;
            let maxResourceLoad = 0;
            let validResources = [];    // Resources which started after given first resource
            
            let checkedResources = arguments[2];
            let checkedResourceLength = checkedResources && checkedResources.length > 0 ? checkedResources.length : 0;

            let stallTimeArray = [];
            let nameArray = [];
            let validNameArray = [];
            let stallSum = 0;
            let first = 0;
            let firstStartTime = 10000000000; // this is dummy big value to avoid previously started resources
            let last = 0;

            for (let i = 0; i < resourceList.length; i++) {
                let resourcePrefixArray = resourceList[i].name.split('/');
                if (resourcePrefixArray && resourcePrefixArray.length > 0) {
                    let resourcePrefix = resourcePrefixArray[resourcePrefixArray.length - 1];
                    let timingMap = getTiming(resourceList[i]);
                    nameArray[nameArray.length] = resourcePrefix;

                    if (resourcePrefix.includes(arguments[0])) {
                        first = resourceList[i];
                        firstStartTime = resourceList[i].startTime;
                    } else if (resourcePrefix.includes(arguments[1])) {
                        last = resourceList[i];
                    }
                    
        
                    if (resourceList[i].startTime >= firstStartTime) {
                        resourceLength++;
                        validResources[validResources.length] = resourceList[i];
                        validNameArray[validNameArray.length] = resourcePrefix;
                        stallTimeArray[stallTimeArray.length] = timingMap["Stall_Time"];
                        stallSum = stallSum + timingMap["Stall_Time"];
                    }
                }
            }
            
            // Waiting for additional resources specified
            if (checkedResourceLength) {
                let isAllResIncluded = true;
                for (let j = 0; j < checkedResourceLength; j++) {
                    let checkedRes = checkedResources[j];
                    let isCurrentIncluded = false;
                    for (let i = 0; i < validNameArray.length; i++) {
                        let name = validNameArray[i];
                        if (name && checkedRes && name.includes(checkedRes)) {
                            isCurrentIncluded = true;
                        }
                    }
                    isAllResIncluded = isAllResIncluded && isCurrentIncluded
                }
                if (isAllResIncluded) {
                    validResources.sort(function (a, b) {
                        return b.responseEnd - a.responseEnd;
                    });
                    
                    if (validResources.length > 0) {
                        maxResourceLoad = validResources[0].responseEnd - validResources[validResources.length - 1].startTime;
                    }
                }
            }
        
            stallTimeArray.sort(function (a, b) {
                return b - a;
            });
            
            if (first !== 0 && last === 0 && arguments[0] === arguments[1]) {
                last = first;
            }
            
            completeResourceLoad = last.responseEnd - first.startTime;
        
            let max = stallTimeArray[0];
            let min = stallTimeArray[stallTimeArray.length - 1];
            let avg = stallSum / (stallTimeArray.length - 1);
            let sum = stallSum;
        
            return [round(max), round(min), round(avg), round(sum), round(completeResourceLoad), resourceLength, round(maxResourceLoad), nameArray, first.startTime, last.responseEnd];
        
            function getTiming(resourceObj) {
                let timingMap = {};
        
                if (resourceObj) {
                    let stallTime = resourceObj.requestStart - resourceObj.connectEnd;
                    let serverTime = resourceObj.responseStart - resourceObj.requestStart;
                    let contentDownloadingTime = resourceObj.responseEnd - resourceObj.responseStart;
                    let completeTime = resourceObj.responseEnd - resourceObj.startTime;
        
                    timingMap["Stall_Time"] = stallTime;
                    timingMap["Server_Time"] = serverTime;
                    timingMap["Content_Downloading_Time"] = contentDownloadingTime;
                    timingMap["Complete_Resource_Time"] = completeTime;
                }
        
                return timingMap;
            }
            
            function round(value, decimals) {
                let deci = decimals ? decimals : 3; // Default to set it to show milliseconds
                let val = value ? value/1000 : value;
                return Number(Math.round(val + 'e' + deci) + 'e-' + deci);
            }
        ''', start_resource, end_resource, checked_resources)

        is_checked_available = checked_resources and len(checked_resources) > 0
        is_last_loop = is_checked_available and loop_count == 50

        # Sending results to display
        self.Display_Test_Results(resource_timing, operation_type,   test_type,  is_last_loop,nfr,user_type,user_name)
        output = resource_timing[4]
        if checked_resources and len(checked_resources) > 0:
            output = resource_timing[6]

        return output   # Returning Loading Times to compare

    def All_Resources(self, type_operation  ,test_type, loop_count,nfr,user_type,user_name):
        sl = BuiltIn().get_library_instance('SeleniumLibrary')
        driver = sl.driver

        # ''' Use Navigation Timing  API to calculate the timings that matter the most '''
        # navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        # responseStart = driver.execute_script("return window.performance.timing.responseStart")
        # loadEnd = driver.execute_script("return window.performance.timing.loadEventEnd")

        ''' Use Resource Timing  API to calculate the timings that matter the most '''
        resource_timing = driver.execute_script('''
            let resourceList = window.performance.getEntriesByType("resource");
            let resourceLength = resourceList.length;
            let completeResourceLoad = 0;
            let maxResourceLoad = 0;

            let stallTimeArray = [];
            let nameArray = [];
            let stallSum = 0;
            let first = {startTime: 0};
            let last = {responseEnd: 0};
        
            if (resourceList.length > 0) {
                first = resourceList[0];
                last = resourceList[resourceList.length - 1];
        
                completeResourceLoad = last.responseEnd - first.startTime;
            }
        
            for (let i = 0; i < resourceList.length; i++) {
                let resourcePrefixArray = resourceList[i].name.split('/');
                if (resourcePrefixArray && resourcePrefixArray.length > 0) {
                    let timingMap = getTiming(resourceList[i]);
                    nameArray[nameArray.length] = resourcePrefixArray[resourcePrefixArray.length -1];

                    stallTimeArray[stallTimeArray.length] = timingMap["Stall_Time"];
                    stallSum = stallSum + timingMap["Stall_Time"];
                }
            }
        
            stallTimeArray.sort(function (a, b) {
                return b - a
            });
        
            let max = stallTimeArray[0];
            let min = stallTimeArray[stallTimeArray.length - 1];
            let avg = stallSum / (stallTimeArray.length - 1);
            let sum = stallSum;
        
            return [round(max), round(min), round(avg), round(sum), round(completeResourceLoad), resourceLength, maxResourceLoad, nameArray];
        
            function getTiming(resourceObj) {
                let timingMap = {};
        
                if (resourceObj) {
                    let stallTime = resourceObj.requestStart - resourceObj.connectEnd;
                    let serverTime = resourceObj.responseStart - resourceObj.requestStart;
                    let contentDownloadingTime = resourceObj.responseEnd - resourceObj.responseStart;
                    let completeTime = resourceObj.responseEnd - resourceObj.startTime;
        
                    timingMap["Stall_Time"] = stallTime;
                    timingMap["Server_Time"] = serverTime;
                    timingMap["Content_Downloading_Time"] = contentDownloadingTime;
                    timingMap["Complete_Resource_Time"] = completeTime;
                }
        
                return timingMap;
            }
            
            function round(value, decimals) {
                let deci = decimals ? decimals : 3; // Default to set it to show milliseconds
                let val = value ? value/1000 : value;
                return Number(Math.round(val + 'e' + deci) + 'e-' + deci);
            }
        ''')

        # Sending results to display
        self.Display_Test_Results(resource_timing, type_operation ,   test_type,  loop_count,nfr,user_type,user_name)
        return resource_timing[4]   # Returning 'Complete Loading Time' to compare

    @staticmethod
    def Clear_API_Cache():
        sl = BuiltIn().get_library_instance('SeleniumLibrary')
        driver = sl.driver
        clearResponse = driver.execute_script('''
                window.performance.clearResourceTimings();
                let resourceList = window.performance.getEntriesByType("resource");
                return resourceList === "[]";
            ''')
        print("Previous resources are cleared %s" % clearResponse)

    # Display Resource API output in a csv file

    def Display_Test_Results(self, results_array, operation_type,   test_type, is_last_loop, nfr,user_type,user_name):
        current_date_time = datetime.datetime.now()
        date = current_date_time.strftime("%d-%m-%Y")
        time = current_date_time.strftime("%H:%M:%S")
        display_array = [date, time, test_type,   operation_type,   nfr,user_type,user_name]
        csv_results = results_array[:-3]
        display_array = display_array + csv_results

        if is_last_loop or results_array[6] > 0:
            if not path.exists(self.filename):
                test_file = open(self.filename, 'w')
                test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                header_row = ['Date', 'Time',  'Search Type',  'Type of Operation','NFR','User Type','User Name','Maximum Stall Time', 'Minimum Stall Time', 'Average Stall Time', 'Sum of Stall Times', 'Page Loading Time','Number of Resources','Complete Loading Time']
                test_writer.writerow(header_row)

            print("Writing results to CSV")

            with open(self.filename, mode='a') as test_file:
                test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                test_writer.writerow(display_array)

        print("Complete Loading s: %s secs" % results_array[6])
        print("Page Loading Time: %s secs" % results_array[6])
        print("Maximum Stall Time: %s secs" % results_array[0])
        print("Minimum Stall Time: %s secs" % results_array[1])
        print("Average Stall Time: %s secs" % results_array[2])
        print("Sum of Stall Times: %s secs" % results_array[3])
        print("Number of Resources: %s" % results_array[5])
        print("Start time: %s Milli seconds" % results_array[8])
        print("End time: %s milli seconds" % results_array[9] )

        for x in range(len(results_array[7])):
            print(results_array[7][x])