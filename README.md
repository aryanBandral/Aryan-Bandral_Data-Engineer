# xml_to_csv
A python code to convert xml file to csv (steeleye)


As the xml file that was provided had an error in it:

(
root = etree.fromstring(response.content)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "src\lxml\etree.pyx", line 3257, in lxml.etree.fromstring
  File "src\lxml\parser.pxi", line 1916, in lxml.etree._parseMemoryDocument
  File "src\lxml\parser.pxi", line 1803, in lxml.etree._parseDoc
  File "src\lxml\parser.pxi", line 1144, in lxml.etree._BaseParser._parseDoc
  File "src\lxml\parser.pxi", line 618, in lxml.etree._ParserContext._handleParseResultDoc
  File "src\lxml\parser.pxi", line 728, in lxml.etree._handleParseResult
  File "src\lxml\parser.pxi", line 657, in lxml.etree._raiseParseError
  File "<string>", line 1
lxml.etree.XMLSyntaxError: Opening and ending tag mismatch: hr line 1 and div, line 1, column 2369
)

As the error shows there is a mismatched tag that exists in the xml file, and due to the sheer size of the file I was not able to find the error,
because the file wont open completely.

I was not able to completelty work with the file. however, the code should work for other xml files and should be able to convert them into csv without any issues.
