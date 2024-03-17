# HGrab

HGrab is a Python script that retrieves email addresses associated with a domain using the Hunter.io API.

## Features

- **Domain Email Lookup**: Fetches email addresses associated with a specified domain.
- **Hunter.io Integration**: Utilizes the Hunter.io API for email address retrieval.
- **Customizable API Key**: Allows users to input their Hunter.io API key for authentication.

## Usage

1. Install Python 3.x if not already installed on your system.

2. Clone the repository:

    ```bash
    git clone https://github.com/ligurina/HGrab.git
    ```

3. Navigate to the project directory:

    ```bash
    cd HGrab
    ```

4. Run the script with the target domain and your Hunter.io API key:

    ```bash
    python3 HGrab.py example.com --api_key YOUR_API_KEY
    ```

   Replace `example.com` with the domain you want to retrieve email addresses from, and `YOUR_API_KEY` with your actual Hunter.io API key.

## Example

Running the script with a target domain:

```bash
python3 HGrab.py example.com --api_key abcdef1234567890
