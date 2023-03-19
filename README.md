# group_2_final_project

## Data:

Our dataset consists of 1.6 million tweets

source: 

https://www.kaggle.com/code/tamoghna96saha/sentiment-analysis-using-transfer-learning-1


## Purpose:

To get the sentiments of people's tweets as positive or negative, the parts of speech breakdown for each of the tweets, and to extract the subject from the tweet so that users can be suggested to one another for following based on the sentiment value and subject. 

## Dataset description
The dataset has 6 columns:
- target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
- ids: The id of the tweet 
- date: the date of the tweet 
- flag: The query (lyx). If there is no query, then this value is NO_QUERY.
- user: the user that tweeted.
- text: the text of the tweet.

## ETL Process:
<b>Extraction:

- Loaded dataset using pandas

<b>Cleaning:

- Removed stopwords

- Removed @user_name

- Focused on alphabets

- Lemmatized words
	

After the cleaning process the files to be uplaoded to the database will be stored in the path group_2_final\Resources\final_clean_twitter.zip

<b>Transformation(Word embeddings):

- Represent each word as a vector of numbers

- The closer related the words are the more similar the meaning

- 2B tweets, 27B tokens, 1.2M vocab

- 50 dimensions

https://nlp.stanford.edu/projects/glove/

Below is a picture of the word embeddings:

![Word Embedding](images/word_embedding.jpg)
	

Below is the ERD that is used for our tweets database:
![QuickDBD-Free Diagram (5)](https://user-images.githubusercontent.com/94792982/205812766-97767ff0-9583-4397-84e9-83a5cb16e65f.png)



	



## Machine Learning Model:

- Model was trained on a 70/30 train/test split

- The training set was further divided into training/validation set

- Training set (~896,000 tweets)

- Validation set (~224,000 tweets)

- Testing set (~480,000 tweets)

- Max length of words to consider per tweet was set to 500


Below is a picture showing the details of the model:

![ML_model](images/ML_model.jpg)

## Results and Analysis

<b>Final accuracy: 0.7494	 

<b>Validation accuracy: 0.7403 

<b>Precision: 0.7357848    

<b>Recall: 0.754179497

![ML_model](images/model_acc.jpg)	![ML_model](images/model_loss.jpg)

The model predicted more <b>false_positives than <b>false_negatives

- Below is a picture of the confusion matrix:

![Confusion matrix](images/conf_mat.png)


## Django Web Framework 

Django was used to deploy the machine learning model. This application is comprised of PostgreSQL for the database, TensorFlow for the machine learning model, Spacy for the parts of speech breakdown, Wordnet for computational liguistics, the NewsAPI for the api and the pyttsx library for the AI chatbot. 

The system works by taking a tweet, breaking the tweet down by parts of speech, getting the sentiment and subject from the tweet which is done by running through a series of functions and the ML model. This data is then called, via a get request, and returns the latest tweet and the revelant data assocaited with this tweet. Based on the subject, it then is sent to the NewsApi and returns topics relevant to the subject. This is synonmous to target marketing. To add, the data is then used to query the database for like users based on sentiment and subject so that other users are suggested to follow each other. This can be used to group like users. When there is no subject, the computational linguistics steps in to control the process. Based on the sentiment and the words in the tweet, the APi is then queried based on how the liguistics suggest based on the subject and sentiment. 
	
Figure 1-- The image below is the page to enter the tweet to be analyzed



![2022-12-05 (17)](https://user-images.githubusercontent.com/94792982/205812601-cf0bc4b3-0a2e-4da0-95ea-07bb0b33d50f.png)

Figure 2-- The image below is the page that analyzes the tweet
![ANALYTICS_PJT](https://user-images.githubusercontent.com/94792982/205812625-0f8997b7-420d-492a-931d-542d5da70972.png)
Figure 3-- The image below is the page the API returns data based on subject of the tweet	
![API_DATA_PJT](https://user-images.githubusercontent.com/94792982/205812645-6f5c0573-89d0-4494-9bf1-2b0b6a20e3be.png)
Figure 4-- The image below is the page that the followers are suggested	
![SUGGESTER_PJT](https://user-images.githubusercontent.com/94792982/205812664-219807d4-16e5-49b0-be59-1a9c9c31bfa7.png)

	
