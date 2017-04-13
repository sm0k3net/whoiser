# whoiser
python script for parsing domains owners data (email, phone etc) from WHOIS

WHOISER is Python3 script for domains WHOIS information gathering into MySQL database (emails, phones etc)
<pre>
1. Import mysql database script
2. Upload whoiser.py
3. Set 755 rights on whoiser.py ($ chmod +x whoiser.py)
4. Prepare file with domains list (1 domain in line)
5. Configure script with database access credentials (line 25 in whoiser.py)
Execute script with path to file with domains list: "python3 whoiser.py domains.txt"

Example file with domains from alexa top 1mil you can find in this repo as well.

If uncomment line 87 in "whoiser.py" file, than you will also have output into HTML file "results.html".
</pre>
