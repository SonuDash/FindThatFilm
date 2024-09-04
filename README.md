# FindThatFilm
Imagine you are with your crush sitting on a park bench and having a deep conversation about modern cinema, their plots and philosophies. This is your chance to impress them, this is your chance to shine, you remember the plot of a perfect cinema, you speak out the entire plot, the philosophy behind it, even the artists! **BUT** you forgot the movie name!!! Your braincells are firing every nook and corner of your memory cortex just to get the name, you close your eyes with force to focus and remember but the incomplete information from your brain is not enough, you are not abe to connect dots, inside of your brain there's a war going on. You are anxious, "No way this can happen!". At this time the voice from the person sittng next to you reaches you ears, "Great evening with you, I've to catch next train to Panwel, I'll get late. Good Bye :)"

You have f***ed up the date.


![image](https://github.com/user-attachments/assets/2c0bf0c0-dbcc-4da9-abe8-4f0d5d872f2c)

Now you don't have to worry about it, presenting **Find that Film**, now you can just enter the keywords for the movie in the generous search box and get a list of all the related movies. Be it a date, a family get together, first day at a corporate sprint meeting (I hate 'em) or just random mind mapping, **Find that Film** got your back.


## Problem Statement
The intro to the application pretty much explains the problem statement. It's basically the problem that, cinema industry is ever-expanding, especially in an era where Indian-Film-Industry alone churns out 100s of movies every year, it's very hard to keep a track of all the name by the viewers, however some movies and their plots stand out to the viewers but there is no effective tool in the market which gives users their required information just from the movie descriptions.

## Proposed Solution
The proposed solution is to build an application which will provide number of movie options to uers whose plot and setting matches their custom description that they provided in the searchbox.

![image](https://github.com/user-attachments/assets/51772752-62b7-41f0-9604-6cedbf4c0fb2)
The demo of **Find that Film**

## Pre-Requisites:
1. Python
2. MongoDB account
3. a free shared cluster in MongoDB Atlas
4. Some basic front-end

### With these in place let's begin the process

## Procedure:
1. **Chose a code editor of your choice**: Chose VSCode probably, unless you are the gigachad of computer programming and use NeoVim or the God-tier Notepad++
2. **List out and install the requirements**: this contains all the packages you require for this project: [https://github.com/SonuDash/FindThatFilm/blob/main/requirements.txt]
3. Replace the hf_token with a **hugging face access token** [https://huggingface.co/docs/hub/en/security-tokens]
4. Replace the URI with the **MongoDB connection** string [https://www.mongodb.com/docs/guides/atlas/connection-string/]
5. Create a vector Search Index, let me paste my vector search index json data:
```
{
  "fields": [
    {
      "numDimensions": 384,
      "path": "plot_embedding_hf",
      "similarity": "dotProduct",
      "type": "vector"
    }
  ]
}
```

6. Make the flask app [https://github.com/SonuDash/FindThatFilm/blob/main/app.py]
7. Save everything and run the program with
```
python app.py //if in windows
python3 app.py //for mac
```
8. If you have set everything properly you will be able to see the app running on `localhost:2408`
(2408 because that was the date for NammaMUG event in Bengaluru (24/08/24) and it's from there I got the idea and the hands on experience to mke this)

## Problems that I faced:
I faced some issues while making it.
1. Setting up of the cluster, I suggest you check out the official MongoDB docs on how to set up a free-tier cluster for person usage.
2. Setting up the search index: In Mongo, it's easier for people to mistake **Atlas Search** for **Atlas Vector Search** or vice versa, the requirement here is an **Atlas Vector Search Index**
3. Set all the db names correctly, One issue that I faced was I was trying to access the **'movies'** db from **'sample_mflix'** collections but I typed the db name incorrectly. Remember to put the same db name on which you are creating vector embedings on. AND ALL SET!!

## Conclusion and Inspiration:
This is a small used case of the large data that is avaliable publicly right now thanks to MongoDB's sample dataset. I am envisioning to play with some more such datasets and cater to some more used cases, for example collections like **'sample_weatherdata'** can help us make predictive decision about weather. 

The inspiration for this project came from NammaMUG (Mongo User's Group) event on 24th of August at WeWork Bengaluru, it was a great platform to connect with fellow techies and gain valuable insights. One of the organisers helped me to implement this code and fix the bugs.

Untill next time. `Goodbye!!`
