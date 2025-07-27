AUTH_USER_MODEL = 'relationship_app.CustomUser'  # or your app name

# SECURITY: Force HTTPS Redirect
SECURE_SSL_REDIRECT = True

# SECURITY: HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# SECURITY: Cookies over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# SECURITY: HTTP Headers
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# SECURITY: Turn off debug in production
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']  # Update with your production domain
