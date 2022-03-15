# fastAPI backend-data-api-v2

This is the data access server for personicle.

To run this server:

- Add ```config.ini ``` in project root folder.

- Run the server: ``` uvicorn --port 8000 --host 127.0.0.1 main:app --reload ```

### Endpoints

#### /request
- Endpoint for datastreams. 

#### /request/events
- Endpoint for events. 
