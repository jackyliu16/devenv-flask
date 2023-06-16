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
        - test 230616 20:44
    2. #### Document Conventions
        In these documents we distribute bold world as the key for the statement, italic as relatively unimportant supplement.

        Abbreviations | Description
        ------------- | -----------
        DB            | databases
        BC            | because

    3. #### Intended Audience
        The software we provide is aimed at users who want to be as simple as possible, do not need to learn too many applications, directly use a website, achieve travel planning and facilitate the use of taxis during the trip. People with functions such as hotel reservation.
    4. #### PROJECT SCOPE
        The purpose of the online safari Website is to ease travel management and to create a convenient and easy-to-use application for traveler. The system is based on a relational database with user login operation, and making there travel plans. We will have a list of APIs calling for the services from other commercial software. Above all, we hope to provide a comfortable user experience along when they are planing for traveling and travel.
    5. #### Contact Information / SRS team members
        Student Name | Student ID
        ------------ | ---------
        马越         | 20200740014
        刘逸珑       | 20200740029
        刘峻琪       | 20202033010
        朱道鑫       | 20202033015

    6. #### Reference
        - [Software Requirements Specification document with example](https://krazytech.com/projects/sample-software-requirements-specificationsrs-report-airline-database)
        - [How To Add Authentication to Your App with Flask-Login](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
        - develop environment
            - [devenv](https://devenv.sh/)
            - [NixOS](https://nixos.org/)

2. ### Overall Description
    1. #### Product Perspective
        This product a Travel Planning and Execution Website, which provide a main function to helping customers to finish there travel plans.
        When user trying to plane there travel plans or record or even using our website in the travel, we will pack the APIs provide by other Application, like Hotel Reservation and Uber.
    2. #### Product Functions
        1. 主要功能概述：
            - 提供旅游目的地搜索和浏览功能。
            - 允许用户查看目的地的详细信息，如景点、活动、交通和住宿。
            - 提供用户注册和登录功能，以便他们可以保存喜欢的目的地、制定行程和预订服务。
            - 支持在线预订旅行套餐、机票、酒店和租车等服务。
            - 提供用户评价和评论功能，让用户分享他们的旅行经历和建议。
            - 提供旅行指南、旅行建议和行程规划工具等辅助功能。
            - 支持用户支付功能，以便在线完成预订和购买。

        2. 功能组织：
            - 目的地搜索和浏览功能：
                - 提供搜索栏和过滤器，让用户根据目的地、日期、预算等条件查找适合的旅行目的地。
                - 显示目的地的缩略信息和图片，供用户快速浏览。
                - 提供目的地的详细页面，包括景点介绍、活动推荐、交通和住宿信息等。

            - 用户注册和登录功能：
                - 允许用户创建个人账户，填写基本信息和偏好设置。
                - 提供登录界面，确保用户可以安全访问其个人账户。

            - 在线预订功能：
                - 提供预订页面，让用户选择旅行套餐、机票、酒店、租车等服务，并提供价格和可用性信息。
                - 支持添加选项、定制行程，并提供实时价格计算。
                - 要求用户提供必要的预订信息，并提供安全的支付方式。

            - 用户评价和评论功能：
                - 允许用户为他们的旅行目的地和服务提供评分和评论。
                - 显示其他用户的评价和评论，以帮助用户做出决策。

            - 旅行指南和行程规划功能：
                - 提供旅行指南、当地文化和风俗介绍，帮助用户了解目的地。
                - 提供行程规划工具，让用户制定详细的行程计划，并提供导航和提醒功能。

            - 支付功能：
                - 集成安全的在线支付渠道，以便用户可以方便、安全地完成预订和购买。

        3. 相关需求图示：
            - 提供旅游网站的高层数据流图或对象类图，以显示主要功能之间的关系和交互。

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
    6. #### Design/implementation constraintsi

        This section describes any items or issues that will limit the options available to the developers. These may include hardware limitations (such as time requirements and memory requirements), interfaces to other applications, specific technologies, tools, and databases to be used, parallel operations, language requirements, communication protocols, security considerations, and design conventions or programming standards (for example, if the customer's organization will be responsible for maintaining the delivered software).

        Examples of design and implementation constraints include, but are not limited to:

        - Hardware limitations: The software must be able to run on a specified hardware environment and meet specific performance and memory requirements.
        - Interface limitations: The software must integrate with existing reservation systems and payment systems, adhering to their interface specifications.
        - Technology limitations: The development process must utilize specific technology stacks, such as Java, React, and MySQL.
        - Security limitations: The software must comply with relevant security standards and privacy regulations, including requirements for data encryption, access control, and authentication.
        - Design conventions and programming standards: Developers must adhere to the design conventions and coding standards of the customer's organization to ensure the delivered software is easy to maintain and extend.
        - Communication protocol limitations: The software must support common communication protocols, such as HTTP, HTTPS, and SMTP.
        - Database limitations: The software must utilize a specified database management system (such as MySQL) for data storage and management.
    7. #### Assumptions and dependencies

        This section lists any assumed factors (as opposed to known facts) that could affect the requirements stated in the SRS. These assumptions could include third-party or commercial components that are planned to be used, issues related to the development or operating environment, or any constraints. It is important to note that if these assumptions are incorrect, not shared, or change, they could potentially impact the project.

        Additionally, identify any dependencies the project has on external factors, such as software components that are intended to be reused from another project. If these dependencies are not already documented elsewhere (for example, in the vision and scope document or the project plan), they should be listed here.

        The following are examples of assumptions and dependencies for the project:

        Assumptions:
        - The availability of reliable internet connectivity for users to access the website.
        - The availability of necessary hardware resources to support the software's performance requirements.
        - The compatibility of the chosen development framework with the target operating systems and browsers.

        Dependencies:
        - Integration with a third-party payment gateway for secure online transactions.
        - Utilization of a geolocation service to provide location-based services for users.
        - Integration with a customer relationship management (CRM) system for managing user data and interactions.

        It is essential to regularly review and validate these assumptions and dependencies throughout the project lifecycle to ensure they remain accurate and up to date.

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
        1. Because the need of distributed development, the development environment need to be Reproducible.
    2. #### Safety Requirements
    3. #### Security Requirements
        1. BC our application will be using in the Online Payment, thus have external security need.
    4. #### Software Quality Attributes
    5. #### Project Documentation
    6. #### User Documentation
