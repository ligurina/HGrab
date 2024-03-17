#!/usr/bin/python3
import argparse
import requests

def get_emails(domain, api_key):
    url = f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}'
    try:
        response = requests.get(url)
        data = response.json()
        if data['data']['emails']:
            print(f"Email addresses found for {domain}:")
            for email in data['data']['emails']:
                print(email['value'])
        else:
            print(f"No email addresses found for {domain}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retrieve email addresses associated with a domain using Hunter.io API')
    parser.add_argument('domain', type=str, help='Target domain to retrieve email addresses from')
    parser.add_argument('--api_key', type=str, required=True, help='Hunter.io API key')
    # Parse the command-line arguments
    args = parser.parse_args()
    get_emails(args.domain, args.api_key)
