<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201005T214356Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e38282225068b25c0f036f6e9f1086cf623d7a4bc02459c2ef5d330fe72ee7b7">

# Repository Title Goes Here

Despite the contrast implied by “application server vs. web server,” on the Internet the two types of server are usually deployed together for a common purpose: fulfilling user requests for content from a website. There are no standards documents that define the properties of web servers and application servers, but let’s look at how the terms are commonly understood.

A web server‘s fundamental job is to accept and fulfill requests from clients for static content from a website (HTML pages, files, images, video, and so on). The client is almost always a browser or mobile application and the request takes the form of a Hypertext Transfer Protocol (HTTP) message, as does the web server’s response.

An application server’s fundamental job is to provide its clients with access to what is commonly called business logic, which generates dynamic content; that is, it’s code that transforms data to provide the specialized functionality offered by a business, service, or application. An application server’s clients are often applications themselves, and can include web servers and other application servers. Communication between the application server and its clients might take the form of HTTP messages, but that is not required as it is for communication between web servers and their clients. Many other protocols are popular, including the variants of CGI.

How Do Application Servers and Web Servers Work Together?
In a typical deployment, a website that provides both static and dynamically generated content runs web servers for the static content and application servers to generate content dynamically. A reverse proxy and load balancer sit in front of one or more web servers and one or more web application servers to route traffic to the appropriate server, first based on the type of content requested and then based on the configured load-balancing algorithm. Most load balancer programs are also reverse proxy servers, which simplifies web application server architecture.

Why the Question?
Why is it a question whether something is an application server vs. a web server? It’s largely due to how the design and use of the two types of servers has increasingly come to overlap as the demands on websites have grown. Many popular applications act as both web servers and application servers (think Apache HTTP Server, Express, Hapi, and Koa).

Another overlap is that some web application servers use HTTP as their communication protocol. Similarly, some web servers end up looking like application servers because they have built-in modules and functionality that natively support popular languages like PHP, or proxy and translate requests from HTTP into the protocol (such as FastCGI) used by the application.



---

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [Support](#support)
- [License](#license)


---

## Installation

Copy the code, compile (if is necessary), and execute it.

---

### Setup

---

## Features
## Usage

See the codes of different functions and programs.

## Documentation

<a href="https://intranet.hbtn.io/rltoken/RerpYBxsgrpIorHjbDgulw">`Application server vs web server`</a><br>
<a href="https://intranet.hbtn.io/rltoken/uosy5QXdMbDPA1tFTR1eoA">`How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04'</a><br>
<a href="https://intranet.hbtn.io/rltoken/QTnnkj6vfQV9ovW_eYWWDQ">`Running Gunicorn`</a><br>
<a href="https://intranet.hbtn.io/rltoken/whE8do28ZiJJoJLyb1ACwA">`Be careful with the way Flask manages slash in route - strict_slashes`</a><br>
<a href="https://intranet.hbtn.io/rltoken/oQPs-o5UUcZkxOw5sNIM0g">`Upstart documentation`</a><br>

---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using.
---

## Team

https://github.com/Charliemur2
---

## Support

Feel free to contact me!

- GitHub at <a href="https://github.com/Charliemur2">`Charliemur2`</a>
- Twitter at <a href="https://twitter.com/charliesoka">`@charliesoka`</a>
- Insert more social links here.

---

## License

Free Source Code
