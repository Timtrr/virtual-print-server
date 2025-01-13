# virtual-print-server
Этот код реализует сервер печати, который принимает данные по сети, сохраняет их во временный файл и отправляет на печать через указанный принтер.

# Printer Server

This project is a simple TCP-based print server designed to work with Windows printers, such as the Xprinter XP-365B. It listens for incoming connections, receives print jobs, and sends them to the configured printer.

## Features

- Receives print jobs via TCP/IP.
- Sends print jobs to a Windows-configured printer.
- Configuration file (`settings.ini`) for flexible printer settings.
- Automatically generates a default `settings.ini` file if it does not exist.

## Requirements

- Python 3.x
- Windows OS
- Required Python packages:
  - `pywin32`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Timtrr/printer-server.git
   cd printer-server
   ```

2. Install the required dependencies:
   ```bash
   pip install pywin32
   ```

3. Run the server:
   ```bash
   python printer_server.py
   ```

## Configuration

The printer server uses a configuration file named `settings.ini`. If the file is not found, it will be automatically created with default settings:

```ini
[Printer]
name = Xprinter XP-365B
```

You can edit the file to specify a different printer name as configured in your Windows printer settings.

## Usage

1. Start the server by running `printer_server.py`.
2. The server listens on `0.0.0.0:9100` by default.
3. Send print jobs to the server using any TCP client.
4. The server will process the data and send it to the configured printer.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes.

## Issues

If you encounter any issues or have suggestions for improvement, please open an issue in the repository.

