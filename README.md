## Table of Contents
- [What is Child Care Aware?](#what-is-child-care-aware)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

# ccana

> An updated website for Child Care Aware of Northcentral Arkansas.

### What is Child Care Aware?

Child Care Aware of Northcentral Arkansas is a community child care resource and referral program providing services in fourteen Northcentral Arkansas counties. The program helps parents locate child care through a database of licensed and registered facilities based upon that family's needs all free of charge.

### Installation
Django can be installed with the following command:

`python -m pip install Django`

Additionally, this website also uses the *django-widget-tweaks* library
to render its forms. [Check out its repository](https://github.com/jazzband/django-widget-tweaks) for installation instructions.

### Usage
As with any Django website, you can launch the server with

`python3 manage.py runserver`

Most content served is static. The bulk of user-interaction (Referral Form, Contact Us) is self explanatory, as it primarily consists of simple forms.

Most admin interaction will come in the form of adding events to the registration page. This is handled through Django's built-in admin back-end and forms. 


### Credits
- [ericpinter](https://github.com/ericpinter)
- [SpenThompson](https://github.com/spenthompson)
- [ZacharyANelson](https://github.com/zacharyanelson)
- [astoyanow](https://github.com/astoyanow)
- [CWTBT](https://github.com/cwtbt)
