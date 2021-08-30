# VIDEO_TO_SUMMARIZED_TEXT


## Team members
- [Kushal Shah](https://github.com/Kushal-Ajay-Shah)
- [Anupam Laddha](https://github.com/Anupamladdha)
- [Azeez](https://github.com/azeez-72)

## Table of Contents

* [About the Project](#about-the-project)
  * [Description](#description)
  * [Presentation](#presentation)
  * [Visuals](#visuals)
  * [Modules used in the project](#modules-used-in-the-project)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Sample Input and Output](#sample-input-and-output)





## About The Project

### Description

    Our Project is based on an original idea which we thought of that would automate things in our life. 

    The idea behind this project was to automate video to summarized text conversion.

    In this project first: 

        1)We take a youtube link as an input from the user.
        2)Also we take the number of sentences in summarized text as an input from the user.
        3)Then it is converted into a audio file.
        4)Convert the audio file to text file.
        5)Punctuate the text.
        6)Summarize the punctuated text.
        7)Display the output in GUI.
      
### Presentation 
[Project Overview](https://docs.google.com/presentation/d/1ZXrcSNWf0AMQt-cr2gYh-kJHyNturibQR8BC6oQkLDc/edit#slide=id.gb0f88be3ed_4_5)

### Visuals
<img src="https://github.com/Anupamladdha/VIDEO_TO_SUMMARIZED_TEXT/blob/main/Screenshots/Output1.png" height = 450/> 


### Modules used in the project

    For downloading youtube video:
        youtube-dl

    For video to text conversion:
        Speech_recognition
        Moviepy.editor

    For text summarization:
        Nltk
        Numpy
        Networkx

    For GUI:
        Tkinter

    **Also we have added requirements.txt file to install modules used for the project.**

    For installing nltk you can refer to (https://www.youtube.com/watch?v=Qu8pob9RX64) 
    
## Getting Started
    
### Installation
* Clone the repo
```bash
git clone https://github.com/Anupamladdha/VIDEO_TO_SUMMARIZED_TEXT.git
```
* Create a virtual environment and install all dependencies from the requirements.txt file
```bash
$ virtualenve your_env
$ source your_env/bin/activate
$ pip install -r requirements.txt
```

### Sample Input and Output:

    Enter youtube link:
    https://www.youtube.com/watch?v=AshTPy3pa5I

    Enter the number of sentences in summarized text:
    7

    Non summarized punctuated text:
    World good morning to the respected principal teachers, parents and my dear friends today, I am here to share my opinion about social media. Social media is an online platform where we can share their thoughts, information, pictures and videos. We all use it in our day to day life. It has become an integral part of our lives. There are various social media platforms like Facebook, Twitter, WhatsApp, accept all use them to communicate and socialize locally, as well as Global social media has both advantages and disadvantages. I would like to mention advantages of social media. First, the biggest benefit of social media is that we can share of a thoughts and ideas with people across the world. Now even a common man can express his opinion on any national or International issue. Another benefit of social media is that people can showcase their talent. On this platform. Many people have gained Fame by showing that Ireland, through social media, it is also helping people to earn money. People sell a lot of things like clothes works, electronic items, except through social media. Social media is also used to create awareness amongst people. People with good knowledge about topics like health or nutrition use this platform to create awareness amongst people. Now I would like to talk about the drawbacks of social media. Addiction is the biggest drawback of social media. People have got used to of checking the social media accounts every now, and then they spend a lot of time in checking various post on social media spending. A lot of time on social media also brings a lot of health disorders like stress, anxiety and sleeplessness. Another drawback of social media is that we cannot trust all the information available here. Some information can be true, while some can be fake at times false news spread like Wildfire. Through this platform, our personal information becomes easily available too many on the net. Hence we need to stay a lot from hackers. Apart from this, cyber bullying is another major drawback of social media. Some people, personality and Heath comments on others, accounts and harass them. Social media has both advantages and disadvantages. The advantage, like socializing, has made our life simpler and convenient. There are some disadvantages to. We need to use this platform wisely and in a limited way, so that we can make the most out of this new platform. With this, I and my speech, thank you. Everyone have a wonderful day. 

    Summarized text:
    Social media has both advantages and disadvantages. There are various social media platforms like Facebook, Twitter, WhatsApp, accept all use them to communicate and socialize locally, as well as Global social media has both advantages and disadvantages. People have got used to of checking the social media accounts every now, and then they spend a lot of time in checking various post on social media spending. I would like to mention advantages of social media. Now I would like to talk about the drawbacks of social media. Another benefit of social media is that people can showcase their talent. Social media is also used to create awareness amongst people.

