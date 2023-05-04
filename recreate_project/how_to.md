What do you need to do to recreate project?

* Create GCP account
* Create a new project & empty gcs bucket
* Create a google service account and strore credentials `/c/Users/<my_user>/.google/credentials/google_credentials.json`, and change the path in docker-compose file
* Create Open Sky API username (or remove the auth from the mage loaders, it can be used anonymously)
* Create a git clone of this project on your local computer.
* If you want to play around with the python files in `test-py` folder - create a env using `conda create --name <environment_name> --file requirements.txt`
* Fill out the `.example.env` and `.example.env_pg` and move to main project folder, remove .example prefix from file (don't worry, they are .gitignore'd)
* Upload files Airport & Airline Files to GCS from https://openflights.org/data.html
* Build External Tables in BigQuery using the `build_external_tables.sql` commands
* Follow docker build commands in `useful_commands.md` file
* Open Mage-AI web interface on [http://localhost:6789/](http://localhost:6789/)
* Add 'airport' variable of icao code of choice to mage pipeline, such as LLBG.
* Create backfill of wanted dates
* Run DBT Model Pipeline
* Connect BigQuery to PowerBI File (flights project.pbix)
* Enjoy!
