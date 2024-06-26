
<br/>
<p align="center">
  <a href="https://github.com/Mijux/SWU">
    <img src="justseat.png" alt="Rocket Logo" width="250px" height="250px"/>
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
    - Refer to the [official Github documentaion](https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks) for more details on creating a webhook
    - Make sure to set the `Content type` to `application/json`
    - In the "Which events would you like to trigger this webhook?" section, select "Let me select individual events."
    - Ensure you check at least the "**Release**" event
- A [Fine-grained personal access tokens](https://github.com/settings/tokens?type=beta) with at least those repository  permissions:
    - *Read-Only* on **Contents** 

### Installation

You have several choices:
1. Using docker
2. Install as systemd service
3. Run manually

In all cases, clone or download the repository:

```bash
git clone https://github.com/Mijux/SWU.git
```

Or using cURL:

```bash
curl -L https://github.com/Mijux/SWU/archive/main.tar.gz -o SWU.tar.gz
tar xzf SWU.tar.gz
rm SWU.tar.gz
mv SWU-main SWU
```

Navigate to the folder:

```bash
cd SWU
```

Then, configure your `.env`:

```bash
cp .env.example .env
# Open it with your prefered editor to set the variables
```

You can now follow the process of your choice:

#### Docker

1. Create the `swu-data` directory
    ```bash
    mkdir swu-data
    ```

2. Run
    ```bash
    docker compose up -d
    ```

#### Systemd service

- Deploy service
    ```bash
    sudo bash deploy-systemd.sh
    ```

#### Manually

1. Create you virtual env
    ```bash
    python3 -m venv .venv
    .venv/bin/pip3 install -r requirements.txt
    ```

2. Run it
    ```bash
    .venv/bin/gunicorn --config gunicorn_config.py main:app
    ```

### Installation

Now it's time to update your website!

Once the update is complete, use the following commands to push the changes through and trigger the porcesses correctly:

```bash
git add myfile
git commit -m "my commit"
git push
git tag v0.1.2
git push origin v0.1.2
```

The github workflow should be triggered automatically. Once this is complete, the site will be updated almost immediately.

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
