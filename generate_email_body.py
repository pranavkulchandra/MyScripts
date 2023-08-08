import re

input_text = """
BRB_103_SQ02_0050_Animation_Polish_v0205
BRB_103_SQ02_0050_Animation_Polish_v0205.ma: 01 - Must version up
BRB_103_SQ02_0050_Animation_Polish_v0205.mov: 01 - Must version up
BRB_103_SQ04_0160_Animation_Polish_v0101
BRB_103_SQ04_0160_Animation_Polish_v0101.ma: 01 - Must version up
BRB_103_SQ04_0160_Animation_Polish_v0101.mov: 01 - Must version up

"""

# Split the input text into lines
lines = input_text.strip().split('\n')


# Regular expression pattern to match filenames and versions
pattern = r'^(BRB_[A-Za-z0-9_]+)\.(ma|mov): (\d+) -'

# Initialize a list to store matches
matches = []

# Process each line using the pattern
for line in lines:
    match = re.match(pattern, line)

    if match:
        matches.append(match.groups())

# Print the matches


# Initialize a dictionary to store the versions
version_dict = {}

# Process each match
for match in matches:
    filename, extension, version = match
    if filename not in version_dict:
        version_dict[filename] = []
    version_dict[filename].append(f"{filename}.{extension}: {version}")

# Prepare the email body
email_body = "Hi Cathy,\n\nThe following failed due to HK not versioning up:\n"
for filename, versions in version_dict.items():
    email_body += '\n'.join(versions) + "\n"

email_body += "\nThese files can be found in the Failed_FTP/20230802 folder\n"

print(email_body)
