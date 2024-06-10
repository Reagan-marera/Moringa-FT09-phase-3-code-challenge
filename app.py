from models.author import Author
from models.magazine import Magazine
from models.article import Article

def add_author():
    name = input("Enter author name: ")
    author = Author(name)
    print(f"Author '{name}' added with ID {author.id}")

def add_magazine():
    name = input("Enter magazine name: ")
    category = input("Enter magazine category: ")
    magazine = Magazine(name, category)
    print(f"Magazine '{name}' added with ID {magazine.id}")

def add_article():
    author_id = int(input("Enter author ID: "))
    magazine_id = int(input("Enter magazine ID: "))
    title = input("Enter article title: ")

    author = Author.get_by_id(author_id)
    magazine = Magazine.get_by_id(magazine_id)

    if author and magazine:
        article = Article(author, magazine, title)
        print(f"Article '{title}' added with ID {article.id}")
    else:
        print("Invalid author or magazine ID")

def search_author_articles():
    author_id = int(input("Enter author ID: "))
    author = Author.get_by_id(author_id)
    if author:
        articles = author.articles()
        for article in articles:
            print(f"Article ID: {article[0]}, Title: {article[1]}")
    else:
        print("Author not found")

def search_magazine_articles():
    magazine_id = int(input("Enter magazine ID: "))
    magazine = Magazine.get_by_id(magazine_id)
    if magazine:
        articles = magazine.articles()
        for article in articles:
            print(f"Article ID: {article[0]}, Title: {article[1]}")
    else:
        print("Magazine not found")

def search_magazine_contributors():
    magazine_id = int(input("Enter magazine ID: "))
    magazine = Magazine.get_by_id(magazine_id)
    if magazine:
        contributors = magazine.contributors()
        for contributor in contributors:
            print(f"Author ID: {contributor[0]}, Name: {contributor[1]}")
    else:
        print("Magazine not found")

def main():
    while True:
        print("\nMenu:")
        print("1. Include new Author")
        print("2. Include new Magazine")
        print("3. Include new Article")
        print("4. Get Author's Articles")
        print("5. Get Magazine's Articles")
        print("6. Get Magazine's Contributors")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_author()
        elif choice == '2':
            add_magazine()
        elif choice == '3':
            add_article()
        elif choice == '4':
            search_author_articles()
        elif choice == '5':
            search_magazine_articles()
        elif choice == '6':
            search_magazine_contributors()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
