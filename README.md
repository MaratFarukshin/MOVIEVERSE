# **Movie Review Website**
A Django-based website for reviewing movies and TV series, allowing users to explore movie information, manage watchlists, and filter or sort movies by genres, awards, and more. This site integrates with the TMDb API to fetch movie and TV show data.



## Features

### 1. **Movie Search**
Search for movies using the search bar and filters to quickly find details about your favorite movies and TV series.


### 2. **Watchlist**
Users can add movies and TV shows to their personal watchlist.
View, manage, and organize the watchlist according to preferences.


### 3. **Filters and Sorting**
Genre and Award Filters: Narrow down movie results by genre or award categories.
Sorting Options: Sort movies by title, release date, or rating to easily browse content.


### 4. **Follow System**
Follow actors, directors, and other users to receive updates.
Get notified when new movies or shows featuring followed actors or directed by followed directors are released.
### 5. **User Profiles**
Custom User Model: Each user has a personalized profile page where they can view their activity, watchlist, and followed actors/directors/profiles.
### 6. **Reviews and Ratings**
User Reviews: Users can leave detailed reviews for movies and TV series.
Rating System: Rate movies/TV series on a scale of 1 to 10, with average ratings displayed on the movie pages.
### 7. **List creation**

### 8. **User Roles and Permissions**
* Admin: Full access to manage all content on the website, including adding, editing, and deleting movies, TV series, and user reviews. Admins can also manage user accounts and permissions.
* Moderator: Ability to review, approve, or remove user-submitted content such as reviews and comments. Moderators can also manage flagged content for potential issues.
* User: Standard access to the platform, including adding movies or TV shows to their watchlist, leaving reviews, and rating content. Users can follow other users, actors, and directors.

### **Technologies Used**
- Backend: Django (Python)
- Frontend: HTML5, CSS3, JavaScript

### **API Integration:**
This project integrates with the TMDb API to fetch real-time movie and TV series data, including:

- Titles
- Overviews
- Release Dates
- Posters and Backdrops

## Installation

1. **Clone the Repository**

   Clone the project from GitHub to your local machine:

2. **Create and Activate a Virtual Environment**
    ``` bash
    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment

    # On Windows
    venv\Scripts\activate

    # On macOS/Linux
    source venv/bin/activate

3. **Install project dependancies**
   ```bash
   pip install -r requirements.txt

4. **Set Up the Database**
   ```bash
   python manage.py migrate

5. **Create a Superuser (Optional)**
   ```bash
   python manage.py createsuperuser

6. **Run the Development Server**
   ```bash
   python manage.py runserver
You can now access the project at http://127.0.0.1:8000/.
