# Task Manager Web Application
#### Video Demo:  [ReadMe](https://www.youtube.com/watch?v=OYSPtjAF0Gw)
#### Description:

## Introduction
The Task Manager web application is designed to help users manage their tasks effectively through a simple and intuitive interface. This README.md provides an overview of the project, its features, setup instructions, and future enhancements.

## Features
### User Authentication
The application supports user registration and login functionalities. Users can securely create an account with a unique username and password. Passwords are hashed using SHA-256 for security.

### Task Management
Once logged in, users can perform various actions related to task management:
- **Add Tasks:** Users can add tasks with titles and optional descriptions.
- **View Tasks:** Tasks are displayed in a list format, showing the title and description. Each task can be managed individually.
- **Delete Tasks:** Users can delete tasks they no longer need, ensuring their task list stays organized.

### Responsive UI Design
The user interface (UI) is designed to be responsive, adapting to different screen sizes and devices. This ensures a seamless user experience whether accessed from a desktop, tablet, or mobile phone.

### Flash Messages
The application provides informative flash messages to users, notifying them of important events such as successful logins, registration, task additions, and errors (e.g., incorrect login credentials).

### Database Integration
The application uses SQLite as its database backend, facilitating efficient storage and retrieval of user data (e.g., usernames, hashed passwords) and task information (e.g., task titles, descriptions).

### Error Handling
Comprehensive error handling ensures that users receive clear and actionable feedback in case of invalid inputs, database errors, or other issues encountered during their interaction with the application.

## Setup Instructions
To run the Task Manager web application locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/task_manager.git
   cd task_manager
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database:**
   ```bash
   python -c 'from app import init_db; init_db()'
   ```

5. **Run the Application:**
   ```bash
   flask run
   ```

6. **Access the Application:**
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Future Enhancements
While the current version of the Task Manager web application offers essential functionalities for task management, there are several potential enhancements for future iterations:

- **Task Editing:** Allow users to edit existing tasks to update titles, descriptions, or other details.
- **Task Filtering and Sorting:** Implement features to filter tasks based on categories, due dates, or priority levels. Allow sorting tasks by different criteria (e.g., alphabetical order, creation date).
- **User Profile Management:** Enable users to manage their profiles, including changing passwords, updating personal information, and viewing past activities.
- **Email Notifications:** Implement email notifications to remind users of upcoming task deadlines or important updates related to their tasks.
- **Data Visualization:** Introduce graphical representations (e.g., charts, graphs) to visualize task completion rates, productivity trends, or other insightful metrics.

## Conclusion
The Task Manager web application provides a foundational platform for users to efficiently manage their tasks online. Built using Flask, SQLite, and JavaScript, it demonstrates core concepts of web development including user authentication, database integration, and responsive design. Whether for personal use or team collaboration, this application serves as a practical tool for organizing tasks and enhancing productivity.

For further inquiries or contributions, please contact Devinder at iamDevinderSharma15122005@gmail.com.

