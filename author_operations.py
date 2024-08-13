

class AuthorOperations:
    def __init__(self):
        self.authors = []

    def add_new_author(self, name, biography):
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f"Author '{name}' added successfully.")

    def view_author_details(self, name):
        for author in self.authors:
            if author.get_name() == name:
                print(f"Name: {author.get_name()}")
                print(f"Biography: {author.get_biography()}")
                return
        print("Author not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors found.")
            return
        for author in self.authors:
            print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_biography(self):
        return self.__biography

    def set_biography(self, biography):
        self.__biography = biography
