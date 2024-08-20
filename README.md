# FastAPI 101

### Project Structure
```
fastapi-101/
│
├── src/
│   ├── main.py
│   │
│   └── api_v1/
│       ├── __init__.py
│       ├── api.py
│       └── endpoints/
│           ├── __init__.py
│           ├── auth.py
│           ├── models.py
│           └── ai_function.py
│
├── requirements.txt
│
├── dockerfile
│
├── docker-compose.yml
│
└── README.md
```

### Deployment
1. Build docker image
```bash
bash docker_build.sh
```

2. Deploy your service
```bash
docker-compose up -d
```

3. Firewall configuration

- Open port 8888 (not safe)

4. Nginx reverse proxy configuration

- Open port 80, 443

- Use your domain / subdomain

- Create a file named with your domain, put it under `/etc/nginx/sites-available/`
```nano
// yourdomain.com

server {

    server_name yourdomain.com www.yourdomain.com;
        
    location / {
        proxy_pass http://127.0.0.1:8888;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }

}
```

- Create a soft link under `/etc/nginx/sites-enabled/`
```bash
sudo ln -s /etc/nginx/sites-available/yourdomain.com /etc/nginx/sites-enabled/
```

- Test and restart Nginx to make it work

```bash
sudo nginx -t
sudo service nginx restart
```

- Then you can enter `http://<your-ip>:8888/docs` to view the API Docs


### Add API Token

For security, users should authorized to call your API.

