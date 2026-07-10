from playwright.sync_api import sync_playwright, expect

books = ["A Light in the ...", "Tipping the Velvet", "Soumission", "Sharp Objects", "Sapiens: A Brief History ..."]

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://books.toscrape.com/")

        all_books = page.locator("article.product_pod").all()
        print(f"Total books found: {len(all_books)}")

        with open("books.txt", "w", encoding="utf-8") as file:
            file.write("--- FIRST 5 BOOKS IN THE STORE ---\n\n")

            for i, book in enumerate(all_books[:5]):

                title = book.locator("h3")
                try:
                    expect(title).to_contain_text(books[i], ignore_case=True, timeout=1000)
                    price = book.locator("p.price_color").inner_text()

                    output_line = f"Book {i + 1}: {title.inner_text()} | Price: {price}"
                    print(f"✅ {output_line}")

                    file.write(output_line + "\n")
                except AssertionError:
                    print(f"❌ Book {i + 1}: Title {title.inner_text()} does not match expected value.")


        print("\n🚀 Success! Data written cleanly to 'books.txt'")
        browser.close()

if __name__ == "__main__":
    main()