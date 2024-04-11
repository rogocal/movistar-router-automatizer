# Movistar Router Automatizer

This tool streamlines the process of refreshing the DNS settings on the Movistar ASKEY router, model RTF8115VW, automating a task that would otherwise require manual intervention.

## Introduction

The Movistar Router Automatizer script, powered by Python and Selenium, simplifies the task of updating DNS settings on the Movistar ASKEY router, specifically the model RTF8115VW. As of now, the script offers basic functionality, with potential for further enhancements based on user needs and feedback.

## Features

- Automates the process of refreshing DNS settings on the Movistar ASKEY router.
- Simplifies routine maintenance tasks, reducing manual effort and potential errors.
- Provides a foundation for additional features and improvements in future updates.

## Installation

Ensure you have the following dependencies installed:

```bash
sudo apt install python3-selenium python3-dotenv
```

## Usage

1. Clone the repository to your local machine.
2. Navigate to the directory containing the script.
3. Configure your environment variables using a .env file (see the example in this repo).
4. Open your terminal and edit your cron jobs using `crontab -e`.
5. Add the following line at the end of the file to schedule the script:

```bash
0 5 * * * python /home/user/router-automatizer/update.py
```

This example schedules the script to run every day at 5 AM. Adjust the timing according to your preferences and remember to replace `/home/user/router-automatizer/update.py` with the actual path to your script.

6. Save the changes and exit the editor.
7. Verify that your cron job has been successfully added, list your current cron jobs by running the following command

```bash
crontab -l
```

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License. Feel free to modify and distribute it as needed.

## Acknowledgements
Special thanks to the developers of Selenium and other open-source libraries used in this project.

## Disclaimer
This script is provided as-is, without any warranties or guarantees. Use it at your own risk.

## Contact
For any inquiries or support, please contact me via github.
