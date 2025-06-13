# Google Sheets MCP Server

This MCP server provides a seamless interface to interact with Google Sheets using a service account authentication method. It allows you to perform various operations on your Google Sheets such as listing sheets, locating information, retrieving contact details, and adding new contacts.

## Prerequisites

1. Python 3.x
2. Google Cloud Project with Google Sheets API enabled
3. Service Account credentials (JSON file)
4. Access to a Google Sheet with the service account email shared

## Setup Instructions

1. **Create a Service Account**:
   - Go to Google Cloud Console
   - Create a new project or select an existing one
   - Enable the Google Sheets API
   - Create a service account and download the JSON credentials file
   - Save the credentials file securely (e.g., `credentials.json`)

2. **Share Your Google Sheet**:
   - Open your Google Sheet
   - Click the "Share" button
   - Add the service account email (found in your credentials.json) as an editor
   - Copy the Sheet ID from the URL (the long string between /d/ and /edit in the URL)

3. **Environment Setup**:
   Create a `.env` file with the following content:
   ```
   SHEET=your_sheet_id_here
   ```

## Project Structure

```
sheets/
├── sheetServer.py      # Main MCP server entry point
├── environments/
│   ├── loader.py       # Authentication and initialization logic
│   └── __init__.py
└── README.md
```

## Available Tools

The MCP server provides the following tools:

1. `list_sheets()`: Lists all worksheets in the connected Google Sheet
2. `locate_info(info)`: Finds the row and column of specific information in the sheet
3. `get_number(name)`: Retrieves a contact's phone number
4. `get_email(name)`: Retrieves a contact's email address
5. `add_contact(body)`: Adds a new contact with name, number, and email

## Running the Server

To start the MCP server in development mode:

```bash
mcp dev sheetServer.py
```

## Example Usage

```python
# Example of adding a new contact
contact_data = {
    "name": "John Doe",
    "number": "1234567890",
    "email": "john@example.com"
}
add_contact(contact_data)

# Example of retrieving contact information
email = get_email("John Doe")
number = get_number("John Doe")
```

## Security Notes

- Keep your service account credentials file secure and never commit it to version control
- Regularly rotate your service account credentials
- Use appropriate access controls in your Google Sheet
- Consider implementing additional authentication layers for production use

## Troubleshooting

1. If you get authentication errors:
   - Verify that the service account email has been added to the Google Sheet
   - Check if the credentials file path is correct
   - Ensure the Sheet ID in your .env file is correct

2. If operations fail:
   - Verify that the Google Sheets API is enabled in your Google Cloud Console
   - Check if the service account has the necessary permissions
   - Ensure your sheet structure matches the expected format

## Contributing

Feel free to submit issues and enhancement requests!
