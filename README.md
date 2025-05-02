#Clone & Bootstrap
git clone https://github.com/<org>/lumina-contracts.git
make -C lumina-contracts build

#Set Encryption Key
cp lumina-identity/.env.example lumina-identity/.env
export $(cat lumina-identity/.env | xargs)

#Run local stack
make dev   # starts identity_srv, sync loop, backend mock


