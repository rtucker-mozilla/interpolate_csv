# interpolate_csv
Python script to take CSV input and run commands or output strings

## Example CSV

hostname,dnsserver  
mozilla.com,4.2.2.2  

csv_interpolate.py -x -s -f "input.csv" -c "host {} {}" -d "1,3"

The preceeding would execute:

host mozilla.com 4.2.2.2

You can also use positional interpolation

csv_interpolate.py -s -f "input.csv" -c "host {0} {1} {0}" -d "1,3"

would output (lack of -x)

host mozilla.com 4.2.2.2 mozilla.com
