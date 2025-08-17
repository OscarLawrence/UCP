#!/bin/bash
# Deploy UCP to all mirror repositories

echo "🚀 UCP MIRROR DEPLOYMENT"
echo "Deploying to all backup repositories"

# Update remotes with SSH config hosts
git remote remove gitlab 2>/dev/null || true
git remote remove bitbucket 2>/dev/null || true
git remote remove codeberg 2>/dev/null || true
git remote remove sourceforge 2>/dev/null || true

# Add remotes using SSH config
git remote add gitlab gitlab-ucp:OscarLawrence/ucp.git
git remote add bitbucket bitbucket-ucp:connection_love/ucp.git
git remote add codeberg codeberg-ucp:vindao/UCP.git
git remote add sourceforge ssh://OscarLawrence@sourceforge-ucp/p/ucp/code

echo "✅ Remotes configured"

# Test SSH connections
echo "🔍 Testing SSH connections..."

ssh -T gitlab-ucp 2>&1 | grep -q "Welcome to GitLab"
if [ $? -eq 0 ]; then
    echo "✅ GitLab connection successful"
else
    echo "❌ GitLab connection failed"
fi

ssh -T bitbucket-ucp 2>&1 | grep -q "authenticated via ssh key"
if [ $? -eq 0 ]; then
    echo "✅ Bitbucket connection successful"
else
    echo "❌ Bitbucket connection failed"
fi

ssh -T codeberg-ucp 2>&1 | grep -q "Hi there"
if [ $? -eq 0 ]; then
    echo "✅ Codeberg connection successful"
else
    echo "❌ Codeberg connection failed"
fi

echo ""
echo "🚀 DEPLOYING TO ALL MIRRORS..."

# Deploy to GitLab
echo "Pushing to GitLab..."
if git push gitlab main; then
    echo "✅ GitLab deployment successful"
else
    echo "❌ GitLab deployment failed"
fi

# Deploy to Bitbucket
echo "Pushing to Bitbucket..."
if git push bitbucket main; then
    echo "✅ Bitbucket deployment successful"
else
    echo "❌ Bitbucket deployment failed"
fi

# Deploy to Codeberg
echo "Pushing to Codeberg..."
if git push codeberg main; then
    echo "✅ Codeberg deployment successful"
else
    echo "❌ Codeberg deployment failed"
fi

# Deploy to SourceForge
echo "Pushing to SourceForge..."
if git push sourceforge main; then
    echo "✅ SourceForge deployment successful"
else
    echo "❌ SourceForge deployment failed"
fi

echo ""
echo "🎯 MIRROR DEPLOYMENT COMPLETE"
echo ""
echo "📍 UCP NOW AVAILABLE AT:"
echo "• GitHub: https://github.com/OscarLawrence/UCP"
echo "• GitLab: https://gitlab.com/OscarLawrence/ucp"
echo "• Bitbucket: https://bitbucket.org/connection_love/ucp"
echo "• Codeberg: https://codeberg.org/vindao/UCP"
echo "• SourceForge: https://sourceforge.net/projects/ucp/"
echo ""
echo "🛡️ ANTI-SUPPRESSION: MAXIMUM REDUNDANCY ACHIEVED"