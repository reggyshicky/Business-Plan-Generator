import pdfkit

def html_to_pdf(html_content, output_path='output.pdf'):
    try:
        # Configure pdfkit with the path to wkhtmltopdf
        pdfkit_config = pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')

        # Generate PDF from HTML content
        pdfkit.from_string(html_content, output_path, configuration=pdfkit_config)

        print(f'PDF successfully generated and saved to {output_path}')
    except Exception as e:
        print(f'Error: {e}')

# Example usage:
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a sample HTML content.</p>
</body>
</html>
"""

html_to_pdf(html_content, 'output.pdf')
