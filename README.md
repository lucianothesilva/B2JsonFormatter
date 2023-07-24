# B2JsonFormatter
Python script to format json data extracted via RClone from Backblaze b2, it will bring Name and Size of the file and change the timezone to Brazilian.

Export the data with RClone

.\rclone.exe lsjson bucket-name: > FileList.json --recursive  

Then use the RCloneFormatter to generate a txt with the formatted data.
