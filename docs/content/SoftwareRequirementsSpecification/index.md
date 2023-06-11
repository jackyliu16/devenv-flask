+++
title = "SRS (Software Requirements Specifications)"
description = "The SRS of Safari Website"
date = 2023-06-11
draft = false

[taxonomies]
categories = ["Safari"]
tags = ["SRS"]
[extra]
toc = true
keywords = "SRS"
# thumbnail = "ferris-gesture.png"
+++

This is the Software requirements specification of Safari Website.

<!-- more -->

1. ### Introduction
    1. #### Purpose
        Our project focuses on the collection problem that when user making travel plan. Nowadays, when user using application for traveling, they have to use many apps to complete the different step of tourism, We are trying to develop a website to contains all of this kind information into one website, and this website could be using in computer and mobile phone.
    2. #### Document Conventions
        In these documents we distribute bold world as the key for the statement, italic as relatively unimportant supplement.

        ```markdown
        The following is a description of the abbreviations used in this article. 
        | abbreviations | description |
        | ------------- | ----------- |
        | DB            | databases   |
        | BC            | because     |
        ```

    3. #### Intended Audience
        The software we provide is aimed at users who want to be as simple as possible, do not need to learn too many applications, directly use a website, achieve travel planning and facilitate the use of taxis during the trip. People with functions such as hotel reservation.
    4. #### PROJECT SCOPE
        The purpose of the online safari Website is to ease travel management and to create a convenient and easy-to-use application for traveler. The system is based on a relational database with user login operation, and making there travel plans. We will have a list of APIs calling for the services from other commercial software. Above all, we hope to provide a comfortable user experience along when they are planing for traveling and travel.
    5. #### Additional Information
    6. #### Contact Information / SRS team members
        - 20200740014: 马越
        - 20200740029: 刘逸珑
        - 202020: 朱道鑫
        - 202020: 刘峻琪
    7. #### Reference
        - [Software Requirements Specification document with example](https://krazytech.com/projects/sample-software-requirements-specificationsrs-report-airline-database)
2. ### Overall Description
    1. #### Product Perspective
        This product a Travel Planning and Execution Website, which provide a main function to helping customers to finish there travel plans.
        When user trying to plane there travel plans or record or even using our website in the travel, we will pack the APIs provide by other Application, like Hotel Reservation and Uber.
    2. #### Product Functions
    3. #### User classes and Characteristics
        The user of our website will be divided into 3 parts, planner, traveler, administrator, *maybe collision*.
        - Planner
            using our website to plan there trip, relatively high level of technology, higher level of education, the main use of computer sites to complete their operations.  
            #TODO If it should be place here.
            @ - Should be able to using our website to planning there travel, which contains we should provide map or other method to helping them with this.
            @ - When planner making the choice from A to B, our website should provide the route selection.
        - Traveler
            using our website to complete their journey with relative ease experience. Uncertain education and skill level, the main use is the phone website to complete their operations.
        - Administrator
            using to clean unfriendly content on the website and management user operation. Have higher level of education and skill level, the main terminals used are computer website and databases.
    4. #### Operating Environment
        The backend of our website is build on [devenv](https://devenv.sh/), which is a development environment depends on [nix](https://nixos.org/). Thus, it is portable in every computer on linux(i686, x86_64, aarch64) and macOS(x86_64, aarch64).
        #TODO finish this
        The test computer configuration as follows:
        - databases: MySQL
        - client/server system
        - Operating System: Linux
        - platform: flask
    5. #### User environment
        Almost all users access the site through a browser, some people using the website in computer, and other's using it in phone.
    6. #### Design/implementation constraints
    7. #### Assumptions and dependencies
3. ### External Interface Requirements
    1. #### User Interfaces
    2. #### Hardware interfaces
    3. #### Software Interfaces
    4. #### Communication Protocols and Interfaces
4. ### System Features
    1. #### System Feature A
        1. Description and Priority
        2. Action / Result
        3. Functional Requirements
    2. #### System Feature B
5. ### Other Nonfunctional Requirements
    1. #### Performance Requirements
    2. #### Safety Requirements
    3. #### Security Requirements
        1. BC our application will be using in the Online Payment, thus have external security need. 
    4. #### Software Quality Attributes
    5. #### Project Documentation
    6. #### User Documentation
