# AI Services at Salesforce 

Mishra, Divyanshu, sp20-516-224

## Einstein AI Overview

Salesforce offers AI services platform called [Einstein Analytics](https://www.salesforce.com/products/einstein-analytics/overview/) which can help organizations build AI 
powered apps quickly for employees and customers.  

It provides features which are grouped under four basic AI Domains.

* **Machine Learning**: Features provided under this category are -
    
    * Einstein Discovery
    * Einstein Prediction Builder
    * Einstein Next Best Action

* **Natural Language Processing**: Features provided under this category are -

    * Einstein Language
    * Einstein Bots    

* **Computer Vision**: Feature provided under this category are -

    * Einstein Vision
    
* **Automatic Speech Recognition**: Feature provided under this category are -

    * Einstein Voice(open beta)
    
## Einstein AI Services

Services provided by Einstein AI

* **Einstein Bots**: Einstein Bots use Natural Language Processing (NLP) to 
  provide instant help for customers by answering common questions or gathering
  the right information to hand-off the conversation seamlessly to the right 
  agent for more complex questions or cases. 
  
  Example: Chat Bot

* **Einstein Voice**: Einstein Voice enables all users to talk to Salesforce from
  any device. Einstein Voice is broken down into two buckets: 
  
  * Einstein Voice Assistant: This enables anyone to update Salesforce conversationally.
    
    Example: Verbally logging meeting notes to Salesforce. Einstein intelligently 
    predicts what information to log and what records to associate it with, what
    changes to make, and what follow-ups to assign. Another example is to get 
    Salesforce daily briefing read to him. 
  
  * Einstein Voice Bots: It enables customers to speak into their voice assistants 
    and get the answers and updates they’re looking for in real time.
  
* **Einstein Prediction Builder**: Einstein Prediction Builder is a simple 
    point-click wizard that allows one to make custom predictions on your 
    non-encrypted Salesforce data, fast. It can apply -
    
  * Binary Classification: When user wants to predict the answer to a Yes 
    or No question.
  * Regression(in Beta): When user wants to predict an amount.  

* **Einstein Next Best Action (NBA)**: Einstein NBA allows one to use rules-based
    and predictive models to provide anyone in one's business with intelligent, 
    contextual recommendations and offers. With NAB, one create rules, or 
    propositions, based off of predictions and outcomes, to provide the best 
    recommendation.   

* **Einstein Discovery**: It analyses patterns in data and provides full 
    understanding of relevant patterns. This can be used to make predictions 
    which are relevant to end customers. 

* **Einstein Vision**: Einstein Vision and Language are a set of 
    APIs and services for developers to use to add deep-learning capabilities 
    to any application, ultimately allowing end users to classify images and 
    extract meaning from text.
    
    Einstein Vision consists of:
    
    * Einstein Object Detection: Extraction and contextualization of objects 
      in images. 
    * Einstein Image Classification: Image Classification.

* **Einstein Language**: It enables ens user build natural language processing 
    into your apps to classify the underlying intent and sentiment in a body of
    text. Einstein Language consists of Einstein Sentiment and Einstein Intent.
    Together, these APIs harness and make sense out of unstructured data from 
    text to help better understand your customers.
    
    * Einstein Intent: The Einstein Intent API categorizes unstructured text 
    into user-defined labels to better understand what users are trying to 
    accomplish.
    * Einstein Sentiment: The Einstein Sentiment API classifies text into 
    positive, negative, and neutral classes to understand what the words people 
    use can tell us about how they’re feeling.      

## How To Use Einstein Language 

These steps explain how to use Einstein Language API. [Einstein Platform Services](https://metamind.readme.io/)
allows one to seamlessly integrate custom deep learning models into workflows.

### Setting Up Environment

#### Download Key

An account needs to be created at this [link](https://api.einstein.ai/signup) 
to access Einstein Platform Services APIs. Once account is created, a private 
key is required to download. The key file is named einstein_platform.pem

#### Generate a Token  

To generate token, navigate to [link](https://api.einstein.ai/token) and 
provide account id or mail id along with private key.Browse and navigate 
to the einstein_platform.pem file downloaded during account signup. Click 
Get Token, and save the token in a text file or somewhere you can access it.

#### Create Dataset

The Einstein Language APIs support data in these file formats:

* .csv (comma-separated values)
* .tsv (tab-separated values)
* .json

A sample CSV file is provided by Salesforce at [link](http://einstein.ai/text/case_routing_intent.csv).
The data in this .csv file takes this format: 
"intent string",label. Examples from dataset in shown in @fig:csv-sample.

![CSV Sample Data Set Example [@sp20-516-224-json-api-dataset-response]](images/csv-data-set.jpg){#fig:csv-sample}

To create dataset out of input csv file, enter this cURL command, replacing 
`<TOKEN>` with the token which is generated.

* Create dataset from provided sample.(Asynchronous Call)

    ```bash
    $ curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" 
                   -H "Content-Type: multipart/form-data" -F "type=text-intent" 
                   -F "path=http://einstein.ai/text/case_routing_intent.csv" 
                       https://api.einstein.ai/v2/language/datasets/upload
    ```

* Create dataset from a local file.(Synchronous Call)

    ```bash
    $ curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" 
                   -H "Content-Type: multipart/form-data" -F "type=text-intent" 
                   -F "data=@C:\Data\weather.csv" 
                       https://api.einstein.ai/v2/language/datasets/upload
    ```

JSON Request Parameters for Create Dataset API:

Table: Create Dataset Request Body [@sp20-516-224-create-dataset-response]

    Name                Type                    Description
    ------------------- ----------------------- -------------------------------
    data                string                  Path to the .csv, .tsv, or .json 
                                                file on the local drive (FilePart). 
                                                The maximum file size you can 
                                                upload from a local drive is 25 MB.
    language            string                  Dataset language. Optional. Default 
                                                is en_US. Reserved for future use.
    name                string                  Name of the dataset. Optional. If 
                                                this parameter is omitted, the 
                                                dataset name is derived from the 
                                                file name.
    path                string                  URL of the .csv, .tsv, or .json file. 
                                                The maximum file size you can upload 
                                                from a web location is 25 MB.
    type                string                  Type of dataset data. Valid values are:
                                                    * text-intent
                                                    * text-sentiment


This curl command makes call to Einstein Intent API and creates dataset. The 
response from the API looks something like this JSON shown in @Fig:json-dataset.

![JSON Response [@sp20-516-224-json-api-dataset-response]](images/json-dataset.png){#fig:json-dataset}

The API call is asynchronous, so we receive a **dataset ID** back immediately but 
the available value is false and the statusMsg value is UPLOADING. Use the **dataset 
ID** and make a call to **Get a Dataset** to query when the upload is complete. When 
available is true and statusMsg is SUCCEEDED, the data upload is complete, and 
we can train the dataset to create a model.

JSON Response body for Create Dataset API:

Table: Create Dataset Response Body [@sp20-516-224-create-dataset-response]

    Name                Type                    Description
    ------------------- ----------------------- -------------------------------
    available           boolean                 Specifies whether the dataset 
                                                is ready to be trained.
    createdAt           date                    Date and time that the dataset 
                                                was created.
    id                  long                    Dataset ID.
    labelSummary        object                  Contains the labels array that 
                                                contains all the labels for the 
                                                dataset. This is an asynchronous 
                                                call, so the labels array is empty 
                                                when you first create a dataset.
    language            string                  Dataset language. Default is en_US.
    name                string                  Name of the dataset. The API uses 
                                                the name of the file for the dataset 
                                                name.
    numOfDuplicates     int                     Number of duplicate text strings 
                                                in the .zip file from which the 
                                                dataset was created.
    object              string                  Object returned; in this case, 
                                                dataset.
    statusMsg           string                  Status of the dataset creation 
                                                and data upload. Valid values are:
                                                    * FAILED: Data upload 
                                                      has failed.
                                                    * SUCCEEDED: Data upload is 
                                                      complete.
                                                    * UPLOADING: Data upload is 
                                                      in progress.
    totalExamples       int                     Total number of examples in the 
                                                dataset.    
    type                string                  Type of dataset data. Valid values are:
                                                    * text-intent
                                                    * text-sentiment
    updatedAt           date                    Date and time that the dataset was 
                                                last updated.                                                                       

#### Get the Dataset Status

The call made to create the dataset is asynchronous. This means that the API 
returns a response with the dataset ID right away. But in the background, it 
could still be loading data. This is especially true if we have a large dataset. 

The **available** field in response tells us whether we can use the dataset or 
not. Calls that reference the dataset succeed only when available is true.

The **statusMsg** field gives us more information about what’s happening with the 
dataset. A value of UPLOADING means that the API is uploading the data from the 
.csv file. If statusMsg is QUEUED, it means that the API hasn’t started 
uploading the data yet, but the request is in line.        

To make a call to get the status of dataset, execute curl command:

```bash
$ curl -X GET -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" 
                https://api.einstein.ai/v2/language/datasets/<DATASET_ID>
```                                       

In this curl command, replace `<TOKEN>` with the token and `<DATASET_ID>` with the 
dataset ID. Then run the command in the command line window.

In the response when **available** is true and **statusMsg** is SUCCEEDED, then
the dataset is ready for training. When statusMsg is SUCCEEDED, we can proceed 
to training.

JSON Response body:

Table: Dataset Status Response Body [@sp20-516-224-create-dataset-response]

    Name                Type                    Description
    ------------------- ----------------------- -------------------------------
    available           boolean                 Specifies whether the dataset 
                                                is ready to be trained.
    createdAt           date                    Date and time that the dataset 
                                                was created.
    id                  long                    Dataset ID.
    labelSummary        object                  Contains the labels array that 
                                                contains all the labels for the 
                                                dataset. This is an asynchronous 
                                                call, so the labels array is empty 
                                                when you first create a dataset.
    language            string                  Dataset language. Default is en_US.
    name                string                  Name of the dataset. The API uses 
                                                the name of the file for the dataset 
                                                name.
    numOfDuplicates     int                     Number of duplicate text strings 
                                                in the .zip file from which the 
                                                dataset was created.
    object              string                  Object returned; in this case, 
                                                dataset.
    statusMsg           string                  Status of the dataset creation 
                                                and data upload. Valid values are:
                                                    * DELETION_PENDING—Dataset is 
                                                      in the process of being 
                                                      deleted.
                                                    * FAILED: <message>—Data upload 
                                                      has failed.
                                                    * SUCCEEDED: Data upload is 
                                                      complete.
                                                    * UPLOADING: Data upload is 
                                                      in progress.
    totalExamples       int                     Total number of examples in the 
                                                dataset.    
    totalLabels         int                     Total number of labels in the dataset.  
    type                string                  Type of dataset data. Valid values are:
                                                    * text-intent
                                                    * text-sentiment
    updatedAt           date                    Date and time that the dataset was 
                                                last updated.
                                                
#### Train the Dataset and Create a Model                                                

Curl command to train dataset is:
 
 ```bash
$ curl -X POST -H "Authorization: Bearer <TOKEN>" 
               -H "Cache-Control: no-cache" 
               -H "Content-Type: multipart/form-data" 
               -F "name=Service Request Routing Model" 
               -F "datasetId=<DATASET_ID>" 
                https://api.einstein.ai/v2/language/train
```        

Replace `<TOKEN>` with generated token ID and `<DATASET_ID>` with the dataset id
generated in dataset creating step.   

Request Parameters For Training API:

Table: Training Request Body [@sp20-516-224-create-dataset-response]

    Name                Type                    Description
    ------------------- ----------------------- -------------------------------
    datasetId           long                    ID of the dataset to train. 
    epochs              int                     Number of training iterations 
                                                for the neural network. Optional. 
                                                If not specified, the default 
                                                is calculated based on the dataset 
                                                size. The larger the number, the 
                                                longer the training takes to 
                                                complete.

                                                The training process stops before 
                                                the specified number of epochs if 
                                                the model has reached the optimal 
                                                accuracy. When you get the training 
                                                staus, the earlyStopping field 
                                                specifies whether the training 
                                                stopped 
                                                early, and the lastEpochDone value 
                                                specifies the last training 
                                                iteration.
    learningRate        float             	    N/A for intent or sentiment models.
    name                string                  Name of the model. Maximum length
                                                is 180 characters.
    trainParams         string                  JSON that contains parameters that 
                                                specify how the model is created. 
                                                Optional. Valid values:

                                                * {"trainSplitRatio": 0.n}—Lets you 
                                                specify the ratio of data used to 
                                                train the dataset and the data used 
                                                to test the model. The default split 
                                                ratio is 0.8; 80% of the data is 
                                                used to train the dataset and create 
                                                the model and 20% of the data is 
                                                used to test the model. If you pass 
                                                in a split ratio of 0.6, then 60% 
                                                of the data is used to train the 
                                                dataset and create the model and 40% 
                                                of the data is used to test the 
                                                model.

                                                * {"withFeedback": true}—Lets you 
                                                specify that feedback examples are 
                                                included in the data to be trained 
                                                to create the model. If you omit this 
                                                parameter, feedback examples aren't 
                                                used in training.

                                                * {"withGlobalDatasetId": <DATASET_ID>}—
                                                Lets you specify that a global dataset 
                                                is used in addition to the specified 
                                                dataset to create the model.

Name                Type                    Description
------------------- ----------------------- -------------------------------
datasetId           long                    ID of the dataset to train. 
epochs              int                     Number of training iterations 
                                            for the neural network. Optional. 
                                            If not specified, the default 
                                            is calculated based on the dataset 
                                            size. The larger the number, the 
                                            longer the training takes to 
                                            complete.
                                            The training process stops before 
                                            the specified number of epochs if 
                                            the model has reached the optimal 
                                            accuracy. When you get the training 
                                            staus, the earlyStopping field 
                                            specifies whether the training 
                                            stopped 
                                            early, and the lastEpochDone value 
                                            specifies the last training 
                                            iteration.
learningRate        float             	    N/A for intent or sentiment models.
name                string                  Name of the model. Maximum length
                                            is 180 characters.
trainParams         string                  JSON that contains parameters that 
                                            specify how the model is created. 
                                            Optional. Valid values:
                                            * {"trainSplitRatio": 0.n}—Lets you 
                                            specify the ratio of data used to 
                                            train the dataset and the data used 
                                            to test the model. The default split 
                                            ratio is 0.8; 80% of the data is 
                                            used to train the dataset and create 
                                            the model and 20% of the data is 
                                            used to test the model. If you pass 
                                            in a split ratio of 0.6, then 60% 
                                            of the data is used to train the 
                                            dataset and create the model and 40% 
                                            of the data is used to test the 
                                            model.
                                            * {"withFeedback": true}—Lets you 
                                            specify that feedback examples are 
                                            included in the data to be trained 
                                            to create the model. If you omit this 
                                            parameter, feedback examples aren't 
                                            used in training.
                                            * {"withGlobalDatasetId": `<DATASET_ID>`}—
                                            Lets you specify that a global dataset 
                                            is used in addition to the specified 
                                            dataset to create the model.

The API response looks similar to shown in @fig:json-training.

![JSON Training API Response [@sp20-516-224-json-api-training-response]](images/json-training.png){#fig:json-training}

The important fields to note are **status** and **modelId**. The status field 
value is QUEUED, and that tells us that the training process hasn’t started. 
The queuePosition field tells us the queue position. The modelId field 
contains the ID of the model. Make a note of the modelId, because we use this 
ID any time to refer to the model in your code.

Response Parameters For Training API:

Table: Training Response Body [@sp20-516-224-create-dataset-response]

    Name                Type                    Description
    ------------------- ----------------------- -------------------------------
    algorithm           string                  Algorithm used to create the 
                                                model. Returned only when the 
                                                modelType is text-intent. 
                                                Default is intent. 
    createdAt           date                    Date and time that the model 
                                                was created.
    datasetId           long             	    ID of the dataset trained to 
                                                create the model.
    datasetVersionId    int                     N/A
    epochs              int                     Number of epochs used during 
                                                training.
    language            string                  Model language inherited from 
                                                the dataset language.
    learningRate        float                   N/A for intent or sentiment models.
    modelId             string                  ID of the model. Contains letters 
                                                and numbers.
    modelType           string                  Type of data from which the model 
                                                was created. Inferred from the 
                                                dataset type. Valid values are:
                                                    * text-intent
                                                    * text-sentiment
    name                string                  Name of the model.
    object              string                  Object returned; in this case, 
                                                training.
    progress            float                   How far the training job has 
                                                progressed. Values are between 0–1.
    queuePosition       int                     Where the training job is in the 
                                                queue. This field appears in the 
                                                response only if the status is 
                                                QUEUED.
    status              string                  Status of the training job. 
                                                Valid values are:

                                                   * QUEUED—The training job is 
                                                     in the queue.
                                                   * RUNNING—The training job is 
                                                     running.
                                                   * SUCCEEDED—The training job 
                                                     succeeded, and the model was 
                                                     created.
                                                   * FAILED—The training job failed.
    trainParams         object                  Training parameters passed into 
                                                the request. For example, if you 
                                                sent in a split of 0.7, the response 
                                                contains 
                                                "trainParams": {"trainSplitRatio": 0.7}
    trainStats          object                  Returns null when you train a dataset. 
                                                Training statistics are returned when 
                                                the status is SUCCEEDED or FAILED.
    updatedAt           date                    Date and time that the model was 
                                                last updated.
    

The **trainStats** object contains information about how long various tasks in the 
training process took. This can be helpful information to gauge the training 
times based on the amount of data you have.

Another interesting field is the **epochs** field. When we train a dataset with 
the command we used, the API selects a default number of epochs based on the 
amount of data in the dataset. However, we can pass in the number of epochs you 
want the training process to use.

In our dataset, the API chose 1,000 epochs or training iterations. But the 
earlyStopping field reports that the training stopped before it completed 
the 1,000 epochs. And the lastEpochDone field reports that the training 
stopped after 49 epochs.

Why did it stop before completing 1,000 epochs? During the training process, 
if the API determines that further training won’t improve the model accuracy, 
it stops the training early. This is just one way that the API handles a lot 
of the details for us.                

#### Use the Model to Make a Prediction

Now we have created the dataset, trained the dataset to create a model, and 
at last we’re ready to test it out. we test the model by sending some text 
into the model and getting a response back.

Curl command to test model is:

```bash
$ curl -X POST -H "Authorization: Bearer <TOKEN>" 
               -H "Cache-Control: no-cache" 
               -H "Content-Type: multipart/form-data" 
               -F "modelId=<MODEL_ID>" 
               -F "document=I'd like to buy some shoes" 
                https://api.einstein.ai/v2/language/intent
```

In the request, the document parameter contains the string you want to classify.
We expect model to put a label on this text.

Request Parameter for Prediction API:

Table: Prediction Request Body [@sp20-516-224-create-dataset-response]

    Name                Type                    Description
    ------------------- ----------------------- -------------------------------
    document            string                  Text for which you want to return 
                                                an intent prediction.
    modelId             string                  ID of the model that makes the 
                                                prediction. The model must have 
                                                been created from a dataset with 
                                                a type of text-intent.
    numResults          int             	    Number of probabilities to return. 
                                                Optional. If passed, must be a 
                                                number greater than zero.

                                                The response is sorted by probability 
                                                in descending order. For example, 
                                                if you pass in 3, only the top three 
                                                label and probability values are 
                                                returned.
    sampleId            string                  String that you can pass in to 
                                                tag the prediction. Optional. 
                                                Can be any value, and is returned 
                                                in the response.

The API response looks similar to shown in @fig:json-prediction.

![JSON Prediction API Response [@sp20-516-224-json-api-prediction-response]](images/json-prediction.png){#fig:json-prediction} 

The model predicts that the request is a sales opportunity.

#### Interpret the Results

From the prediction response, we can see how the labels come into play when we 
make a prediction. The model takes the input text and classifies it based on 
the data associated with each label. In the response, the label value Sales 
Opportunity has a probability value of 0.9540156. In this case, the model is 
95% sure the request is a sales opportunity.                              

### Cost

#### Einstein Analytics Pricing

There are 3 products available under Einstein Analytics[@sp20-516-224-cost-analytics].

* **Einstein Predictions** - Cost $75 /user/month.
* **Einstein Analytics Growth** - Cost $125 /user/month.
* **Einstein Analytics Plus** - Cost $150 /user/month.

Comparison of these 3 products and their top features is provided in @fig:cost-compare-analytics.

![Compare Edition and Top Feature [@sp20-516-224-cost-analytics]](images/cost-compare-analytics.png){#fig:cost-compare-analytics}

#### Einstein Vision and Language through Heroku

Plans & Pricing[@sp20-516-224-cost-heroku]:

* **Starter** - Free. 1000/month Prediction API calls.
* **Bronze** - $40/month. 10000/month Prediction API calls.
* **Silver** - $850/month. 250,000/month Prediction API calls.
* **Gold** - $3400/month. 1,000,000/month Prediction API calls.

References:

* <https://trailhead.salesforce.com/content/learn/modules/einstein_intent_basics>
* <https://metamind.readme.io/docs/prediction-intent> 
* <https://www.salesforce.com/products/einstein-analytics/pricing/>
* <https://elements.heroku.com/addons/einstein-vision>
