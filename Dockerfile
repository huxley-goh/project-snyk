# Use the official NGINX base image
FROM nginx:latest

# Remove the default NGINX index.html
RUN rm /usr/share/nginx/html/index.html

# Copy your custom index.html into the NGINX web root
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 for web traffic
EXPOSE 80

# Start NGINX in the foreground when the container runs
CMD ["nginx", "-g", "daemon off;"]