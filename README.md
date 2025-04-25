# api_test_automation

## 1. Installation

1.1 Install JDK >= 1.8  
https://www.oracle.com/hk/java/technologies/downloads/archive/  
Require add JDK path to system environment variable `"JAVA_HOME"`.

1.2 Python >= 3.10  
https://www.python.org/downloads/  
In the virtual environment of the project, use this command to add dependencies:  
`pip install -r requirements.txt`

1.3 allure  
`irm get.scoop.sh | iex`  
`scoop install allure`  
After installation, use `allure --version` for checking whether the installation is correct.  
Also, the installation path of allure (typically `C:\Users\<current user>\scoop\apps\allure\current`) needs to be added
in environment variable `ALLURE_HOME` and `PATH`.

## 2. Project infrastructure
api_test_automation&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Project root*  
│  
├─allure-results&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Storage of test results for report generation*  
│  
├─api_data&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Storage API data to be used*  
│  
├─api_lib&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Storage of defined domains and APIs*    
│  
├────common&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Commonly used functions, API instances and config files*  
│&ensp;&ensp;&ensp; │  
│&ensp;&ensp;&ensp; └─base_classes&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Base definitions of domain/API. All actual definitions must inherit these classes*  
│  
├─features&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*BDD feature files*  
│  
└─steps&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*BDD step files*

## 3. Steps for creating a new test
 - Create feature file and generate blank step definitions.
 - Manually run the test case in Postman, note down the API interacted, structure of data/params/response body, etc.
 - Check whether the domain/API above is already created in `api_lib`, if not:
   - Create a new `<domain name>_api.py` in `api_lib`, and `<domain name>_api_data.py` in `api_data` if the domain does not exist;
   - Create definitions for the new API after the previous step, if the domain exists yet API does not, create API directly;
   - Create API data (e.g. params, data) in `<domain name>_api_data.py`.
 - Using the defined APIs, fill in the step definitions created before.  
  
## 4. Execution
 - Open a command line prompt and change directory to project root;
 - Use `behave` to run all features under `features` folder, or:
 - Use `behave ./features/<feature name>.feature` to run a specific feature;
 - After execution, use `allure serve` to view the html report.  

## 5. Demo test case design
The API is retrieved from:  
https://data.gov.hk/en-data/dataset/hk-hko-rss-9-day-weather-forecast/resource/c91dace6-d45a-44b3-9474-1b2c3d9acd75  

In order to:
 - Send a request using this API endpoint with your preferred language 
 - Test the request response status is whether successful or not 
 - Extract the relative humidity (e,g, 60 - 85%) for the day after tomorrow from the API response 
  
The following feature is designed: 
  
`When I access the API for 9 day weather`  
In this step, the codes will directly access the URL and gain the response data.

`Then I should see the status is OK `   
This step checks the response status code. If it is 200, then the step will pass. Otherwise, the infrastructure will throw the exception.

`And I should see the relative humidity data for the day after tomorrow `   
Based on the results shown by Postman, the response body is a json, hence the codes will parse the json and try to retrieve the data for the day after tomorrow. If the data if not None or empty, then the test will pass.
  
