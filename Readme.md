## Get started.

1. Create .env file in the /recipes directory and insert database connection parameters. (Use the .env.example for guidance)
2. Create venv with the `python3 -m venv venv` command.
3. Activate virtual envionment with the `source venv/bin/activate` command.
4. Install the necessary packages with the following command: `pip install -r requirements.txt`
5. Run `python manage.py tailwind install` and `python manage.py tailwind start` commands to generate static files.
6. You might need to apply/create migrations, therefore run the following commands:
   `python manage.py makemigrations`
   `python manage.py migrate`

7. Run the django application with `python manage.py runserver`
8. Head to the `http://127.0.0.1:8000/register/` and register into the website.
9. Use the website to create recipes, tags, ingredients.
10. Combine recipes with ingredients/tags.
11. Write reviews under the recipes.

## Notes.

1. Tailwind css framework is being used for the front-end styling if any changes need to be done, run the `python manage.py tailwind start` command.
2. All of the CSS is being stored in the `/theme/static/` directory.
3. When I created the project, I mistakenly named it `recipes`, therefore recipes/ directory is the main project directory.
4. All of the templates, models and migrations are being stored in the `core` app.
5. The website does not have a functioning admin website.
6. MySQL server has to be installed on the computer.
7. NodeJS has to be installed on the computer.
8. recipes database has to be created.

## Things that could be improved.

1. Redirection could sometimes be more rational.
2. Some of the Django templates could have been re-used, although for a project this small, didn't consider it to be a necessity.
3. There could be more data validation.
4. Front-end could be written with ReactJs as an SPA, it would improve speed.
5. Add Logout button.
