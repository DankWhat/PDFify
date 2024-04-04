# PDFify: Web Scraper to PDF

PDFify is a Python script that converts web pages into PDF documents. It utilizes BeautifulSoup (bs4) for web scraping and FPDF for PDF generation. This tool is useful for creating offline copies of web content or archiving web pages for reference.

## Usage

1. **Clone the Repository**: Clone the PDFify repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/pdfify.git
    cd pdfify
    ```

2. **Install Dependencies**: Ensure you have Python installed, then install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Script**: Execute the Python script and provide the URL of the web page you want to convert to PDF:

    ```bash
    python pdfify.py <url>
    ```

    Replace `<url>` with the URL of the web page you want to convert.

4. **Output**: The script will generate a PDF file named `output.pdf` in the current directory containing the content of the specified web page.

## Features

- Converts web pages to PDF format.
- Supports conversion of both static and dynamic web pages.
- Customizable PDF output options, such as page size, orientation, and margins.

## Example

```bash
python pdfify.py https://example.com
```

  # Output : 
  ```lua
PDF file generated: output.pdf
```
## Contributing
Contributions are welcome! Feel free to submit issues or pull requests for any improvements or feature additions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

```css

This documentation provides clear instructions on how to use the PDFify script, including cloning the repository, installing dependencies, running the script, and understanding its features. Additionally, it includes an example command and output to demonstrate its usage.
```
