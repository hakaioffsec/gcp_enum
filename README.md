# Overview
This Python script simplifies authentication and resource listing in Google Cloud Platform (GCP). 

It automates the process of authenticating GCP service accounts using JSON key files and provides a convenient way to list various GCP resources.

# Usage
Make sure you have the Google Cloud SDK installed, as the tool utilizes the `gcloud`, `gsutil`, and `bq` commands.

Pass the JSON service account key file with the -f flag and specify the output file with the -o flag. Optionally, you can set the timeout in seconds with the -t flag (default is 30 seconds).
```
python3 gcp_enum.py -f file.json -o output.txt
```


# Tests
The script performs various tests to list GCP resources, including:
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
# Example
![Screenshot_15](https://github.com/b-hermes/gcp_enum/assets/39487743/78806648-4075-4c0e-85ca-2bc5f640090f)

# References
While developing the tool I found [this](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-public/gcp_enum) script from [Chris Moberly](https://www.linkedin.com/in/chrismoberly) and I realized that I had some tests that I missed to add. 
