# 🐍 HNG Backend Wizards — Stage 0 Task

## 🚀 Task Overview
This is my Stage 0 task for the **HNG 13 Backend Wizards Track**.  
The goal is to create a simple REST API that returns:
- My profile information  
- A dynamically fetched cat fact from the [Cat Facts API](https://catfact.ninja/fact)  
- The current UTC timestamp in ISO 8601 format  

---

## 🧩 Endpoint Specification

**GET** `/me`  
Returns JSON response in the following format:

```json
{
  "status": "success",
  "user": {
    "email": "my.email@example.com",
    "name": "My Full Name",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-17T15:00:00.000Z",
  "fact": "Cats sleep for 70% of their lives."
}
