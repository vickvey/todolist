# Backend Task List

1. Set Up Project and App  
   - Create a new Django project. 
   - Create a new app named `core_api`.
   - Install and configure Django REST Framework (DRF).

2. Define Models
   - Create a `Task` model in `core_api` with fields like `title`, `description`, `completed`, and `created_at`.
   - Run migrations to create the database schema for the `Task` model.

3. Create Serializers
   - Create a serializer for the `Task` model to convert model instances to JSON and validate incoming data.

4. Set Up Views
   - Create API views or viewsets in `core_api` for CRUD operations (Create, Read, Update, Delete) on tasks.

5. Configure URLs
   - Define URL patterns in `core_api` to route API requests to the appropriate views or viewsets.
   - Set up endpoints for listing tasks, retrieving a specific task, creating a task, updating a task, and deleting a task.

6. Add Authentication and Permissions
   - Implement authentication (e.g., token-based) to secure the API.
   - Set permissions to ensure that only authenticated users can access the API endpoints.

7. Test the API
   - Write unit tests for your API endpoints to ensure they function correctly.
   - Use testing tools like Django’s test framework or Postman to manually test the API.

8. Document the API
   - Optionally, add API documentation using tools like `drf-yasg` or `Swagger` for easy reference and interaction with the API.
