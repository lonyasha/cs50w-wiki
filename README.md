# Wiki

**Wiki** is a simple Wikipedia-like online encyclopedia created as part of **[CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/)** course.  It allows users to view, create, edit, search, and navigate through encyclopedia entries. Entries are stored in Markdown format and are converted to HTML for rendering.

## Features

- **Entry Pages**: View individual entries by visiting `/wiki/TITLE`.
- **Index Page**: Displays a list of all encyclopedia entries with clickable titles.
- **Search**: Search for entries by name or substring.
- **Create New Page**: Users can create new encyclopedia entries using Markdown content.
- **Edit Pages**: Edit existing entries with pre-populated Markdown content.
- **Random Page**: Navigate to a random encyclopedia entry.
- **Markdown to HTML Conversion**: Converts Markdown content into HTML for rendering.

## Technologies Used 
- **Django**  
- **HTML/CSS**  
- **Markdown** 

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
