import argparse
import subprocess

# ANSI escape codes for colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def list_service_accounts():
    try:
        # Run 'gcloud auth list' to list available accounts
        command = "gcloud auth list --format='value(account)'"
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True)
        
        # Extract and print available service accounts
        accounts = result.stdout.strip().split('\n')
        print("Available service accounts:")
        for account in accounts:
            print(account)

    except Exception as e:
        print(f"{RED}Failed to list service accounts: {str(e)}{RESET}")

def test_resource_access(resource_type, command, output_file, timeout_seconds):
    try:
        result = subprocess.run(f"{command} --quiet", shell=True, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout_seconds)

        if result.returncode == 0 and result.stdout.strip() != "":
            access_status = f"{resource_type} access granted"
            access_color = GREEN
        else:
            # Check if the stderr contains specific authentication error messages
            if "insufficientPermission" in result.stderr:
                access_status = f"{resource_type} access denied (authentication issue)"
            else:
                access_status = f"{resource_type} access denied"
            access_color = RED

        # Print the access status with color and save the full output to the specified file
        print(f"{access_color}{access_status}{RESET}")
        with open(output_file, "a") as file:
            file.write(f"{access_status}\n")
            file.write(result.stdout)
            file.write("\n")
            file.write(result.stderr)
            file.write("\n")

    except subprocess.TimeoutExpired:
        print(f"{RED}{resource_type} test timed out after {timeout_seconds} seconds{RESET}")
    except Exception as e:
        print(f"{RED}Failed to test {resource_type} access: {str(e)}{RESET}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Authenticate and test GCP resource access")
    parser.add_argument("-l", "--list-accounts", action="store_true", help="List available service accounts and exit")
    parser.add_argument("-s", "--service-account", help="Switch to the specified service account and run tests")
    parser.add_argument("-f", "--file", help="Path to the JSON key file")
    parser.add_argument("-o", "--output", help="Path to the output file")
    parser.add_argument("-t", "--timeout", type=int, default=30, help="Timeout in seconds (default: 30)")
    args = parser.parse_args()

    if args.list_accounts:
        list_service_accounts()
        exit()

    if args.service_account:
        # Switch to the specified service account
        switch_service_account(args.service_account)
    elif args.file:
        # Authenticate using the provided JSON key file
        try:
            # Authenticate the service account using the provided key file
            command = f"gcloud auth activate-service-account --key-file={args.file}"
            subprocess.run(command, shell=True, check=True)
            print("Authentication successful.")
        except Exception as e:
            print(f"{RED}Failed to authenticate: {str(e)}{RESET}")
            exit()
    else:
        print("Please specify a service account or provide a JSON key file.")
        exit()

    if args.output:
        # Clear the content of the output file if provided
        with open(args.output, "w") as file:
            file.write("")

    # Test GCP resource access and save the results
    resource_commands = {
        "AI Platform Jobs": "gcloud ai-platform jobs list",
        "AI Platform Models": "gcloud ai-platform models list",
        "BigQuery": "bq ls",
        "Cloud Bigtable Instances": "gcloud bigtable instances list",
        "Cloud Filestore Instances": "gcloud filestore instances list",
        "Cloud Functions": "gcloud functions list",
        "Cloud KMS Keyrings": "gcloud kms keyrings list",
        "Cloud Run GKE Services": "gcloud run services list --platform=gke",
        "Cloud Run Managed Services": "gcloud run services list --platform=managed",
        "Cloud Spanner Instances": "gcloud spanner instances list",
        "Cloud SQL Instances": "gcloud sql instances list",
	"Cloud Storage Buckets": "gsutil ls",
        "Compute Engine Backend Services": "gcloud compute backend-services list",
        "Compute Engine Firewall Rules": "gcloud compute firewall-rules list",
        "Compute Engine Images": "gcloud compute images list",
        "Compute Engine Instance Templates": "gcloud compute instance-templates list",
        "Compute Engine Network Subnets": "gcloud compute networks subnets list",
        "Container Images": "gcloud container images list",
        "GCP Projects": "gcloud projects list",
        "IAM Service Accounts": "gcloud iam service-accounts list",
        "Kubernetes Engine Clusters": "gcloud container clusters list",
        "Pub/Sub Subscriptions": "gcloud pubsub subscriptions list",
        "Pub/Sub topics": "gcloud pubsub topics list",
        "Secrets": "gcloud secrets list",

    }

    for resource_type, command in resource_commands.items():
        test_resource_access(resource_type, command, args.output, args.timeout)
