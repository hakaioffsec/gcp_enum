import argparse
import subprocess

def authenticate_service_account(json_file_path, key_file_path):
    try:
        if not key_file_path:
            raise ValueError("Key file path not provided.")
        
        # Authenticate the service account using the provided key file
        command = f"gcloud auth activate-service-account --key-file={key_file_path}"
        subprocess.run(command, shell=True, check=True)
        print("Authentication successful.")

    except ValueError as ve:
        print(f"Failed to authenticate: {str(ve)}")
    except Exception as e:
        print(f"Failed to authenticate: {str(e)}")

def list_resources(resource_type, command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
        resources = result.stdout.decode().split('\n')
        for resource in resources:
            print(f"{resource_type}: {resource}")

    except Exception as e:
        print(f"Failed to list {resource_type}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Authenticate and list GCP resources")
    parser.add_argument("-f", "--file", required=True, help="Path to the JSON key file")
    args = parser.parse_args()

    # Authenticate using the provided JSON key file
    authenticate_service_account(args.file, args.file)

    # List GCP resources
    resource_commands = {
        "Cloud Storage Buckets": "gsutil ls",
        "Cloud Storage Buckets2": "gcloud storage buckets list", 
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
        "Cloud KMS Keyrings": "gcloud kms keyrings list --location=global",
    }

    for resource_type, command in resource_commands.items():
        print(f"Listing {resource_type}:")
        list_resources(resource_type, command)
