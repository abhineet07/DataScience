This project is based perfroms sentiment analysis on data collected from multiple websites about multiple brand phones
Data collected : 
	- Comment title
	- User's comment
	- Ratings
	- Date
	- Pros
	- Cons

In this project we collect data from various websites using webcrawling. Websites
	- amazon
	- flipkart
	- indiatoday
	- phonecurry
	- gadgets360
	- mobile91


The users comment from the data collected then processed. 
Important points from the comment are extracted based on features.
Then the polarity of the those points are determined (positive or negative)
	- eg. camera is not good -> negative
	- eg. display is awesome -> positive
(for this collections of positive, negative and features are created 
and inserted in trie data structure for faster search and reduce ambiguity)

Then we analyse based on the polarity data, whether the phone is positively or negatively based on a certain feature recieved by the users.
'Textblob' is also used to give the polarilty score to the one complete comment of user.

User interface is provided for user to get the data of a particular phone of his choice from Internet and perform feature wise analysis.
'tkinter' is used for making GUI.

----------------------------------------------------------------------------------
**Project starting point is 'GUI_adv_2.py'**


