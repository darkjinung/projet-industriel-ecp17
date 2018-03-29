# Industrial Project
### ECP 2017-2018

*Authors*: Amine **B.**, Amine **A.**, Yoannis **T.**

# Goal
Implement NLP "Proof Of Concept" that determines the topic(s) of a given customer review as well as the sentiment(s).
In essence, POC will help to answer 2 key questions regarding a given review : 
 - What : which topic the review is about ? For i.e. consumers will focus more on the screen of a new released laptop than on the performance or the overall shape 
 - How : how consumers feel about the product ? For i.e happy, upset ...

# Strategy

Creation of a Black Box. (IA, Deep/Machine learning)

State of the Art [Research, Open Source, Proprietary]
 - Deep learning & Marchine Learning
 - Text Mining
 - Sentiment Analysis
 - Topic Analysis
 - Semantic Analysis

> Development of the Black Box through a project


# Project
Project coordinator: **SCRUM master** *per sprint*
  - [x] Roles & Responsabilities
  - [x] Phase zero
    - [x] Opportunity study
    - [x] Feasibility study (*State of the Art*)
  - [x] Definition (Analyse & Conception)
  - [x] Realisation (POC)
  - [x] Qualification (testing via promotion)


# Working environment 

**Documentation & Development**
> Github

**Planning & Coordination**
> Trello

**Live messaging**
> Google Hangout

**Project Managment Method**
> SCRUM

- - -

##**Déploiement sur Lambda:**
Endpoint AWS: https://a6odurddmf.execute-api.eu-west-1.amazonaws.com/dev/report


Exemple d'utilisation depuis le browser:
https://a6odurddmf.execute-api.eu-west-1.amazonaws.com/dev/report?review="Great build quality, great screen, great battery life and the best feature is the Face ID, quick and realible, much better and fast than a fingerprint scanner. The bad side it’s too expensive for what it is."


Utilisation avec Django:
> git clone git@github.com:darkjinung/projet-industriel-ecp17.git
> pip install virtualenv
> source projet-industriel-ecp17/Django-project-chart/Projet_Indus/Scripts/activate
> python projet-industriel-ecp17/Django-project-chart/manage.py runserver
> Depuis un navigateur aller sur localhost:8000

