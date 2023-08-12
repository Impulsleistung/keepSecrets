# keepSecrets
A quick demonstration of handling confidential data within a public repository. This is the most easiest and a secure way of using GPG within Github


# On my personal computer
## Encrypting

```bash
gpg --symmetric --cipher-algo AES256 --batch --passphrase-file pass.txt confidential.json
```

## Decrypting

```bash
gpg --quiet --batch --yes --decrypt --passphrase-file pass.txt --output decrypted_file.json confidential.json.gpg
```

# In GitHub

```bash
gpg --quiet --batch --yes --decrypt --passphrase="$PASSPHRASE" --output $HOME/decrypted_file.json confidential.json.gpg
```