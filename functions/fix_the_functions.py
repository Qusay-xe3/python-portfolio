# fix_the_functions.py


def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)
#RuntimeError: The error lies in placing the `print_header` attribute before defining a function with the same name, rendering it undefined.
#The solution is to place it after the definition.
print_header()

def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    #SemanticError: The mistake is that the result was stored in a variable without being returned, so the function always returned 0.
    #The solution is to return the multiplication result directly.
    if failed >= 3:
      return failed * minutes
    else:
        return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"

#RuntimeError: The mistake is that he defined a new variable called user inside another variable.
#The solution is to delete only the new variable, and keep the value.
print(login_line("sara", failed=4))
#SemanticError: The mistake is that it called the function without printing it.
#The solution is to place (print) before it.
print(login_line("omar", 1))