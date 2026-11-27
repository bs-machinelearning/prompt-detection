"""Load the pinned prompt-injection dataset."""

from datasets import DatasetDict, load_dataset

DATASET_REVISION = "4f61ecb038e9c3fb77e21034b22511b523772cdd"


def fetch_dataset() -> DatasetDict:
    """Download and load the published dataset splits."""
    return load_dataset("deepset/prompt-injections", revision=DATASET_REVISION)


if __name__ == "__main__":
    fetch_dataset()
