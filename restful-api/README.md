# RESTful API

**Novice**

**By: Javier Valenzani**

## Description

This project delves into the domain of RESTful APIs, a cornerstone in the realm of web services. The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

## Learning Objectives:

*   **HTTP/HTTPS Basics:** Grasp the foundational principles of the web’s primary protocol, understanding how data transfer occurs, methods involved, and the difference between the secure and non-secure versions.
*   **API Consumption with Command Line:** Hands-on experience in interacting with APIs using basic command-line tools, laying the groundwork for more advanced interactions.
*   **API Consumption with Python:** Elevate your data fetching skills by leveraging Python’s capabilities, allowing for more advanced processing and data manipulation.
*   **API Development with `http.server`:** Understand the basics of crafting an API from scratch using Python’s built-in modules, setting a solid foundation.
*   **API Development with Flask:** Dive deeper into API development using the lightweight Flask framework, focusing on routing, data management, and scalability.
*   **API Security & Authentication:** Address the crucial aspect of security, understanding how to protect data transfer and ensure only authorized access to resources.
*   **API Standards & Documentation with OpenAPI:** Conclude with the importance of maintaining standardized documentation, ensuring that APIs are usable, understandable, and maintainable.

## Importance:

In our interconnected digital age, RESTful APIs play a pivotal role in the integration of different systems. They serve as the middlemen, translating requests into understandable actions, fetching data, or triggering procedures. From social media platforms sharing data with advertisement agencies to complex industrial systems communicating with each other for automation, APIs are ubiquitous.

Developing a solid understanding of how to consume, develop, secure, and document these APIs equips you with a critical skill set. It’s a blend of understanding both the technical intricacies and the larger design picture, ensuring seamless and efficient communication in the digital world.

## REST API Conceptual Diagram:

+-------+ +-------+ +---------+ +---------+
| | Request | | Process | | Fetch/ | |
| | -----> | | -------> | | Modify | |
| | | | | | -------> | |
| | <----- | | <------- | | | |
| | Response | | Return | | | |
+-------+ +-------+ +---------+ +---------+
Client Web Server API Server Database


**Components:**

*   **Client:** The requester of the service, often a web browser or application.
*   **Web Server:** Handles the incoming request, acts as a middleman before passing it to the API server.
*   **API Server:** The actual logic layer that processes the request, determining what data or action is required.
*   **Database:** Stores the data which the API might fetch or modify.

**Flow:**

1.  The client sends an HTTP/HTTPS request to the Web Server.
2.  The Web Server, after potential routing and load balancing, forwards the request to the API Server.
3.  The API Server processes the request, interacts with the database if needed.
4.  The API Server returns the processed response to the Web Server.
5.  The Web Server sends back the final HTTP/HTTPS response to the client.

*This diagram provides a high-level view of how RESTful API communication typically works. In simpler setups, the Web Server and API Server might be combined into one. The separation here illustrates potential layers in a more complex or scaled environment.*

## Tasks

### 0. Basics of HTTP/HTTPS (Mandatory)

*   **Score:** 0.00% (Checks completed: 0.00%)
*   **Background:**
    The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows web clients (like browsers) to communicate with web servers. HTTP has evolved over time and has a secure counterpart called HTTPS (HTTP Secure). HTTPS is just like HTTP but with an added layer of security using SSL/TLS encryption. This layer protects the data from eavesdroppers and tampering.

*   **Objective:**

    *   Differentiate between HTTP and HTTPS.
    *   Understand the basic working and structure of HTTP requests and responses.
    *   Recognize and explain the common HTTP methods and status codes.
