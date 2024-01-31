# Overview
This Python script simplifies authentication and resource listing in Google Cloud Platform (GCP). 

It automates the process of authenticating GCP service accounts using JSON key files and provides a convenient way to list various GCP resources.

# Usage
Make sure you have the Google Cloud SDK installed, as the tool utilizes the `gcloud`, `gsutil`, and `bq` commands.

To authenticate and test GCP resource access, use the following command:
```
python3 gcp_enum.py -f <path_to_json_key_file> -o <output_file>
```
You can also list available service accounts that you have authenticated previously with:
```
python3 gcp_enum.py -l
```
To switch to a specific service account and run tests, use the following command:
```
python3 gcp_enum.py -s <service_account_email> -o <output_file>
```
All options:
```
options:
  -h, --help            show this help message and exit
  -l, --list-accounts   List available service accounts and exit
  -s SERVICE_ACCOUNT, --service-account SERVICE_ACCOUNT
                        Switch to the specified service account and run tests
  -f FILE, --file FILE  Path to the JSON key file
  -o OUTPUT, --output OUTPUT
                        Path to the output file
  -t TIMEOUT, --timeout TIMEOUT
                        Timeout in seconds (default: 30)
```

# Tests
The script performs various tests to list GCP resources, including:
```
    Cloud Storage Buckets
    Pub/Sub Topics
    BigQuery
    Compute Engine Firewall Rules
    Compute Engine Network Subnets
    IAM Service Accounts
    GCP Projects
    Compute Engine Instance Templates
    Compute Engine Images
    Cloud Functions
    Pub/Sub Subscriptions
    Compute Engine Backend Services
    AI Platform Models
    AI Platform Jobs
    Cloud Run Managed Services
    Cloud Run GKE Services
    Cloud SQL Instances
    Cloud Spanner Instances
    Cloud Bigtable Instances
    Cloud Filestore Instances
    Kubernetes Engine Clusters
    Container Images
    Secrets
    Cloud KMS Keyrings
```
# Examples
![Screenshot_7](https://github.com/b-hermes/gcp_enum/assets/39487743/bfcd5c79-4367-4020-92fb-f6501a82f998)


# References
While developing the tool I found [this](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-public/gcp_enum) script from [Chris Moberly](https://www.linkedin.com/in/chrismoberly) and I realized that I had some tests that I missed to add. 
