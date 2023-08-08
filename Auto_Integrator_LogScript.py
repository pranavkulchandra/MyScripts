def check_file_names_in_log(log_file, target_file_names_file):
    with open(log_file, 'r') as log_file:
        log_content = log_file.read()

    with open(target_file_names_file, 'r') as target_file_names_file:
        target_file_names = target_file_names_file.read().splitlines()

    found_file_names = []
    for target_file_name in target_file_names:
        if target_file_name in log_content:
            found_file_names.append(target_file_name)

    return found_file_names

log_file_path = "/Users/pranavjashma/Desktop/log.txt"
target_file_names_path = "/Users/pranavjashma/Desktop/files.txt"

found_file_names = check_file_names_in_log(log_file_path, target_file_names_path)

if found_file_names:
    print("The following file names are found in the log:")
    for file_name in found_file_names:
        print(file_name)
else:
    print("None of the target file names are found in the log.")
