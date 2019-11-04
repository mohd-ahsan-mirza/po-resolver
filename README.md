# Description
I built this handy little tool because resolving code conflicts in PO files with thousands of translations is very tedious. With this tool you can merge any number of po files you want. The resulting PO file will have all the unique translations from all the po files passed as arguments.

# Example
` python3 main.py {destination branch po file } {source branch po file} `

# Usage
After generating the `result.po` file, copy paste the content of the file into your `source branch po file`. The code conflicts should resolve

# Note
* The file generated can have some duplicates
* Ideally on merge two PO files at a time if you are trying to resolve code conflicts
