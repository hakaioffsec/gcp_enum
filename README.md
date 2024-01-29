# Overview
This Python script simplifies authentication and resource listing in Google Cloud Platform (GCP). 

It automates the process of authenticating GCP service accounts using JSON key files and provides a convenient way to list various GCP resources.

# How to use
Pass the json service account key file with the -f flag and the output file with the -o flag.
```
python3 gcp_enum.py -f file.json -o output.txt
```

You need to have the Google Cloud SDK installed. 

The tool use the 'gcloud', 'gsutil' and 'bq' commands.

# Tests
The list of tests that are performed
```
"Cloud Storage Buckets": "gsutil ls",
"Pub/Sub topics": "gcloud pubsub topics list",
"BigQuery": "bq ls",
"Compute Engine Firewall Rules": "gcloud compute firewall-rules list",
"Compute Engine Network Subnets": "gcloud compute networks subnets list",
"IAM Service Accounts": "gcloud iam service-accounts list",
"GCP Projects": "gcloud projects list",
"Compute Engine Instance Templates": "gcloud compute instance-templates list",
"Compute Engine Images": "gcloud compute images list",
"Cloud Functions": "gcloud functions list",
"Pub/Sub Subscriptions": "gcloud pubsub subscriptions list",
"Compute Engine Backend Services": "gcloud compute backend-services list",
"AI Platform Models": "gcloud ai-platform models list",
"AI Platform Jobs": "gcloud ai-platform jobs list",
"Cloud Run Managed Services": "gcloud run services list --platform=managed",
"Cloud Run GKE Services": "gcloud run services list --platform=gke",
"Cloud SQL Instances": "gcloud sql instances list",
"Cloud Spanner Instances": "gcloud spanner instances list",
"Cloud Bigtable Instances": "gcloud bigtable instances list",
"Cloud Filestore Instances": "gcloud filestore instances list",
"Kubernetes Engine Clusters": "gcloud container clusters list",
"Container Images": "gcloud container images list",
"Secrets": "gcloud secrets list",
"Cloud KMS Keyrings": "gcloud kms keyrings list",
```
