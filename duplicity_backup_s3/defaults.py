import os
import platform
from pathlib import Path

# default config file name
CONFIG_FILENAME = "duplicity_backup_s3.yaml"
CONFIG_FILEPATH = Path.cwd() / CONFIG_FILENAME

# Schema to check config file against
CONFIG_SCHEMA_FILENAME = "schema.yaml"
CONFIG_SCHEMA_PATH = Path(Path(__file__).parent / "files" / CONFIG_SCHEMA_FILENAME)

FULL_IF_OLDER_THAN = "7D"
DUPLICITY_BASIC_ARGS = [
    "--s3-european-buckets",
    "--s3-use-new-style",
    "--no-encryption",
]
DUPLICITY_BACKUP_ARGS = ["--asynchronous-upload", "--exclude-device-files"]
DUPLICITY_VERBOSITY = 3
DUPLICITY_MORE_VERBOSITY = DUPLICITY_VERBOSITY + 1
DUPLICITY_DEBUG_VERBOSITY = 5

__platform = platform.system()
ON_LINUX = os.name == "posix" or __platform == "Linux"
ON_MACOS = os.name == "mac" or __platform == "Darwin"
ON_WINDOWS = NEED_SUBPROCESS_SHELL = os.name == "nt" or __platform == "Windows"

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"], "max_content_width": 88}
UNKNOWN_OPTIONS = {"ignore_unknown_options": True}.update(CONTEXT_SETTINGS)

EMPTY_CONFIGFILE = dict(
    aws=dict(
        AWS_ACCESS_KEY_ID="foobar_aws_key_id",
        AWS_SECRET_ACCESS_KEY="foobar_aws_access_key",
    ),
    backuproot="/path/to/backup/",
    includes=["/full/path/to_include", "/another/path/to_include"],
    excludes=["/full/path/to_exclude", "/another/path/to_exclude"],
    remote=dict(bucket="<bucketname>", path="<path>"),
    full_if_older_than="7D",
)
