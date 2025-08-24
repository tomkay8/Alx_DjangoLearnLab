# Deployment Configuration for HTTPS

To enable HTTPS in production:

1. Obtain SSL/TLS certificates (e.g., from Let's Encrypt).
2. Configure the web server (Nginx/Apache) to use the certificates.
   Example (Nginx):
server {
listen 443 ssl;
server_name example.com;

   ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
   ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

   location / {
       proxy_pass http://127.0.0.1:8000;
   }
}

3. Ensure Django security settings in `settings.py` are enabled:
- `SECURE_SSL_REDIRECT = True`
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`
- etc.

This enforces HTTPS and strengthens application security.
