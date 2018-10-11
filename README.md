# **TweetDB**
## Problem Statement
Use Twitter Search/Streaming API to fetch are store the target tweets with metadata
(eg: user details, tweet time, favorites and retweet counts etc ) for a recent high traffic event
and create a MVP.

## Solution
APIs that have been designed to create an MVP -

1. **API1(/api1)** - This API triggers twitter streaming and stores a curated version of the data returned by Twitter Streaming API. Supports both GET and POST methods. Sample url - 
```
http://127.0.0.1:5000/api1?keywords=modi,Brexit,Trump
```
Successful response will yield result - 
```
{
	  "message": "Stream started with ['modi', 'Brexit', 'Trump']",
	  "status": "success"
}
```
2. **API2(/api2)** - API2 is used to return stored tweets and their metadata based on applied filters/search.
It applies filter to data stored in NoSql Database and shows the formatted result. Sample url - 
```
http://127.0.0.1:5000/api2?start=0&end=10&uname=.*Alm.*&lang=en&twtext=buy
``` 
Successful response will yield result - 
```
[
  {
    "_id": {
      "$oid": "5bbf7ce6347fe912db983ff9"
    },
    "Name": "AlmBardy",
    "Username": "Gina Alm Bardy",
    "Location": "Palm Bay, FL",
    "SourceDevice": "Twitter for iPhone",
    "Retweets": false,
    "Country": "",
    "CountryCode": "",
    "TweetText": "RT @CREWcrew: “They buy apartments from me. They spend $40 million, $50 million. Am I supposed to dislike them?” - @realDonaldTrump on the…",
    "FavouriteCount": 0,
    "Timestamp": "2018-10-11",
    "CreatedAt": {
      "$date": 1539276006000
    },
    "ReplyCount": 0,
    "Language": "en",
    "HashTags": []
  }
]
```
There are various parameters that you can pass to filter your query. Have a look to some of the
parameters.

```
url = "http://127.0.0.1:5000/api2?param1=xxxx&param2=yyyy"
     where xxxx,yyyy = args

Params - 

1. favct - Filters FavouriteCount 
	  format - l10 , e2, g6 where l = less than or equal to, g = greater than or equal to, e = equal to

2. rtct - Filters ReplyCounts
	 format - l10 , e2, g6 where l = less than or equal to, g = greater than or equal to, e = equal to

3. lang - Specifies Language type 
	 format - Value must be in ISO639-2 encoded form eg: for Hindi it will be 'hi', English='en', German='de' etc.

4. start - Specifies starting index for pagination.
	   ormat - 10, 5 ,6 or any integer value

5. end - Specifies closing index for pagination
	 format - 10, 5 ,6 or any integer value
	 Note - end value must be greater than start value

6. twtext - Specifies searching filter for Tweet Text
	  format - a) hello - If you are sure about the complete word ie hello
		    b) ^hello - If the word starts with hello and ends with different characters eg- helloabc
		    c) hello$ - If the word ends with hello but starts with different character eg- abchello
		    d) .*hello.* - If the word contains hello but has different starting and ending characters 
			            eg- xyzhelloabc

7. uname - Specifies searching filter for Username
	   format - same as of twtext

8. sname - Specifies searching filter for Screen Name
	   format - same as of twtext
       
9. sort - Provides sorting mechanism on basis of argument
	  format - If you want to sort by Timestamp pass 'date'. Similarly for FavouriteCount use 'favct', 'rtct' for 
		   ReplyCounts. Can provide a single argument at a time.

10. date - Filters on basis of Date time
	  format -  yyyy-mm-dd eg: 2018-07-13 etc.
      
It is mandatory for user to pass start and end paramters. Rest all can be passed depending upon filter.
```
3. **API3(/api3)** - It is used to export filtered data as CSV with selected columns of my choice.
Sample url - 
```
http://127.0.0.1:5000/api3
```
Successful response will yield - 
```
{
    "Message": "Success",
    "Result": "CSV file is present in folder with name script.csv"
}
```

## Tools and Framework used - 
- Python-Flask
- Twitter Streamin API
- MongoDB

## Setup and Run Project - 
- Git clone the following repo
- Make sure you have Python and MongoDB installed in your local machine
- Install the requirements
		pip install -r requirements.txt
- Run the server file
		python3 server.py