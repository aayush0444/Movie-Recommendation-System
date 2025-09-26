Movie Recommendation System

This project is a showcase of how to use scikit-learn libraries to create a machine learning model. This model is trained on a specific dataset to perform a specific task: recommending movies.

Live Demo-https://movie-recommendation-system-e9es8hxjqm5rtpbok9it6x.streamlit.app/

You can see a live demo of this project here: Movie Recommendation System

Getting Started

To get a local copy of this project, you can clone the repository to your machine.

    Clone the repository:

    git clone https://github.com/aayush0444/Movie-Recommendation-System.git

    Navigate into the project directory:

    cd Movie-Recommendation-System

The Idea Behind the Project

We've all been in that situation where we want to watch a movie but can't decide what to pick. We often end up searching for a movie that gives the same thrill and enjoyment as one of our favorites. This project was created to solve that problem by building a movie recommendation system that suggests similar movies based on your liking.

How It's Built

Data

The first and most crucial step was gathering data. This project uses a dataset of 5,000 movies from The Movie Database (TMDb). While this is a small dataset, it provides decent predictions. A larger dataset could be used, but it would introduce additional challenges.

Data Preprocessing

After gathering the data, the next step was cleaning and preprocessing. A major task in this phase was creating a tags column. This column helps to find the type and context of a particular movie, which is then used by the model to provide specific recommendations.

Model Building

The model uses CountVectorizer, a simple but highly effective and lightweight model for predictions. It works by counting the number of each word in a movie's description to create a vector representation.

Recommendations

To find the closest movies for a given one, I used cosine similarity. This is a very useful mathematical approach for finding the similarity between two vectors in a multidimensional space.

Deployment

A good model is only part of the project; showcasing it is also crucial. For deployment, I used Streamlit, a powerful tool that helps to deploy our project and display the model's results on a web page. This makes the project easily accessible and user-friendly.

I hope reading this documentation gives you a clear understanding of the thought process behind developing a project like this and the steps involved.

Thank you for your patience in reading this document.

Author: Aayush Kumar
