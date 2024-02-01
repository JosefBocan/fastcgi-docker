docker run -p 9000:9000 -d shipmonkdevops/shipmonk-test
REQUEST_METHOD=GET SERVER_PROTOCOL=HTTP/1.1 cgi-fcgi -bind -connect localhost:9000