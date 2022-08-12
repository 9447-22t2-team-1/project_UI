
![Sahara](logo4.png)


# Sahara

This documentation will take the reader through **Installation**, **Usage** and **Additional notes** regarding the Sahara project

## Installation
>Currently, Sahara is dependent on us to run and manage the frontend. The following steps are a guide to set things up on a new sandbox environment

Most of our installation is completed via a AWS CloudFormation template, covering our EC2, API Gateway, DynamoDB and Lambda. 
This can be found in the repo as `template.yaml`

Before installation, users will need to provide their own key-pair, security policy and subnet ID.

### Official AWS
Users will need to navigate to the **CloudFormation** service in AWS. That can be found [here](https://ap-southeast-2.console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks?filteringStatus=active&filteringText=&viewNested=true&hideStacks=false)

Users will navigate to **Stacks** then choose to **Create stack**/**With new resources** on the top right of the table.

Users must select **Template is ready** and specify. Users are then prompted to upload a template file, which should be `template.yaml` from the repository. 

Users will be able to enter their stack name (such as 'MyStack') and then proceed.

Skip to the last stage and agree to the AWS permissions, then proceed to creation. After waiting a short amount of time, the service is ready to be used.

## Testing
To ensure everything is setup correctly, we will test the Lambda functions

### Testing the first Lambda function: 
Additional configuration is needed for our first function.
#### Getting a subnet and security group ID

Users will need to navigate to the **VPC** service and click **Subnets** on the navigation page. They need to have a valid*Subnet ID*. Copy this ID.

Users will also need to get their *Security Group ID* policy from the **Security Groups** on the navigation page. Copy this ID.

Users will then go to the **Lambda** then the **Functions** service and click on the *InitEC2* Lambda function. Clicking on the *InitEC2* hyperlink, then **Configuration**, then **Environment variables** and click **edit**. Users will put their security and subnet ID in here.

Users can test the program by clicking the **Test** button, provide a test name, and then paste the following into the **Event JSON field**

```
{ "userID": "1", "title": "postAPI", "pipeline": "eyJCdWlsZCI6W3siaWQiOiIwIiwiZGF0YSI6Imh0dHBzOi8vZ2l0aHViLmNvbS9zbnlrL2NsaSJ9XSwiVGVzdCI6W10sIkRlcGxveSI6W119" }
```
Users click save and then launch a test. If successful, the Execution result should be a *Status Code 200* with the ID of the pipeline provided. Users can go to **DynamoDB**, **Tables** and search for our table *PipelineTable*. On this table, click *explore table items*. A new pipeline ID should be here that matches the result ID.

### Testing the second Lambda function
Users will then go to the **Lambda** then the **Functions** service and click on the *QueryReportFunction* Lambda function.

Users can test the program by clicking the **Test** button, provide a test name, and then paste the following into the **Event JSON field**
```
{ "queryStringParameters": { "userID": "1" } }
```
Users click save and then launch a test. If successful, the Execution result should be a *Status Code 200* with  the pipeline and its result in *base64*

## Build
Go to **API Gateway**, and click on our entry named *API*.

 Click on **Resources** on the left pane, click on the Root icon (i.e.`/`) then click *Actions*, and *Deploy API*
Users can name and describe their stage e.g. ("Demo Stage"), and click *Deploy*.

AWS will give them an public facing API address, which they get the report remotely, based off the user ID.

## Usage
We currently offer two ways to use Sahara, via API or GUI.
### API Usage
Users need to get the provided API from the *Build* step to interact with our API.

Users can use and API platform like [PostAPI](https://www.postman.com/) to interact with their provided API. 

Sending a GET request will fetch the results of a previously run test.
To send a GET request, users can paste the following such as 
`userID` with a value of `1` and send to the API address. The return value is base64 encoded of the result of the pipeline for User 1.  

Sending a POST request will send the results of pipeline into the database.
To send a POST request, select the Body and paste the following in:
```
{ "userID": "1", "title": "postAPI", "pipeline": "eyJCdWlsZCI6W3siaWQiOiIwIiwiZGF0YSI6Imh0dHBzOi8vZ2l0aHViLmNvbS9zbnlrL2NsaSJ9XSwiVGVzdCI6W10sIkRlcGxveSI6W119" }
```
This will return a *Status Code 200* if successful.

### GUI Usage

Users are supposed to interact with Sahara through our *Graphical User Interface* (GUI). Users will find our website and will be able to navigate to our login screen
> As this is a proof-of-concept, there are currently no accounts, so any username/password combination will be accepted for the time being.  

Once through, the user is presented the dashboard. This hub will show the user feedback from previous pipelines, any significant warnings, the ability to create new pipeline and more planned features 
#### Creating a new Pipeline
Once on the dashboard, navigate to the **New Service Pipeline** button at the top of the screen. Clicking this will send you to another page, responsible for pipeline creation

Here, you will find boxes on the left and a pipeline in the middle.  The boxes on the left represent the services *Sahara* officially offers.  To choose a service for the pipeline, the user can click and drag the box into the middle of the screen, representing the pipeline order. The pipeline is run from top to bottom, so users can choose their order preference. 

Once a service is added onto the pipeline, it can be deleted with the garbage can icon if the user is unhappy with it. Additionally, users can click on the service to control and modify its parameters.
> As this is a proof-of-concept, the only parameter applicable is the address to the desired target (a public GitHub repository). **This will have to be configured for each service in the pipeline**
> 
Pipeline creation is performed one step at a time, *i.e. Users choose their Build stage, then click verify in order to progress to creating the next stage*

#### Running the Pipeline
Once all stages in the pipeline creation is complete, click **Verify and Continue** to send the information to the backend infrastructure. A prompt will confirm that this has happened and redirect the user back onto the dashboard.

Users may have to wait for the backend to run before they can view results. The length of this wait is determined on factors like the size, number of items, choice of services and ordering.
#### Viewing the Pipeline results
Once on the dashboard, the bottom left of the screen contains the **Reports** box. This list will contain all reports from the user. Once the pipeline has been run to completion, the status will change from *Running* to *Done*. Clicking on the report will show the date when the service ran,  and the report file itself
> Currently the report structure is a text log containing the output of the service (Typically JSON). In the future we plan to support other file types like PDF and HTML for a more graphical communication of statistics.

The report will contain the output of all the services, in order of their execution (specified by the user in creation). Each report entry is also dated with when it was run by the backend.

## Additional notes
Here is some miscellaneous information which you may find helpful
- Currently, in the pipeline creation, each service must be configured with the target repository  in order for the service to work. We were unsure if users wanted to run the same pipeline but against different repositories so we kept this as a feature, despite its potentially confusing behavior.
- Target repositories **must be made public**. So far, our testing has only been with GitHub, but it is equally likely that other git services will also work.
