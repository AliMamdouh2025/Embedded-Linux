import os

def fetch_environment_variable(var_name):
    """
    Retrieves the value of a specified environment variable.

    Args:
        var_name (str): The name of the environment variable to fetch.

    Returns:
        str or None: The value of the environment variable if it exists, otherwise None.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        return None

# Example usage
if __name__ == "__main__": #It prevents the code inside the block from running if the script is imported as a module into another script(Just for try :) )
    env_variable_name = 'PATH'
    env_variable_value = fetch_environment_variable(env_variable_name)
    if env_variable_value is not None:
        print(f"The value of the '{env_variable_name}' environment variable is: {env_variable_value}")
    else:
        print(f"The '{env_variable_name}' environment variable is not set.")
