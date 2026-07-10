from playwright.sync_api import sync_playwright, expect

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

        button = page.locator("button")

        with page.expect_response("**/ajax-loader.gif") as response_info:
            button.click()

        response = response_info.value
        print(response)

        try:
            assert response.status == 200
            print("✅ Response status is 200")
        except AssertionError:
            print(f"❌ Response status is {response.status}")

        try:
            assert response.ok
            print("✅ Response is ok")
        except AssertionError:
            print(f"❌ Response is not ok: {response.ok}")

        try:
            assert response.url == "https://the-internet.herokuapp.com/img/ajax-loader.gif"
            print("✅ Response URL is correct")
        except AssertionError:
            print(f"❌ Response URL is incorrect: {response.url}")

        browser.close()

if __name__ == "__main__":
    main()