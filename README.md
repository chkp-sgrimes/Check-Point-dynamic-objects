# Check-Point-dynamic-objects
Examples for creating and auditing dynamic objects

Dynamic object types offer a flexible way to update attributes used in access policies in a way that allows them to be updated using automation logic.  The ability to make ongoing changes to these object types sets them apart from traditional static objects and allows organizations flexibility with regard to changes associated with their applications and network infrastructure.


To use this collection
1. clone the repo
2. create a virtual [environment](https://docs.python.org/3/library/venv.html)
3. Invoke the virtual environment "source [path to the environment]/bin/activate"
4. Install the Check Point python SDK "pip install cp-mgmt-api-sdk"
5. If you would like to make objects available locally, install flask "pip install Flask"
6. Revise the hostname or IP address, account and password in cpclient.py
7. run the add_objects.py, del_objects.py, or show_objects.py mods with "python add_objects.py" 
The first time any mod is run you'll need to provide a "y" so that the SDK can create the fingerprints.txt file.
