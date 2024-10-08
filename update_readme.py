import os
import datetime

readme_file = "README.md"

now = datetime.datetime.now()

state_file = "last_state.txt"
if os.path.exists(state_file):
    with open(state_file, "r") as f:
        last_state = f.read().strip()
else:
    last_state = "minus"

if last_state == "minus":
    new_time = now + datetime.timedelta(minutes=1)
    new_state = "plus"
else:
    new_time = now - datetime.timedelta(minutes=1)
    new_state = "minus"

with open(state_file, "w") as f:
    f.write(new_state)

current_time = new_time.strftime("%Y-%m-%d %H:%M:%S")

update_message = f"\nREADME updated automatically on: {current_time} - Alternating between adding or subtracting a minute each day.\n"

with open(readme_file, "r") as file:
    readme_content = file.readlines()

updated_content = []
updated = False
for line in readme_content:
    if line.startswith("README updated automatically on"):
        updated_content.append(update_message)
        updated = True
    else:
        updated_content.append(line)

if not updated:
    updated_content.append(update_message)

with open(readme_file, "w") as file:
    file.writelines(updated_content)
