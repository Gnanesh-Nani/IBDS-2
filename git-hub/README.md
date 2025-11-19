```
# ============================
# 1. CREATE LOCAL REPOSITORY
# ============================
git init
git status
git add .
git commit -m "Initial commit"

# ============================
# 2. CONNECT REMOTE REPO
# ============================
git remote add origin https://github.com/USERNAME/REPO.git
git remote -v

# ============================
# 3. PUSH CODE
# ============================
git push -u origin main        # or use master if your branch is master
# Next pushes:
git push

# ============================
# 4. LOGIN TO GITHUB CLI
# ============================
gh auth login                   # Choose GitHub.com → HTTPS → Login with browser

# Or store credentials temporarily:
git config --global credential.helper store

# ============================
# 5. FIX 403 PERMISSION ERROR
# ============================

# A) Use Personal Access Token instead of password
# (Generate token: GitHub → Settings → Developer Settings → PAT → Tokens → Classic)

# B) Clear wrong/old credentials
git credential-manager reject  # Windows
git credential-cache exit      # Linux
rm ~/.git-credentials          # Linux/Mac

# C) Fix wrong remote URL
git remote -v
git remote set-url origin https://github.com/USERNAME/REPO.git

# D) If no permission → ask to be added as collaborator OR fork the repo
```