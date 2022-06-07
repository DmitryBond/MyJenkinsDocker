#!/bin/sh
#CGI script for displaying CPU usage on a web page

#Output the header
echo Content-type: text/html
echo

#Output the top of the html page
echo "<html><head><title>CPU Usage</title></head>"
echo "<body>"

#Stick anything to go above the table on the webpage here

#output the table with the CPU usage
echo "<table border=1>"
echo "<tr><td>CPU</td><td colspan=2>% Usage</td></tr>"
mpstat -P ALL 1 1 | sed /^$/d | sed /^Linux/d | sed -n '/CPU/,/CPU/p' | sed /CPU/d | awk ' { print "<tr><td>",$2,"</td><td>",100-$10,"</td><td><div style=\"width:",(100-$10)*2,"px;background:green;border: 1px solid black;\">&nbsp;</div></td></tr>" }'
echo "</table>"

#Put anything to go below the table on the webpage here

#Finish off the HTML output.
echo "</body></html>
