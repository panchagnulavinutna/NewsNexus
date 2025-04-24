NewsNexus: Connecting You To What Matters Most

NewsNexus is a personalized news recommendation system that helps users discover relevant news articles based on their interests and past reading history. It uses NLP-based text embeddings, similarity matching, and user interaction data to provide tailored recommendations.

Features
1. Personalized recommendations based on user history
2. Interest-based news search with real-time results
3. Interactive feedback system using like/dislike buttons
4. User activity logging and feedback collection for analysis

Technologies Used
1. Python 3.8+
2. Streamlit (Web-based frontend)
3. SentenceTransformers (Embedding model)
4. Scikit-learn (Similarity calculation)
5. Pandas (Data handling)
6. NewsAPI (Real-time news fetching)

How to Get a NewsAPI Key
1. Go to https://newsapi.org.
2. Sign up for a free account.
3. After logging in, navigate to the “API” section.
4. Copy your API key.

Once you have the API key:
1. Open app.py
2. Replace "your_newsapi_key" in the fetch_live_news function in app.py with your actual key
Example:
fetch_live_news(interest, api_key="your_actual_api_key")

Step-by-Step Execution
1. Fetch the Latest News Articles
Run the script to collect news data using your NewsAPI key:
`python news_api.py`
This will create a CSV file containing the latest articles.
2. Generate Article Embeddings
To create vector representations of the articles, run:
`python recommendate.py`
This will generate a file named news_embeddings.pkl with encoded data.
3. Launch the Streamlit App
Run the main application using:
`streamlit run app.py`
You will see the following tabs:
Explore by Interest: Enter your username and a topic of interest (e.g., music, finance). The system fetches live news articles related to the topic and allows you to like or dislike them.
Recommended for You: Enter your name to get recommendations based on your reading history.
4. Interaction Logging
All clicks are logged to user_history.csv
Like/Dislike feedback is saved in feedback.csv

Recommendation Logic
1. News articles are encoded into numerical vectors using a SentenceTransformer model.
2. For interest-based search, the user’s query is embedded and compared with news vectors using cosine similarity.
3. For personalized recommendations, recent article titles from the user’s history are embedded as a query and matched against available articles.

Output
1. Users receive article suggestions relevant to their input or reading behavior.
2. News titles and descriptions are displayed in sentence case, retaining original formatting.
3. Articles are separated visually, with large like/dislike buttons for feedback.
4. User behavior and feedback are saved for improving future recommendations.