import argparse
import subprocess
import json

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

def test_resource_access(resource_type, command, output_file, timeout_seconds):
    try:
        result = subprocess.run(command, shell=True, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout_seconds)
        if result.returncode == 0:
            access_status = f"{resource_type} access granted"
        else:
            access_status = f"{resource_type} access denied"

        # Print the access status directly and save the full output to the specified file
        print(access_status)
        with open(output_file, "a") as file:
            file.write(f"{access_status}\n")
            file.write(result.stdout)
            file.write("\n")
            file.write(result.stderr)
            file.write("\n")

    except subprocess.TimeoutExpired:
        print(f"{resource_type} test timed out after {timeout_seconds} seconds")
    except Exception as e:
        print(f"Failed to test {resource_type} access: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Authenticate and test GCP resource access")
    parser.add_argument("-f", "--file", required=True, help="Path to the JSON key file")
    parser.add_argument("-o", "--output", required=True, help="Path to the output file")
    parser.add_argument("-t", "--timeout", type=int, default=30, help="Timeout in seconds (default: 30)")
    args = parser.parse_args()

    # Clear the content of the output file
    with open(args.output, "w") as file:
        file.write("")

    # Authenticate using the provided JSON key file
    authenticate_service_account(args.file, args.file)

    # Test GCP resource access and save the results
    resource_commands = {
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
    }

    for resource_type, command in resource_commands.items():
        test_resource_access(resource_type, command, args.output, args.timeout)
