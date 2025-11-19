# Use official Node image
FROM node:18-alpine

# Create app directory
WORKDIR /usr/src/app

# Copy package files
COPY mynodeapp/package*.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application
COPY mynodeapp/ ./

# Expose port
EXPOSE 3000

# Start app
CMD ["node", "server.js"]
