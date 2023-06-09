def load_template(name):
    try:
        with open(f"templates/{name}.txt", "r") as file:
            return file.read()
    except Exception as exception:
        return str(exception)