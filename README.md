
## Clone & Bootstrap

git clone https://github.com/wellnessatwork/waw-testcase-backend
make -C waw-contracts build

## Set Encryption Key
cp waw-identity/.env.example waw-identity/.env
export $(cat waw-identity/.env | xargs)

## Run local stack
make dev   # starts identity_srv, sync loop, backend mock


