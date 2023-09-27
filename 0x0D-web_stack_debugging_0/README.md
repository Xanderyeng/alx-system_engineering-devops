<img src="https://s3.amazonaws.com/intranet-projects-files/concepts/68/OZeHN3D.png">

# 0x0D. Web stack debugging #0

Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.

Holberton specific
If you are struggling to get something right that is run on the checker, like a Bash script or a piece of code, keep in mind that you can simulate the flow by starting a Docker container with the distribution that is specified in the requirements and by running your code. Check the Docker concept page for more info.

Test and verify your assumptions
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

Is the web server started? - You can check using the service manager, also double check by checking process list.
On what port should it listen? - Check your web server configuration
Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
It is listening on the correct server IP? - netstat is also your friend here
Is there a firewall enabled?
Have you looked at logs? - usually in /var/log and tail -f is your friend
Can I connect to the HTTP port from the location I am browsing from? - curl is your friend
There is a good chance that at this point you will already have found part of the issue.

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

<a href="https://intranet.hbtn.io/concepts/33">`Network basics`</a><br>
<a href="https://intranet.hbtn.io/concepts/65">`Docker`</a><br>
<a href="https://intranet.hbtn.io/concepts/68">`Web stack debugging`</a><br>

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
