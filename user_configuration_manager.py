def add_setting(dictionary, keyval):
    """Function to add a new setting to the user configuration."""
    key, value = (s.lower() for s in keyval)

    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary, keyval):
    """Function to update an existing setting in the user configuration."""
    key, value = (s.lower() for s in keyval)
    if key in dictionary:
        dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary, key):
    """Function to delete a setting from the user configuration."""
    key = key.lower()
    if key in dictionary:
        del dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dictionary):
    """Function to view all settings in the user configuration."""
    if not dictionary:
        return "No settings available."
    
    lines = ["Current User Settings:"]
    for key, value in dictionary.items():
        lines.append(f"{key.capitalize()}: {value}")
    
    return "\n".join(lines) + "\n"

test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high",
    "language": "en",
    "auto_save": True
}

print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(update_setting({'theme': 'light'}, ('theme', 'dark')))
print(update_setting({'theme': 'light'}, ('volume', 'high')))
print(delete_setting({'theme': 'light'}, 'theme'))
print(delete_setting({'theme': 'light'}, 'type'))
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
