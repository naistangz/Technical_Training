# Webservers

## Summary 
Can refer to hardware or software 
- On **hardware side**, a web server is a computer that stores web server software and a website's component files (e.g. HTML documents, images, CSS stylesheets, and JavaScript files)
- It is connected to the Internet and supports physical data interchange with other devices connected to the web.
- On the **software** side, a web server includes several parts that control how web users access hosted files, at minimum an HTTP server.
- An HTTP server is a piece of software that understands URLs (web addresses) and HTTP (the protocol your browser uses to view webpages). It can be accessed through the domain names (like `mozilla.org`) of websites it stores, and delivers their content to the end-user's device. 
- Can satisfy client requests on the World Wide Web
- They process incoming network requests over HTTP and other protocols.
- Primary function is to store, process and deliver web pages to clients. 

<img src='https://mdn.mozillademos.org/files/8659/web-server.svg' alt='http protocol img'>

Whenever a browser needs a file which is hosted on a web server, the browser requests the file via HTTP. When the request reaches the correct web server (hardware), the *HTTP* server (software) accepts request, finds the requested document (if it doesn't then a 404 response is returned), and send it back to the browser, also through HTTP.

# Nginx
```bash
$ sudo -i
root@ubuntu-xenial:
$ whoami
root
```

**Installing** `nginx`
1. Log into your (ve) Server via SSH as the root user
`ssh root@hostname`
`sudo -i`

2. Use apt-get to update your (ve) Server
`root@ubuntu-xenial:~# apt-get update`

3. Installing `nginx`
`root@ubunt-xenial:~# apt-get install nginx`
`service nginx start`

4. Test `nginx`
`sudo nginx -s reload`
**or**
`sudo service nginx reload`
**sudo systemctl status nginx.service**

