
<!--
*** github_username, repo, twitter_handle, email
-->



<!-- PROJECT LOGO -->
<br />
<p align="center">


  <h3 align="center">StocksScrape</h3>

  <p align="center">
    Getting stock price data using a python script.
    <br />
    <a href="https://github.com/pylyf/stockscrape"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/pylyf/stockscrape/issues">Report Bug</a>
    ·
    <a href="https://github.com/pylyf/stockscrape/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

![example screenshot](https://github.com/pylyf/stockscrape/blob/master/screenshots/example.png)

A simple python script that parses the Open and Close price of a stock from the yahoo finance site and writes it in to a csv file.
Leave it running for many days and it will create a dataset.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Clone the repository on your machine.
```
git clone https://github.com/pylyf/stockscrape.git
```

### Installation
 
Install all required libraries in order to execute the script.
```
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage
```
python stockscrape.py
```

The script will ask you for a yahoo finance stock URL.
Go to this site https://finance.yahoo.com/ and find a stock you would like to scrape the price of.
Copy the url (ex. https://finance.yahoo.com/quote/NFLX?p=NFLX ) and paste it in the script.

Now leave the script running and wait till 22:00 ( the stock market closes at this time ) and the script will scrape the data and enter them in to a csv file.

## Tweaking
I use the schedule library to execute the scraping function at 22:00 because that is the time when the stock market closes (so we can get the close value).
You can edit this value to any day you want / or you can delete the scheduler and just scrape it immediately.
```
schedule.every().day.at("22:00").do(AutoScrape)
```

<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Your Name - Filip Komarek - pylyf.kom@gmail.com

Project Link: [https://github.com/pylyf/stockscrape](https://github.com/pylyf/stockscrape)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
