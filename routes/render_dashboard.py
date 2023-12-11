from bottle import get, template, response, request
import traceback
import x
import os


@get("/dashboard")
def show_tasks():
    try:
        db = x.db()  # Connect to your database
        
        user_cookie = x.user()
        user_cookie = request.get_cookie("user", secret=os.getenv('COOKIE_SECRET'))
        if not user_cookie:
            raise Exception("No cookie detected")
        # Fetch tasks from the database
        cursor = db.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.close()
        
        return template("dashboard", tasks=tasks, user_cookie=user_cookie)  # Pass tasks to your template for rendering
        
    except Exception as ex:
        response.status = 500  # Internal Server Error
        traceback.print_exc()  # Print the traceback for debugging
        return "An error occurred while fetching tasks."

    finally:
        if "db" in locals():
            db.close()