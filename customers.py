"""Customers at Hackbright."""

class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    def __init__(self, first_name, last_name, email, password):
        """Initialize a customer class."""


        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "Customer: {} {}, {}".format(self.first_name, self.last_name, self.email)


def make_email_dict():
    """Make dictionary with emails as keys and customers as values."""
    the_file = open("customers.txt")

    email_dict = {}  # make empty dictionary

    for line in the_file:
        new_line = line.rstrip()
        new_list = new_line.split("|")
        email_dict[new_list[2]] = Customer(*new_list)

    return email_dict


def get_by_email(email_address):
    """Given an email address, returns corresponding Customer object."""

    email_dict = make_email_dict()

    if email_dict.get(email_address):
        return email_dict[email_address]

