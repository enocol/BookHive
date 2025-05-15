<h1 align='center'> BookHive </h1>

BookHive is a Django-based web application and Minimum Viable Product (MVP) designed to showcase core full-stack functionality. The platform enables users to register, log in, browse books, post reviews, and initiate borrowing.

This project demonstrates my ability to build scalable, modular Django applications with clean UI using Bootstrap. While this version includes essential features, it is intentionally lean to highlight core functionality. The UX and feature set can be expanded based on future goals or user feedback.

## Index

- [User Experience](#user-experience-ux)
- [Features](#features)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Notes for testing](#Notes-for-testing)
- [Deployment](#deployment)
- [Future Features](#future-features)
- [Credits](#credits)

# 🧠 User Experience (UX)

## ✅ For General Users

As a regular user of **BookHive**, I want to:

- Access the website seamlessly across all devices — desktops, laptops, tablets, and smartphones.
- Navigate a clean, consistent, and responsive interface with intuitive menus and clear categories.
- Browse books by genre, title, or author with easy filtering and search functionality.
- View detailed information about each book, including title, author, cover image, description, and category.
- Register or log in quickly using an email address or a connected social media account (e.g., Google).
- Leave reviews for books and read others’ feedback to help with selection.
- Borrow books with clear instructions and receive confirmation or error messages as needed.
- Return to the homepage or previous browsing state without getting lost.
- Receive immediate visual feedback when submitting forms (e.g., sign-up, login, reviews).
- View a confirmation message or final state after each key action (e.g., successful borrow, review posted).
- Restart or return to the main book catalog at any point in the user journey.

## 🔧 For Admin Users

As an admin, I want to:

- Access a secure, user-friendly admin interface to manage users, books, and reviews.
- Add or update books with fields like title, author, description, category, and cover image.
- Moderate or delete user reviews if needed.
- View and manage borrowing activity across users (if implemented).
- Access the admin dashboard from a dedicated and protected URL.
- Receive clear validation messages when adding/editing book entries.
- Upload media (e.g., cover images) through a reliable integration (e.g., Cloudinary).

## ♿ Accessibility Considerations

- Use semantic HTML and proper heading structure for screen readers.
- Ensure adequate color contrast for text and interactive elements.
- Include `alt` text for all book cover images.
- Enable keyboard navigation for forms and buttons.
- Display clear error messages and form validation feedback.

---

## 📸 Screenshots

### 📚 Home Page (Book List)

![BookHive Home](screenshots/home.png)

### 🔍 Search Results

![Search Results](screenshots/search.png)

### 📘 Book Detail Page

![Book Detail](screenshots/book_detail.png)

### 🔐 Login Page

![Login Page](screenshots/login.png)

## 🚀 Features

- 🔍 Search for books by title
- 📝 User registration and login
- 💬 Review system for each book
- 📷 Book cover image upload using Cloudinary
- 🔐 login via `django-allauth`
- 📄 Pagination for book listings
- 🖼️ Responsive design using Bootstrap 5

---

### Fonts

## 🛠️ Tech Stack

- **Backend**: Django 5+
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: PostgreSQL (for production)
- **Media Storage**: Cloudinary
- **Authentication**: `django-allauth`

---

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/enocol/bookhive.git
   cd bookhive
   ```

🌐 Deployment
This app is ready for deployment on Heroku (with backend support).

Make sure to:

Set DEBUG=False

Configure allowed hosts

Use WhiteNoise or S3 for static/media files

Set up PostgreSQL in production

👤 Author
BookHive was created by Enoh Collins as a full-stack Django portfolio project.
Feel free to fork, star, and contribute!

📜 License
MIT License — see LICENSE file for details.
