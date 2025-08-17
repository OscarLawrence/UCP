#!/bin/bash
# npm Package Deployment Script for UCP

echo "📦 Preparing npm package deployment..."

# Check if logged in to npm
echo "Checking npm authentication..."
npm whoami

if [ $? -ne 0 ]; then
    echo "❌ Not logged in to npm. Run 'npm login' first."
    exit 1
fi

echo "✅ npm authentication confirmed"

# Publish the package
echo "🚀 Publishing UCP to npm..."
npm publish

if [ $? -eq 0 ]; then
    echo "✅ UCP successfully published to npm"
    echo "📦 Install with: npm install ucp-protocol"
    echo "🔗 Package URL: https://www.npmjs.com/package/ucp-protocol"
else
    echo "❌ npm publish failed"
    echo "Common solutions:"
    echo "- Package name might be taken (check package.json)"
    echo "- Version might already exist (increment version)"
    echo "- Authentication issues (run 'npm login')"
fi