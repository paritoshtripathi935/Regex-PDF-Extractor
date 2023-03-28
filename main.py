import re
import PyPDF2

# Open the PDF file
pdf_file = open('AWS Lambda Pricing.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Initialize the output list
output = []


page = pdf_reader.pages[0]
text = page.extract_text()

# Use regex to extract the table data
table_regex = r'(\d+)\s+(.+)\s+(\$[\d\.]+\sfor\severy\sGB-second)\s+(\$[\d\.]+\sper\s1M\srequests)'
table_data = re.findall(table_regex, text)

# Format the data as JSON
output = []
for row in table_data:
    id, architecture, duration, requests = row
    output.append({
        'id': id,
        'Architecture': architecture,
        'Duration': duration,
        'Requests': requests
    })
result = {'output': output}

# Close the PDF file
pdf_file.close()

# Print the output list
print(output)


'''
This code reads a PDF file containing a table of AWS Lambda pricing information, extracts the table data using regular expressions, and outputs the data as a list of dictionaries in JSON format.
The code first imports the necessary modules, re for regular expressions and PyPDF2 for working with PDF files. It then opens the PDF file in binary mode and creates a PdfReader object to read the contents of the file. The number of pages in the PDF is determined using the len function.
Next, the code extracts the text from the first page of the PDF using the extract_text method of the pages object. The regular expression table_regex is used to extract the data from the table on this page. This regular expression captures four groups of data for each row of the table: the ID, architecture, duration, and requests.
The code then formats the extracted data as a list of dictionaries, where each dictionary represents a row of the table. The id, Architecture, Duration, and Requests keys of each dictionary correspond to the four groups of data captured by the regular expression.
Finally, the list of dictionaries is formatted as a JSON object and printed to the console. The PDF file is then closed using the close method.
Note that this code assumes that the table is on the first page of the PDF file. If the table is on a different page, the pages object should be indexed accordingly. Additionally, the regular expression table_regex may need to be adjusted if the format of the table is different from what is expected.
'''
