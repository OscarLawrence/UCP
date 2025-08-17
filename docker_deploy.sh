#!/bin/bash
# Docker Hub Deployment Script for UCP

echo "🐳 Building UCP Docker Image..."

# Build the image
docker build -t oscarlawrence/ucp:latest .
docker build -t oscarlawrence/ucp:v1.0.0 .

echo "✅ Images built successfully"

# Login to Docker Hub (you'll need to run: docker login)
echo "📦 Ready to push to Docker Hub"
echo "Run these commands after 'docker login':"
echo ""
echo "docker push oscarlawrence/ucp:latest"
echo "docker push oscarlawrence/ucp:v1.0.0"
echo ""
echo "Test the deployed image with:"
echo "docker run --rm oscarlawrence/ucp:latest"