*   **Resources:**
    *   [Mozilla Developer Network (MDN) - An Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
    *   [Difference between HTTP and HTTPS](https://www.cloudflare.com/learning/ssl/http-vs-https/)
    *   [List of HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

*   **Instructions:**

    *   **Differentiating HTTP and HTTPS:**
        *   Read the provided resources to understand the basic differences between HTTP and HTTPS.
        *   Jot down the main differences, focusing on security aspects.
        *   *Optional*: Use a packet sniffer tool like Wireshark to observe the traffic of an HTTP and an HTTPS request (Make sure you have the appropriate permissions).
    *   **Understanding HTTP Structure:**

        *   Visit a simple website, right-click, and choose “Inspect” or “Inspect Element”. Navigate to the “Network” tab. This shows all network requests made by the page.
        *   Reload the page and observe the first request. Click on it. Explore the “Headers” section to understand the structure of HTTP requests and responses. You’ll see methods, paths, status codes, headers, and more.
    *   **Exploring HTTP Methods and Status Codes:**
        *   Based on the resources provided, make a list of at least four common HTTP methods and explain when each would be used.
        *   Make another list of five common HTTP status codes. For each status code, provide a brief description and a scenario where it might be encountered.
*   **Hints:**

    *   HTTP does not encrypt its data, which means that anyone eavesdropping on the communication can see the content. HTTPS adds a layer of encryption, making the content unintelligible to eavesdroppers.
    *   The “s” in “https” stands for “secure”. Websites, especially those that handle sensitive data like banking websites or email providers, typically use HTTPS.
    *   Each HTTP status code has a specific purpose. They are grouped by their first digit: 1xx (informational), 2xx (successful), 3xx (redirection), 4xx (client errors), and 5xx (server errors).

*   **Expected Output:**

    *   A brief summary explaining the differences between HTTP and HTTPS.
    *   A depiction or outline of the structure of an HTTP request and response.
    *   Lists of common HTTP methods and status codes with their descriptions and possible use cases. For example:

        *   Method: GET, Description: Retrieves data, Use case: Fetching a web page or data from an API.
        *   Status Code: 404, Description: Not Found, Scenario: When a requested page or resource isn’t available on the server.

### 1. Consume data from an API using command line tools (curl) (Mandatory)

*   **Score:** 0.00% (Checks completed: 0.00%)
*   **Background:**
    `curl` (Client URL) is a command-line tool that allows users to transfer data to or from a network server, using one of the supported protocols (HTTP, HTTPS, FTP, and more). It’s widely used for debugging, testing, and interacting with RESTful web services and APIs. By mastering `curl`, one can quickly prototype API requests, diagnose server issues, and more, all from the command line.

*   **Objective:**

    *   Install and use `curl` from the command line.
    *   Construct and execute basic API requests using `curl`, including setting headers and inspecting the output.
    *   Interpret the results of common API requests.
*   **Resources:**
    *   [`curl` - Everything `curl`](https://everything.curl.dev/)
    *   [Using cURL to interact with HTTP APIs](https://medium.com/@rmorgenstern/using-curl-to-interact-with-http-apis-a-practical-guide-b39b37904c04)
    *   [Public API to play with: JSONPlaceholder](https://jsonplaceholder.typicode.com/)
*   **Instructions:**

    *   **Installing and Basic Interaction with `curl`:**
        *   Install `curl` on your system. It’s usually available in standard repositories for Linux/Mac systems. For Windows, consider using Windows Subsystem for Linux (WSL) or downloading a Windows version of `curl`.
        *   Once installed, run `curl --version` to confirm its availability.
        *   Use `curl` to fetch the content of a webpage. For instance: `curl http://example.com`.
    *   **Fetching Data from an API:**
        *   Use `curl` to retrieve posts from JSONPlaceholder: `curl https://jsonplaceholder.typicode.com/posts`
        *   Observe the output. It should be a JSON array of posts.
    *   **Using Headers and Other Options with `curl`:**
        *   Fetch only the headers of the same request using `curl -I https://jsonplaceholder.typicode.com/posts`.
        *   Use `curl` to make a POST request to the same API: `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`
*   **Hints:**
    *   The `-I` flag in `curl` fetches only the headers of the response, which can be useful to diagnose server settings, cache controls, content type, and more.
    *   With the `-X` flag, you can specify an HTTP method for your request. For example, `-X POST` will make a POST request.
    *   The `-d` flag allows you to pass data in your request. In RESTful APIs, this is commonly used with POST, PUT, or PATCH requests to send data to the server.
    *   If you’re getting a lot of output and want to view it in a more organized way, consider piping the output to a tool like `jq` for JSON formatting and highlighting.
*   **Expected Output:**
    *   Upon running `curl --version`, you should see details about your installed version of `curl`, including supported protocols.
    *   Fetching posts from JSONPlaceholder should provide a JSON output of various posts, each having attributes like `userId`, `id`, `title`, and `body`.
    *   Fetching only headers should give a concise output showing status codes and headers without the actual content.
    *   Making a POST request should yield a response from the server acknowledging the reception of the data. For JSONPlaceholder, it typically returns the created post with an id of 101 (since it doesn’t actually save the new post, but simulates the creation).

### 2. Consuming and processing data from an API using Python (Mandatory)

*   **Score:** 100.00% (Checks completed: 100.00%)
*   **Background:**
    Python, due to its readability and a vast library ecosystem, is a popular choice for interacting with web services and APIs. The `requests` library simplifies HTTP communication and allows users to send HTTP requests using Python. Once the data is fetched, Python’s built-in libraries and tools enable effortless data manipulation and processing.
*   **Objective:**
    *   Utilize the `requests` library to send HTTP requests and process responses.
    *   Parse and manipulate JSON data using Python.
    *   Convert structured data into other formats, e.g., CSV.
*   **Resources:**
    *   [Python Requests Library](https://docs.python-requests.org/en/latest/)
    *   [Working with JSON data in Python](https://realpython.com/python-json/)
    *   [Public API to experiment with: JSONPlaceholder](https://jsonplaceholder.typicode.com/)
*   **Instructions:**
    1.  If not installed, install the `requests` library using pip: `pip install requests`.
    2.  Write a basic Python script to fetch posts from JSONPlaceholder using `requests.get()`.
    3.  Create a function `fetch_and_print_posts()` that fetches all post from JSONPlaceholder.
        *   Print the status code of the response i.e. `Status Code: 200`
        *   If the request was sucessfull, parse the fetched data into a JSON object using the `.json()` method of the response object.
        *   Iterate through the parsed JSON data and print out the titles of all the posts.
    4.  Create a function `fetch_and_save_posts()` that fetches all post from JSONPlaceholder.
        *   If the request was sucessfull, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for `id`, `title`, and `body`.
        *   Using Python’s `csv` module, write this data into a CSV file called `posts.csv` with columns corresponding to the dictionary keys.

from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

fetch_and_print_posts()
fetch_and_save_posts()


*   **Expected Output:**

    *   After the basic interaction script, you should have an output indicating a 200 status code, suggesting a successful GET request.
    *   When parsing JSON data, you should see printed titles of the posts, e.g., “sunt aut facere repellat provident occaecati excepturi optio reprehenderit.”
    *   After the data manipulation and conversion task, you should have a CSV file with columns `id`, `title`, and `body`. Each row in the CSV should correspond to a post from the fetched data.

### 3. Develop a simple API using Python with the `http.server` module (Mandatory)

*   **Score:** 100.00% (Checks completed: 100.00%)
*   **Background:**

    The `http.server` module in Python’s standard library provides basic classes for implementing web servers. While it’s not typically used for production applications, it’s a handy tool for building simple web servers and understanding the basics of web programming without relying on third-party libraries.
*   **Objective:**

    *   Set up a basic web server using the `http.server` module.
    *   Handle different types of HTTP requests (GET, POST, etc.).
    *   Serve JSON data in response to specific endpoints.
*   **Resources:**

    *   [Python docs: http.server — HTTP servers](https://docs.python.org/3/library/http.server.html)
    *   [A simple example of using Python’s http.server](https://pythonprogramming.net/basic-http-server-example-python-3/)
*   **Instructions:**

    *   **Setting Up a Basic HTTP Server:**
        *   Use the `http.server` module to set up a simple HTTP server. Start by creating a subclass of `http.server.BaseHTTPRequestHandler`.
        *   Implement the `do_GET` method to handle GET requests. Within this method, send a simple text response back to the client: “Hello, this is a simple API!”.
        *   Start the server on a specific port (8000) and test it by visiting `http://localhost:8000` in your browser or using curl.
    *   **Serving JSON Data:**
        *   Modify the `do_GET` method in your server class to serve a sample JSON data when the endpoint `/data` is accessed.
        *   You should return a simple dataset: `{"name": "John", "age": 30, "city": "New York"}`.
        *   Ensure that the correct content type (`application/json`) header is set in the response.
    *   **Handling Different Endpoints:**

        *   Add an `/status` endpoint to check the API status. It shoud return `OK`.
        *   Implement error handling. If the user tries to access an undefined endpoint, return a `404 Not Found` status with an appropriate message.

## General Requirements

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle style (version 2.7.*)
*   All your files must be executable
*   The length of your files will be checked using `wc`

## Python Test Cases Requirements

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files should end with a new line
*   All your test files should be inside a folder `tests`
*   All your test files should be text files (extension `.txt`)
*   All your tests should be well explained
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length doesn’t matter)
*   To test your code, you should not use `from my_module import *`

## Installation

1.  Clone this repository:

    ```
    git clone <repository_url>
    ```
2.  Navigate to the project directory:

    ```
    cd <project_directory>
    ```
3.  Install the necessary requirements.  It is recommended to use a virtual environment.

    ```
    pip install -r requirements.txt
    ```

## Usage

Refer to the instructions within each task's directory for specific usage examples.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


