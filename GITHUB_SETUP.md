# GitHub Setup Instructions

Follow these steps to push your repository to GitHub.

## 📋 Prerequisites

- [x] Git repository initialized locally ✓
- [x] Initial commit created ✓
- [ ] GitHub account (create at https://github.com/signup)
- [ ] Git configured with your name and email

## 🔧 Step 1: Configure Git (First Time Only)

If you haven't configured Git on your machine:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify configuration:
```bash
git config --global user.name
git config --global user.email
```

## 🌐 Step 2: Create a New Repository on GitHub

### Option A: Via GitHub Website
1. Go to https://github.com/new
2. Repository name: `call-center-workforce-planning` (or your choice)
3. Description: `Comprehensive toolkit for call center workforce planning using Erlang C, Square Root Staffing, and optimization techniques`
4. Choose: **Public** (recommended for open source) or **Private**
5. **Do NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### Option B: Via GitHub CLI (if installed)
```bash
gh repo create call-center-workforce-planning --public --source=. --remote=origin --description="Call center workforce planning toolkit"
```

## 🔗 Step 3: Link Your Local Repo to GitHub

After creating the GitHub repository, copy the repository URL and run:

```bash
# Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/call-center-workforce-planning.git

# Or if using SSH:
git remote add origin git@github.com:YOUR_USERNAME/call-center-workforce-planning.git
```

Verify the remote:
```bash
git remote -v
```

You should see:
```
origin  https://github.com/YOUR_USERNAME/call-center-workforce-planning.git (fetch)
origin  https://github.com/YOUR_USERNAME/call-center-workforce-planning.git (push)
```

## 🚀 Step 4: Push to GitHub

Push your code to GitHub:

```bash
git push -u origin main
```

The `-u` flag sets up tracking so future pushes can be done with just `git push`.

### If you encounter authentication issues:

**For HTTPS:**
- GitHub no longer accepts password authentication
- You need a Personal Access Token (PAT)
- Create one at: https://github.com/settings/tokens
- Use the token instead of your password when prompted

**For SSH:**
- Set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
- Use the SSH remote URL instead of HTTPS

## ✅ Step 5: Verify on GitHub

1. Go to your repository: `https://github.com/YOUR_USERNAME/call-center-workforce-planning`
2. You should see all your files
3. The README.md will be displayed automatically
4. Verify the commit message appears correctly

## 🎨 Step 6: Add Topics (Optional but Recommended)

On your GitHub repository page:
1. Click "About" (gear icon on the right)
2. Add topics: `call-center`, `workforce-planning`, `erlang-c`, `queueing-theory`, `excel`, `staffing`, `operations-research`
3. Add website/description if desired
4. Click "Save changes"

## 📊 Step 7: Enable GitHub Pages (Optional)

To create a website from your README:
1. Go to Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main`, folder: `/` (root)
4. Click Save
5. Your site will be at: `https://YOUR_USERNAME.github.io/call-center-workforce-planning/`

## 🔄 Making Future Updates

After making changes to your files:

```bash
# See what changed
git status

# Stage changes (all files)
git add -A

# Or stage specific files
git add filename.csv

# Commit with a descriptive message
git commit -m "Update: Improve k-value calibration formulas"

# Push to GitHub
git push
```

## 🌟 Best Practices

### Commit Message Format
```
Type: Brief description

- Detailed point 1
- Detailed point 2
```

**Types:**
- `Add:` New files or features
- `Update:` Changes to existing files
- `Fix:` Bug fixes
- `Docs:` Documentation only
- `Refactor:` Code restructuring
- `Test:` Adding tests

### Example Good Commit Messages
```bash
git commit -m "Add: Erlang X formulas for abandonment scenarios"
git commit -m "Update: Calibrate k-values based on real data"
git commit -m "Fix: Correct ASA formula in Excel guide"
git commit -m "Docs: Add tutorial for beginners"
```

## 🔍 Useful Git Commands

```bash
# View commit history
git log --oneline

# See what changed in files
git diff

# Undo uncommitted changes
git checkout -- filename

# Undo last commit (keep changes)
git reset --soft HEAD~1

# View remote repositories
git remote -v

# Pull latest changes from GitHub
git pull origin main
```

## 🐛 Troubleshooting

### "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/repo.git
```

### "! [rejected] main -> main (fetch first)"
Someone else pushed changes. Pull first:
```bash
git pull origin main --rebase
git push
```

### "Permission denied (publickey)"
Set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### Large file warning
GitHub has a 100MB file size limit. If you have large files:
```bash
# Remove from git
git rm --cached large_file.csv

# Add to .gitignore
echo "large_file.csv" >> .gitignore

# Commit the removal
git commit -m "Remove large file from tracking"
```

## 📱 GitHub Mobile App

For on-the-go updates:
- iOS: https://apps.apple.com/app/github/id1477376905
- Android: https://play.google.com/store/apps/details?id=com.github.android

## 🎓 Learning Resources

- [GitHub Docs](https://docs.github.com)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)

## ✨ Next Steps

1. Share your repository on social media (LinkedIn, Twitter)
2. Add collaborators in Settings → Collaborators
3. Enable Issues for community feedback
4. Consider adding GitHub Actions for automated testing
5. Star other relevant repositories for inspiration

---

**Your repository is ready to share with the world! 🎉**

Repository status:
- ✅ Git initialized
- ✅ Initial commit created
- ✅ 13 files ready to push
- ✅ Branch: main
- ⏳ Pending: Push to GitHub remote
