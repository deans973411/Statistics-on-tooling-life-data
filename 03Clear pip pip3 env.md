#### List all plugins 

    pip list


#### Output the plugins list
###### list all the plugins in text file, and run the `pip uninstall` with this list.

    pip freeze>python_modules.txt
    pip uninstall -r python_modules.txt -y
