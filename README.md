# Sahara

This documentation will take the reader through **Installation**, **Usage** and **Additional notes** regarding the Sahara project

## Installation
Most of our installation is completed via a AWS CloudFormation template, covering our EC2, API Gateway, DynamoDB and Lambda. 
This can be found in the repo as `template.yaml`

Before installation, users will need to provide their own key-pair, security policy and subnet ID.

### Official AWS
Users will need to navigate to the CloudFormation service in AWS. That can be found [here](https://ap-southeast-2.console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks?filteringStatus=active&filteringText=&viewNested=true&hideStacks=false)

Users will then choose to **Create stack**/**With existing resources**. Users are then prompted to upload a template file, which should be `template.yaml`. 

Users will be able to enter in their table names (such as 'Pipeline',) their stack name (such as 'MyStack') and then proceed.

## Usage

Users are supposed to interact with Sahara through our *Graphical User Interface* (GUI). Users will find our website and will be able to navigate to our login screen
> As this is a proof-of-concept, there are currently no accounts, so any username/password combination will be accepted for the time being.  

Once through, the user is presented the dashboard. This hub will show the user feedback from previous pipelines, any significant warnings, the ability to create new pipeline and more planned features 
### Creating a new Pipeline
Once on the dashboard, navigate to the **New Service Pipeline** button at the top of the screen. Clicking this will send you to another page, responsible for pipeline creation

Here, you will find boxes on the left and a pipeline in the middle.  The boxes on the left represent the services *Sahara* officially offers.  To choose a service for the pipeline, the user can click and drag the box into the middle of the screen, representing the pipeline order. The pipeline is run from top to bottom, so users can choose their order preference. 

Once a service is added onto the pipeline, it can be deleted with the garbage can icon if the user is unhappy with it. Additionally, users can click on the service to control and modify its parameters.
> As this is a proof-of-concept, the only parameter applicable is the address to the desired target (a public GitHub repository). **This will have to be configured for each service in the pipeline**
> 
Pipeline creation is performed one step at a time, *i.e. Users choose their Build stage, then click verify in order to progress to creating the next stage*

### Running the Pipeline
Once all stages in the pipeline creation is complete, click **Verify and Continue** to send the information to the backend infrastructure. A prompt will confirm that this has happened and redirect the user back onto the dashboard.

Users may have to wait for the backend to run before they can view results. The length of this wait is determined on factors like the size, number of items, choice of services and ordering.
### Viewing the Pipeline results
Once on the dashboard, the bottom left of the screen contains the **Reports** box. This list will contain all reports from the user. Once the pipeline has been run to completion, the status will change from *Running* to *Done*. Clicking on the report will show the date when the service ran,  and the report file itself
> Currently the report structure is a text log containing the output of the service (Typically JSON). In the future we plan to support other file types like PDF and HTML for a more graphical communication of statistics.

The report will contain the output of all the services, in order of their execution (specified by the user in creation). Each report entry is also dated with when it was run by the backend.

## Additional notes
Here is some miscellaneous information which you may find helpful
- Currently, in the pipeline creation, each service must be configured with the target repository  in order for the service to work. We were unsure if users wanted to run the same pipeline but against different repositories so we kept this as a feature, despite its potentially confusing behavior.
- Target repositories **must be made public**. So far, our testing has only been with GitHub, but it is equally likely that other git services will also work.
