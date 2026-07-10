# Automation Practice Suite: Detailed Problem Statements

This document outlines the exact requirements, objectives, and constraints for each of the 5 progressive automation projects. Use these problem statements to build your automation scripts from scratch.

---

## 🔒 Project 1: The Secure Login Tester

### Objective
Automate a user login workflow, handle hidden character formatting issues, and validate the login state with graceful exception catching.

### Target Environment
`https://the-internet.herokuapp.com/login`

### Requirements
1. **Navigation:** Direct the browser to the target login page.
2. **Form Interaction:** Locate the username and password fields using unique CSS IDs. Input the credentials:
   * **Username:** `tomsmith`
   * **Password:** `SuperSecretPassword!`
3. **Execution:** Click the submit button to log into the application.
4. **State Verification:** * Locate the green alert banner component (`div.flash.success`).
   * Extract the text safely and verify that it contains the phrase `"You logged into a secure area!"`.
   * **Constraint:** Account for the hidden close button element (`×`) inside the banner without crashing the script.
5. **Error Handling:** Wrap the assertion check in a mechanism that handles failures gracefully. If an intentional text mismatch occurs (e.g., checking for `"Kemcho Majma"`), print a clean custom error message to the terminal instead of throwing a massive raw stack trace.

---

## 🔄 Project 2: The E-Commerce Dropdown Selector

### Objective
Interact with an HTML `<select>` dropdown menu to dynamically change application state and execute formal value assertions.

### Target Environment
`https://the-internet.herokuapp.com/dropdown`

### Requirements
1. **Navigation:** Open the dropdown testing page.
2. **Element Targeting:** Find the dropdown menu component utilizing its specific tag name and ID.
3. **State Manipulation:** Programmatically select `"Option 2"` from the menu options list.
4. **Validation:** * Assert that the active state of the element accurately updates to reflect the chosen option.
   * **Constraint:** Verify this using the underlying HTML `value` attribute assigned to Option 2 rather than just checking visible text.

---

## 📚 Project 3: The Book Scraper & File Saver

### Objective
Scrape an array of identical web components, safely handle sub-locators, and write the compiled data directly into a local storage file.

### Target Environment
`https://books.toscrape.com/`

### Requirements
1. **Navigation:** Go to the bookstore homepage.
2. **Collection:** Find all individual book containers on the screen and store them in a structural collection (array/list).
3. **Data Extraction & Loop:**
   * Run a loop through the **first 5 items** of the collection.
   * Inside each iteration, scope your selectors *only* to the current book box to avoid global element collisions.
   * Extract the **Title** text and the **Price** text.
4. **Verification & Constraints:** * Verify that the titles found on the webpage match a predefined expected local list of book strings.
   * **Constraint:** Ensure you pass the active Playwright element pointer to the validation engine, not a plain extracted string.
5. **Data Persistence:** Automatically create and write the successfully verified outputs cleanly into a new local file named `books.txt`.

---

## ⏳ Project 4: The Dynamic Element Waiter

### Objective
Handle non-static loading timelines safely using explicit waiting strategies rather than brute-force execution freezes.

### Target Environment
`https://the-internet.herokuapp.com/dynamic_loading/1`

### Requirements
1. **Navigation:** Load the dynamic rendering interface.
2. **Trigger Action:** Find and click the `"Start"` action button.
3. **Timing Synchronization:**
   * An animated loading bar will appear on the interface. 
   * **Constraint:** Do not use hardcoded processing pauses (`time.sleep()`).
   * Instruct the automation driver to explicitly poll the DOM until the loading state terminates and the final text wrapper becomes completely visible.
4. **Validation:** Grab the revealed text string and confirm it says `"Hello World!"`.

---

## 📡 Project 5: The Network API Interceptor

### Objective
Intercept and inspect background network traffic asynchronously to validate backend data consistency alongside frontend UI states.

### Target Environment
Any interactive web dashboard or public API-driven web interface.

### Requirements
1. **Listener Setup:** Before executing frontend interactions, register an event listener to capture background HTTP responses.
2. **Trigger Event:** Execute a UI action (such as loading a dashboard or clicking a search option) that forces the website to call an external database/microservice.
3. **Data Interception:** * Filter and catch the specific background network response that handles the data.
   * Extract its **HTTP Status Code** (e.g., `200 OK`) and its **Content-Type** headers.
4. **Payload Analysis:** Parse the raw response payload and verify that specific data properties inside match your testing expectations.