<img src="https://github.com/PawelSala/Python2/assets/97036429/c927a017-a53b-4081-978b-ef4e82f8afaf"/>

## Table of Contents :scroll:
* [Project overview](#project-overview-rocket)
* [Technologies](#technologies-wrench)
* [Screenshots](#screenshots-desktop_computer)
* [Installation](#installation-magic_wand)
* [Additional Information](#additional-information-loudspeaker)
* [Authors](#authors-black_nib)
## Project overview :rocket:
OrganizeMe app with calendar and notes. The app greets users with a login/register form upon entry.  We used Firebase Authentication to remember users. Once logged in, 
you can change the view between annual and monthly calendar and add notes with "+". To delete notes click "-", and 
to log out - expand the side menu.

## Technologies :wrench:
#### Project is created with:
* python 3.12.1
* figma
* JSON
* Firebase Authentication

## Screenshots :desktop_computer:
<img src="https://github.com/PawelSala/Python2/assets/97036429/daff3ed8-107d-4a22-968a-14b3143be0df" width="500"/>
<img src="https://github.com/PawelSala/Python2/assets/97036429/2df3437a-43b4-4f39-a8aa-766f804458cb" width="1300"/>

## Installation :magic_wand:
##### Clone repository and install dependencies
* git clone https://github.com/Lesiiaa/OrganizeMe.git
* pip install -r requirements.txt
##### Configure .env file 
* go to [Firebase Console](https://console.firebase.google.com/u/0/?_gl=1*wfv8hx*_ga*MTE2NDM1MzA3MC4xNzIwNTI3MDE0*_ga_CW55HF8NVT*MTcyMDUyNzAxMy4xLjEuMTcyMDUyNzMxMS4wLjAuMA..&pli=1)
* create new project
* configure .env file with your Firebase configuration
```python
apiKey=your_api_key_here
authDomain=your_project_id.firebaseapp.com
databaseURL=https://your_project_id.firebaseio.com
projectId=your_project_id
storageBucket=your_project_id.appspot.com
messagingSenderId=your_messaging_sender_id
appId=your_app_id
```
##### Now you can start the project!
* python main.py

## Additional Information :loudspeaker:
#### Please note that the appearance of the project may vary on different screens due to the challenges of adapting the project to various screen sizes.
If u encounter display isssues (especially on laptops), consider using the `graphics_2.py` file located in the `laptop_ver` folder. To use it, replace the graphics.py file with graphics_2.py and rename it to `graphics.py`. This may improve the display of the project on your computer.

## Authors :black_nib:
* Dominika Pucyk
* Paweł Sala
* Letycja Niemiec
