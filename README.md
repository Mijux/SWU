
<br/>
<p align="center">
  <a href="https://github.com/Mijux/SWU">
    <img src="justseat.png" alt="Rocket Logo" width="250px" height="250px" style="border-radius: 50%;object-fit: contain;">
  </a>

  <h3 align="center">SWU</h3>

  <p align="center">
    SWU stands for Static Website Updater. It is a usefull script that update your website from github release. Take a seat and let's the magic ! ✨✨
    <br/>
    <br/>
    <a href="https://github.com/Mijux/SWU/issues">Report Bug</a>
    .
    <a href="https://github.com/Mijux/SWU/issues">Request Feature</a>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/Mijux/SWU?color=dark-green) ![Issues](https://img.shields.io/github/issues/Mijux/SWU) ![License](https://img.shields.io/github/license/Mijux/SWU) 

## About The Project

I really like Github Pages, because it allows me to have a small static site without having to worry about administering it. I've been using GoHugo, the static site generator, for some time now. 

Recently, I wanted to create a GoHugo website but I didn't want it to be accessible to everyone. So Github Pages isn't the solution. So I was looking for a solution that would still allow me to automate the process of publishing the site with Github Actions. 

That's where SWU comes from. After receiving a github webhook, it allows you to update your website locally.

## Built With

* [Python 🐍](https://www.python.org/)

## Getting Started

You will find the steps to setup the project

### Prerequisites

You will need the following assets:
- A personnal server where you can run python program and store you static website
- A github action that creates a release (you can create releases manually)
    - [Here](workflow.example.yaml) you can find an example of a github workflow to create release
    - When creating a release, you must set its tag as *latest*
- A github webhook that is triggered when a release a created on you repository
    - You will need setup a webhook secret
- A [Fine-grained personal access tokens](https://github.com/settings/tokens?type=beta) with at least those repository  permissions:
    - *Read-Only* on **Contents** 

### Installation

You have several choices:
1. Using docker
2. Install as systemd service
3. Run manually

#### Docker

1. Clone the repository
    ```bash
    git clone https://github.com/Mijux/SWU.git && cd SWU
    ```

2. Configure you .env
    ```bash
    cp .env.example .env
    # Then open it with you prefered editor to set the vars
    ```

3. Run
    ```bash
    docker compose up -d
    ```

#### Systemd service

1. Clone the repository
    ```bash
    git clone https://github.com/Mijux/SWU.git && cd SWU
    ```

2. Configure you .env
    ```bash
    cp .env.example .env
    # Then open it with you prefered editor to set the vars
    ```

3. Deploy service
    ```bash
    sudo bash deploy-systemd.sh
    ```

#### Manually

1. Clone the repository
    ```bash
    git clone https://github.com/Mijux/SWU.git && cd SWU
    ```

2. Configure you .env
    ```bash
    cp .env.example .env
    # Then open it with you prefered editor to set the vars
    ```

3. Create you virtual env
    ```bash
    python3 -m venv .venv
    .venv/bin/pip3 install -r requirements.txt
    ```

4. Run it
    ```bash
    .venv/bin/gunicorn --config gunicorn_config.py main:app
    ```

### Troubleshooting 

If you have error, it could a permission error, verify that SWU has the right to delete, create files in you WEB_ROOT. One possibility is to run SWU as www-data (if you WEB_ROOT is owned by www-data)

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/Mijux/SWU/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/Mijux/SWU/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/Mijux/SWU/blob/main/LICENSE) for more information.

## Authors

* **Mijux** - *Cybersec* - [Mijux](https://github.com/Mijux/) - *Maintainer*

## Acknowledgements

* [ImgShields](https://shields.io/)
* [Icons created by Hotpot](https://hotpot.ai/)
