#!/bin/bash
# SSH Key Setup for UCP Multi-Platform Deployment

echo "🔑 UCP SSH KEY SETUP"
echo "Generating SSH keys for repository mirroring"

# Create .ssh directory if it doesn't exist
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# GitLab SSH Key
echo "Generating GitLab SSH key..."
ssh-keygen -t rsa -b 4096 -C "ucp-gitlab@vindao.org" -f ~/.ssh/ucp_gitlab -N ""
echo "✅ GitLab key generated: ~/.ssh/ucp_gitlab"

# Bitbucket SSH Key
echo "Generating Bitbucket SSH key..."
ssh-keygen -t rsa -b 4096 -C "ucp-bitbucket@vindao.org" -f ~/.ssh/ucp_bitbucket -N ""
echo "✅ Bitbucket key generated: ~/.ssh/ucp_bitbucket"

# Codeberg SSH Key
echo "Generating Codeberg SSH key..."
ssh-keygen -t rsa -b 4096 -C "ucp-codeberg@vindao.org" -f ~/.ssh/ucp_codeberg -N ""
echo "✅ Codeberg key generated: ~/.ssh/ucp_codeberg"

# SourceForge SSH Key
echo "Generating SourceForge SSH key..."
ssh-keygen -t rsa -b 4096 -C "ucp-sourceforge@vindao.org" -f ~/.ssh/ucp_sourceforge -N ""
echo "✅ SourceForge key generated: ~/.ssh/ucp_sourceforge"

echo ""
echo "📋 PUBLIC KEYS TO ADD TO PLATFORMS:"
echo ""

echo "=== GITLAB ==="
echo "Add this key to: https://gitlab.com/-/profile/keys"
cat ~/.ssh/ucp_gitlab.pub
echo ""

echo "=== BITBUCKET ==="
echo "Add this key to: https://bitbucket.org/account/settings/ssh-keys/"
cat ~/.ssh/ucp_bitbucket.pub
echo ""

echo "=== CODEBERG ==="
echo "Add this key to: https://codeberg.org/user/settings/keys"
cat ~/.ssh/ucp_codeberg.pub
echo ""

echo "=== SOURCEFORGE ==="
echo "Add this key to: https://sourceforge.net/auth/preferences/"
cat ~/.ssh/ucp_sourceforge.pub
echo ""

echo "🔧 SSH CONFIG SETUP:"
echo "Adding SSH configuration..."

# Create SSH config for different hosts
cat >> ~/.ssh/config << 'EOF'

# UCP Repository Mirroring
Host gitlab-ucp
    HostName gitlab.com
    User git
    IdentityFile ~/.ssh/ucp_gitlab
    IdentitiesOnly yes

Host bitbucket-ucp
    HostName bitbucket.org
    User git
    IdentityFile ~/.ssh/ucp_bitbucket
    IdentitiesOnly yes

Host codeberg-ucp
    HostName codeberg.org
    User git
    IdentityFile ~/.ssh/ucp_codeberg
    IdentitiesOnly yes

Host sourceforge-ucp
    HostName git.code.sf.net
    User OscarLawrence
    IdentityFile ~/.ssh/ucp_sourceforge
    IdentitiesOnly yes
EOF

echo "✅ SSH config updated"
echo ""
echo "🚀 AFTER ADDING KEYS TO PLATFORMS, RUN:"
echo "./deploy_mirrors.sh"