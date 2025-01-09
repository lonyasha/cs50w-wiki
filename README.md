# Wiki

**Wiki** is a simple Wikipedia-like online encyclopedia created as part of **[CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/)** course.  It allows users to view, create, edit, search, and navigate through encyclopedia entries. Entries are stored in Markdown format and are converted to HTML for rendering.

## About the Project

In this project, I built a basic online encyclopedia with the following features:

- **Viewing Entries**: Users can visit an entry page and see the content of an encyclopedia entry.
- **Searching**: Users can search for entries by title or by keywords, displaying relevant results.
- **Creating Entries**: Users can create new encyclopedia entries, writing content in Markdown format.
- **Editing Entries**: Users can edit existing entries and save the changes.
- **Random Entry**: Users can view a random entry from the encyclopedia.
- **Markdown to HTML Conversion**: Each entry is written in Markdown, which is converted to HTML when displayed.

The project uses Django for backend development, ensuring smooth functionality for user interactions and data management.

## Features

- **View Entries**: Browse through existing encyclopedia entries by visiting their unique URL.
- **Search**: Search for entries by title or by keywords within the content.
- **Create New Entry**: Create a new entry by entering a title and content in Markdown format.
- **Edit Entries**: Modify the content of existing entries using a Markdown editor.
- **Random Entry**: Click a button to view a random article from the encyclopedia.
- **Markdown Rendering**: Markdown content is automatically converted into HTML for proper display.

## Technologies Used

- **Python**
- **Django**
- **HTML/CSS**
- **Markdown (for entry content)**
- **SQLite** (for database storage)

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lonyasha/cs50w-wiki.git
2. **Navigate into the project directory**:
   ```bash
   cd cs50w-wiki
3. **Create a virtual environment**:
      ```bash
      python3 -m venv venv
4. **Activate the virtual environment**:
   - For **Windows**:
     ```bash
     venv\Scripts\activate
   - For **MacOS/Linux**:
     ```bash
     source venv/bin/activate
5. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
6. **Run the server**:
   ```bash
   python manage.py runserver

### Key Points:
- All installation and setup instructions are placed in properly formatted code blocks.
- This allows for easy copying and pasting directly into the terminal.

---

This project is a part of **[CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/)** course by Harvard University. The course provided a comprehensive introduction to web development, and this project was designed to showcase the skills learned throughout the course.

Thank you for visiting! 🎉
