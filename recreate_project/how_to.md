What do you need to do to recreate project?

* Create GCP account
* Create a new project & empty gcs bucket
* Create a google service account and strore credentials `/c/Users/<my_user>/.google/credentials/google_credentials.json`, and change the path in docker-compose file
* Create Open Sky API username (or remove the auth from the mage loaders, it can be used anonymously)
* Fill out the `.example.env` and `.example.env_pg` and move to project folder, remove .example prefix from file.
* Upload files Airport & Airline Files to GCS from https://openflights.org/data.html
* Build External Tables in BigQuery using the `build_external_tables.sql` commands
* Follow docker build commands in `useful_commands.md` file
* Create backfill of wanted dates
* Run DBT Model Pipeline
* Connect BigQuery to PowerBI File
* Enjoy!
