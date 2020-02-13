# AI Services at Salesforce sp20-516-224, Mishra, Divyanshu

make sure you comment on cost. DO they have any free services?

## Einstein AI Overview

Salesforce offers AI services platform which can help organizations build AI 
powered apps quickly for employees and customers.  

Products are grouped under four basic AI Domains.

* **Machine Learning**: Products provided under this category are -
    
    * Einstein Discovery
    * Einstein Prediction Builder
    * Einstein Next Best Action

* **Natural Language Processing**: Products provided under this category are -

    * Einstein Language
    * Einstein Bots    

* **Computer Vision**: Products provided under this category are -

    * Einstein Vision
    
* **Automatic Speech Recognition**: Products provided under this category are -

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

## Costs (Any free services??)


## How To Use Einstein Language 


### Setting Up Environment

#### Download Key

An account needs to be created at this [link] (https://api.einstein.ai/signup) 
to access Einstein Platform Services APIs. Once account is created, a private 
key is required to download. The key file is named einstein_platform.pem

#### Generate a Token  

To generate token, navigate to [link] (https://api.einstein.ai/token) and 
provide account id or mail id along with private key.Browse and navigate 
to the einstein_platform.pem file downloaded during account signup. Click 
Get Token, and save the token in a text file or somewhere you can access it.

#### Create Dataset

The Einstein Language APIs support data in these file formats:

* .csv (comma-separated values)
* .tsv (tab-separated values)
* .json

The data in the .csv file takes this format: "intent string",label. Examples
are:

Intent String                                       Label
"need to reset my password",                        Password Help
"when will my order arrive?",                       Shipping Info
"can I buy another pair, these are great?",         Sales Opportunity