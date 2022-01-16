<!-- TABLE OF CONTENTS -->
## Table of Contents
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#important-points-on-task">Important Points On Task</a></li>
      </ul>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
</ol>

## About The Project
Sample API for unity interview process.
### Important Points On Task

1. For the below objective. </br>
`Build a premium game listing feature that allows users from the Unity app to unlock premium game tiles.` </br>
I have implemented a basic authentication mechanism, where authentication would mean that a user has a premium subscription and can view premium listings. </br>
To segregate premium listings from normal ones I have added a new flag in json response `isPremium` which when set would mean that a listing is premium and only authenticated users can see these.

2. This is the reference to the commit for using the response of web api in unity app. [Unity App Web API Integration](https://github.com/ktandon91/unity_challenge/commit/265ec14ced41b1b7141d064a4ee14484f777ad9c)

3. Swagger Documention of the project can be found on root url or on `http://localhost:8000/docs` </br>
 **Note: Make sure project is up and running to view swagger documentation**
 

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With
Technologies used.

* [FastAPI](https://fastapi.tiangolo.com/)
* [Mongodb](https://www.mongodb.com/)
* [Docker](https://www.docker.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure you have Docker installed on your system.

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/ktandon91/unity_challenge.git
   ```
   
2. Build and run docker images using below command.
   ```sh
   docker-compose build --up
   ```
   * Run the above command inside of project directory where `Dockerfile` and `docker-compose` file is residing.

3. Access the API on
   ```
   http://localhost:8000/
   ```

4. To load sample data `UITest.json`, make a simple get request to `/load`.  
    ```
    http://localhost:8000/load
    ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

All the APIs can be tested from swagger on below url.
   ```
   http://localhost:8000/docs
   ```
1. To get all the listings, make a get request on
    ```
    http://localhost:8000/api/games
    ```
2. To add a game listing, make a post request on
    ```
    http://localhost:8000/api/games
    ```
3. To view a single game listing, make a get request using game_id on.
    ```
    http://localhost:8000/api/games/{game_id}
    ```    
4. To update a game listing, make a put request using game_id on.
    ```
    http://localhost:8000/api/games/{game_id}
    ```    
5. To delete a game listing, make a delete using game_id request on.
    ```
    http://localhost:8000/api/games/{game_id}
    ```
