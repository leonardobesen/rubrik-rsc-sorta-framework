# rubrik-rsc-sorta-framework

Python code that makes easier to create automations for Rubrik Security Cloud (RSC)

## Dependencies

- Python >= 3.11
- pandas
- openpyxl
- google-api-python-client
- google-auth-oauthlib

## How to use it

1- Create a JSON file named `config.json` with your Rubrik Security Cloud (RSC) and RSC Service Account information like in the example below and add it inside `configuration` folder:

*config.json*

```json
{
 "client_id": "your_client_id",
 "client_secret": "your_client_secret",
 "name": "name_you_gave",
 "access_token_uri": "https://yourdomain.my.rubrik.com/api/client_token",
 "graphql_url": "https://yourdomain.my.rubrik.com/api/graphql",
 "google_drive_upload_folder_id": ["your_drive_folders_ids_here"],
 "tz_info": "America/Sao_Paulo",
 "excluded_clusters_uuids": ["cluster_uuid_that_you_want_to_exclude"]
}
```

`config.json` parameters explained:

| Key Name                      | Required? | What it does                                                |
| ----------------------------- | --------- | ----------------------------------------------------------- |
| client_id                     | `Yes`     | RSC Service Account Id                                      |
| client_secret                 | `Yes`     | RSC Service Account "password"                              |
| name                          | `Yes`     | RSC Service Account Name                                    |
| access_token_uri              | `Yes`     | On the URL example above replace the inicial domain with your RSC domain |
| graphql_url                   | `Yes`     | On the URL example above replace the inicial domain with your RSC domain |
| google_drive_upload_folder_id | `No`      | Google Drive Folder Id you want to upload your final report. If left blank (`""`) it will **skip** the process that upload the file to Google Drive |
| tz_info                       | `No`      | Your timezone for date and time convertions, if necessary. If `tz_info` is not declared or left blank (`""`) it will use UTC+0. To select the correct timezone name use `pytz.all_timezones` on a Python Prompt with the lib `pytz` imported |
| excluded_clusters_uuids       | `No`      | List of clusters you want to exclude. In case you will use the function `get_excluded_clusters_uuids` avaliable in `configuration\configuration.py`|

2 - *(Skip this step if you did NOT declare `google_drive_upload_folder_id` on `config.json`)*
You must create a file named `google_drive.json` on `configuration` folder. See the file example below:

*google_drive.json*

```json
{
  "installed": {
    "client_id": "your_client_id",
    "project_id": "your_project_id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "your_client_secret",
    "redirect_uris": ["http://localhost"]
  }
}
```

3- Download this repository and place in a computer or server that has access to your Rubrik RSC.

4- Run main.py
