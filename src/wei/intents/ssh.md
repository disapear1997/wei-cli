ls ~/.ssh
ssh-keygen -t ed25519 -C "你的 GitHub Email"
ssh -T git@github.com
git remote set-url origin git@github.com:disapear1997/wei-cli.git