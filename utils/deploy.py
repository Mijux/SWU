#!/usr/bin/env python3

from os.path import join
from subprocess import run, CalledProcessError

from utils.exceptions import DeployException
from utils.logger import get_logger


def deploy_tar_gz(web_root: str, content: str, strip_depth: int = 1):
    try:
        with open("/tmp/release.tar.gz", "wb") as file:
            file.write(content)

        run(["rm", "-rf", join(web_root, "*")], check=True)
        run(
            [
                "tar",
                "xzf",
                "/tmp/release.tar.gz",
                f"--strip-components={strip_depth}",
                "-C",
                web_root,
            ],
            check=True,
        )

        run(["rm", "-rf", "/tmp/release.tar.gz"], check=True)

        get_logger().info("Your website has been deployed !")
        return "Your website has been deployed !", 200

    except OSError as e:
        get_logger().error(
            "Can't create release asset file, it may be a permission problem"
        )
        get_logger().debug(str(e))
        raise DeployException(
            "Can't create release asset file, it may be a permission problem"
        )

    except CalledProcessError as e:
        get_logger().error("Error when processing asset file")
        get_logger().debug(str(e))
        raise DeployException("Error when processing asset file")
