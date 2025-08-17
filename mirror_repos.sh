#!/bin/bash
# Multi-platform repository mirroring script

echo "🔄 UCP REPOSITORY MIRRORING"
echo "Creating mirrors across multiple platforms for anti-suppression"

# Add multiple remotes to the same local repository
echo "Adding remote repositories..."

# GitLab
git remote add gitlab https://gitlab.com/OscarLawrence/UCP.git
echo "✅ GitLab remote added"

# SourceForge  
git remote add sourceforge ssh://OscarLawrence@git.code.sf.net/p/ucp-protocol/code
echo "✅ SourceForge remote added"

# Bitbucket
git remote add bitbucket https://bitbucket.org/OscarLawrence/ucp.git  
echo "✅ Bitbucket remote added"

# Codeberg
git remote add codeberg https://codeberg.org/OscarLawrence/UCP.git
echo "✅ Codeberg remote added"

echo ""
echo "🚀 PUSH TO ALL PLATFORMS:"
echo "Execute these commands after creating repositories on each platform:"
echo ""
echo "git push gitlab main"
echo "git push sourceforge main" 
echo "git push bitbucket main"
echo "git push codeberg main"
echo ""
echo "📋 MANUAL SETUP REQUIRED:"
echo "1. Create repositories on each platform:"
echo "   - GitLab: https://gitlab.com/projects/new"
echo "   - SourceForge: https://sourceforge.net/projects/new/"
echo "   - Bitbucket: https://bitbucket.org/repo/create"
echo "   - Codeberg: https://codeberg.org/repo/create"
echo ""
echo "2. Set repository name: 'UCP' or 'ucp-protocol'"
echo "3. Make public, add MIT license, include README"
echo "4. Run push commands above"
echo ""
echo "🔐 ANTI-SUPPRESSION STRATEGY:"
echo "Multiple independent hosting = impossible to eliminate"
echo "Distributed redundancy = community preservation"