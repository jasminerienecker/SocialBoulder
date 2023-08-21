# SocialBoulder

To run locally:
- clone git repository
- cd into StPetersGym file
- check you have python version 3.11 <-- **python --version**
- make sure you have Django verison 4.2 installed <-- **python -m django --version**
- **python manage.py makemigrations**
- **python manage.py migrate**
- **python manage.py runserver** <-- this should start a webpage locally you can use for testing

  To make UI changes:
  - all the html is within the templates folder in each pyfolder (basically all relevant code is in bouldering/templates/bouldering)
  - it is currently very ugly (ie I have just added all css within the html files and a lot is quite hacky) so apologies there aha :)
  - it uses the model-view-controller architecture where view = templates, controller = views.py and model = models.py
  - email functionality to add a new user doesn't work yet!!
