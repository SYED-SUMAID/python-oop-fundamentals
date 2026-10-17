# Simple Blog Management System
# Practising Python OOP concepts


# 1. Parent class
class Blog:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def show_blog(self):
        print(f"Title: {self.title}")
        print(f"Body: {self.body}")


# 2. Child class: Inheritance
class PublishedBlog(Blog):
    def __init__(self, title, body, author):
        super().__init__(title, body)
        self.author = author

    # 3. Method overriding
    def show_blog(self):
        super().show_blog()
        print(f"Author: {self.author}")
        print("Status: Published")


# 4. Another child class
class DraftBlog(Blog):
    def show_blog(self):
        super().show_blog()
        print("Status: Draft")


# 5. Create objects
blog1 = PublishedBlog(
    "Learning Python OOP",
    "Today I learned classes and inheritance.",
    "Sumaid"
)

blog2 = DraftBlog(
    "Learning FastAPI",
    "Today I started building APIs."
)


# 6. Display blog information
print("----- PUBLISHED BLOG -----")
blog1.show_blog()

print("\n----- DRAFT BLOG -----")
blog2.show_blog()