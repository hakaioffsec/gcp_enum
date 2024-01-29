# Overview
This Python script simplifies authentication and resource listing in Google Cloud Platform (GCP). 

It automates the process of authenticating GCP service accounts using JSON key files and provides a convenient way to list various GCP resources.

# How to use
Pass the json service account key file with the -f flag.
```
python3 gcp_enum.py -f file.json
```

You need to have the Google Cloud SDK installed. 

The tool use the 'gcloud', 'gsutil' and 'bq' commands.

# Tests
The list of tests that are performed
```
cloud storage buckets
pub/sub topics
pub/sub subscriptions
big query
compute engine network subnets
compute engine firewall rules
projects access list
cloud functions
compute engine backend services
AI platform models
AI platform jobs
cloud run managed services
cloud run GKE services
cloud sql instances
cloud spanner instances
cloud bigtable instances
cloud filestore instances
kubernetes engine clusters
container images
secrets manager
cloud kms keyrings
```
