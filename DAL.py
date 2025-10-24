import sqlite3
import os
from typing import List, Dict, Optional

class DatabaseAccessLayer:
    """Data Access Layer for managing projects in SQLite database."""
    
    def __init__(self, db_path: str = "projects.db"):
        """Initialize the DAL with database path."""
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database and create tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    image_filename TEXT NOT NULL,
                    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    
    def add_project(self, title: str, description: str, image_filename: str) -> bool:
        """
        Add a new project to the database.
        
        Args:
            title: Project title
            description: Project description
            image_filename: Name of the image file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO projects (title, description, image_filename)
                    VALUES (?, ?, ?)
                ''', (title, description, image_filename))
                conn.commit()
                return True
        except Exception as e:
            print(f"Error adding project: {e}")
            return False
    
    def get_all_projects(self) -> List[Dict]:
        """
        Retrieve all projects from the database.
        
        Returns:
            List[Dict]: List of project dictionaries
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row  # Enable column access by name
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM projects ORDER BY created_date DESC')
                projects = []
                for row in cursor.fetchall():
                    projects.append({
                        'id': row['id'],
                        'title': row['title'],
                        'description': row['description'],
                        'image_filename': row['image_filename'],
                        'created_date': row['created_date']
                    })
                return projects
        except Exception as e:
            print(f"Error retrieving projects: {e}")
            return []
    
    def get_project_by_id(self, project_id: int) -> Optional[Dict]:
        """
        Retrieve a specific project by ID.
        
        Args:
            project_id: The ID of the project to retrieve
            
        Returns:
            Optional[Dict]: Project dictionary if found, None otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
                row = cursor.fetchone()
                if row:
                    return {
                        'id': row['id'],
                        'title': row['title'],
                        'description': row['description'],
                        'image_filename': row['image_filename'],
                        'created_date': row['created_date']
                    }
                return None
        except Exception as e:
            print(f"Error retrieving project {project_id}: {e}")
            return None
    
    def delete_project(self, project_id: int) -> bool:
        """
        Delete a project from the database.
        
        Args:
            project_id: The ID of the project to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting project {project_id}: {e}")
            return False
    
    def update_project(self, project_id: int, title: str, description: str, image_filename: str) -> bool:
        """
        Update an existing project in the database.
        
        Args:
            project_id: The ID of the project to update
            title: New project title
            description: New project description
            image_filename: New image filename
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE projects 
                    SET title = ?, description = ?, image_filename = ?
                    WHERE id = ?
                ''', (title, description, image_filename, project_id))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating project {project_id}: {e}")
            return False
    
    def close_connection(self):
        """Close any open database connections."""
        # SQLite connections are automatically closed when they go out of scope
        # This method is included for completeness and future extensibility
        pass

# Create a global instance for use throughout the application
dal = DatabaseAccessLayer()
