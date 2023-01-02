# Server Logo Updater
A script that updates the logo on your favorite media server: TwonkyMedia

## Installation
- The script works on a Linux environemnt, but it should also work on Windows
- Make sure you have a working TwonkyMedia server

  - If you want to change the logo in your own server, you can very easily implement a server class that inherits from `GenericServer`.

```bash
pip install -r requirements.txt
```

- Set the server credentials in the environment variables: `TWONKY_USERNAME` and `TWONKY_PASSWORD`

## Usage:

```bash
python3 main.py [-p PORT] <server_address> <filename>
```
