# Stage 1: Build the React app
# Use a Node.js image to build the React application
FROM node:18-alpine as builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY ./frontend/package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the frontend source code
COPY ./frontend .

# Build the React app for production
RUN npm run build

# Stage 2: Serve the static files with Nginx
# Use a lightweight Nginx image to serve the built files
FROM nginx:alpine

# Copy the built React app from the 'builder' stage to the Nginx web root directory
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 80 to the world outside this container
EXPOSE 80

# The default command to start Nginx
CMD ["nginx", "-g", "daemon off;"]

