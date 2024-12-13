# Autonity Piccadilly Tiber Challenge

GitHub repository for the Autonity Piccadilly Tiber Challenge.

For an overview of the Tiber Challenge tasks see the [TIBER_CHALLENGE_README.md](./TIBER_CHALLENGE_README.md).

This repo contains Starter Kit example code for the *Use-case Testing* activity of the Tiber Challenge.

To set up a validator node for *Oracle Calibration Testing* activity of the challenge see the Autonity GitHub repos for the main client [autonity](https://github.com/autonity/autonity) and oracle server [autonity-oracle](https://github.com/autonity/autonity-oracle).

## Starter Kit

Participants can earn points by running the script as-is, but in order to get
awarded with a higher score it is recommended to modify and optimize the code.

The example code has been written in Python using [v6.19.0 of the Web3.py
framework](https://web3py.readthedocs.io/en/v6.19.0/) and [v4.0.0 of the
autonity.py library](https://github.com/autonity/autonity.py/tree/v4.0.0) of Autonity
contract bindings.

The [`starter_kit.bindings`](./starter_kit/bindings/) module contains Python
bindings for the Uniswap V2 Factory and Uniswap V2 Router contracts.

### Getting Started

Pre-requisites:

- Install Nix with the [Determinate Nix Installer](https://zero-to-nix.com/concepts/nix-installer).
- Install [devenv](https://devenv.sh/getting-started/) using `nix profile install --accept-flake-config nixpkgs#devenv`.

Run the starter kit and optional linters:

1. Clone this repository.
2. Duplicate `.env.template` as `.env` and set the required environment variables.
    - `RPC_URL`: The URL of a Piccadilly (Tiber) Testnet RPC provider, please select
      one from [Chainlist](https://chainlist.org/?testnets=true&search=piccadilly).
    - `SENDER_PRIVATE_KEY`: The private key of the account that will sign and
      send the transactions.
    - `RECIPIENT_ADDRESS`: The address of an arbitrary account that tokens may
      be sent to.
3. Run `devenv shell` to enter a devenv shell.
4. In the devenv shell, run the script with `starter-kit`.
5. In the devenv shell, you can run linters with `lint-code`.

Note: the private key can be extracted from a Geth keyfile as a hex-string with
[autonity-cli](https://github.com/autonity/autonity-cli)'s `aut account
reveal-private-key` command.
