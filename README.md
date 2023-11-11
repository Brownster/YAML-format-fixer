# YAML Format Fixer

The YAML Format Fixer is a Flask web application designed to help clean up and fix indentation and formatting issues in YAML files. It provides a simple interface to upload YAML files and download the fixed versions, as well as a diff report highlighting the changes made.

## Features

- Upload YAML files with formatting issues.
- Document Start Marker: Ensures that the file starts with the correct YAML document start marker ---.
- Indentation: Adjusts the indentation of lines to match the structure of the YAML content. This includes:

    Ensuring consistent indentation levels.
    Adjusting comment lines to align with the indentation of the following code block.

- Trailing Spaces: Removes any trailing whitespace at the end of lines.
- Consecutive Blank Lines: Ensures there are no consecutive blank lines, maintaining only single line breaks between blocks for readability.
- Document End Marker: Checks for a document end marker ... and removes it if present, as it is not always necessary.
- Provides a downloadable diff report detailing the changes.
- Download the fixed YAML file.
- Files are automatically deleted after download for privacy.

## Local Setup

To set up the application on your local machine, follow these steps:

1. Ensure you have Python 3.7+ installed on your machine.

2. Clone this repository to your local machine using:

    ```sh
    git clone https://github.com/Brownster/YAML-Format-Fixer.git
    cd YAML-Format-Fixer
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:

    ```sh
    python app.py
    ```

5. Open your web browser and navigate to `http://127.0.0.1:5000` to use the application.

## Usage

- Navigate to the home page.
- Click on the "Choose File" button and select a YAML file with formatting issues.
- Click on "Upload" to submit the file for processing.
- Once processed, you'll be presented with a diff report on the web page.
- Use the provided links to download the fixed YAML file and the diff report.

## Deployment

This app can be deployed on cloud platforms like Render, Heroku, AWS, etc. Follow the platform-specific instructions to deploy a Flask application.

## Contributing

Contributions to improve YAML Format Fixer are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
