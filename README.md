# interpolate_csv
Python script to take CSV input and run commands or output strings

# Example CSV

hostname,dnsserver  
mozilla.com,4.2.2.2  

csv_interpolate.py -x -s -f "input.csv" -c "host {} {}" -d "1,3"

The preceeding would execute:

host mozilla.com 4.2.2.2
