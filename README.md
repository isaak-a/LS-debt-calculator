# Law School Debt Calculator

This repository contains all of the code for [lsdebt.com](https://www.lsdebt.com/), a website to help future law students (or those just considering law school) **quickly and easily estimate law school costs**. 

## The Site

[lsdebt.com](https://www.lsdebt.com/) is built with [Plotly Dash](https://plotly.com/dash/), a framework for building dashboards. 

It's currently deployed on [Heroku](https://www.heroku.com/). 

## Running Locally

First, check out this repository, then open a terminal and `cd` to the repo's root directory. 

Then copy the example `.env` file and choose a username, password, and database name (doesn't matter too much for just running locally):

```bash
cp .env.example .env
```

Fill out `.env` like so: 

```
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_USER=<insert username>
POSTGRES_PASSWORD=<insert password>
POSTGRES_DB=<pick a db name - mine's 'law-school-data'>
```

Build the images: 

```bash
docker-compose build
```

Then finally run the container: 

```bash
docker-compose up
```

Open up <http://localhost:8050> in a browser to view the site. It won't have any data available yet - I'm working on a script to conveniently load the database from publicly available data. 

## About the Data

Currently, data comes from two places: 

- [ABA Required Disclosures](https://www.abarequireddisclosures.org/Disclosure509.aspx) - Data from reports from law schools mandated by the American Bar Association to maintain accreditation. Includes all of the costs and expenses for attending law schools. 
- [publiclegal](https://www.ilrg.com/rankings/law/median/1/desc/MSPrivate) website - Law school median salaries for public and private sectors. 

## About the Project

Funnily enough, I am not (nor do I ever plan to be) a law student! I built this project to help a good friend as they went through the law school process, so that they could easily compare the costs of various law schools, including scholarships and cost of living. 

I thought maybe it could be of some use to other law students, so left the website up. Suggestions and improvement ideas more than welcome! Feel free to make an Issue right here in this repo. 
