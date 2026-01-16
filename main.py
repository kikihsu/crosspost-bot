import argparse

SUPPORTED_PLATFORMS = ["twitter", "instagram", "bluesky", "plurk"]


def main():
    parser = argparse.ArgumentParser(
        description="Cross-post the same content to multiple platforms"
    )
    parser.add_argument(
        "text",
        help="The text content to post"
    )
    parser.add_argument(
        "--platform",
        default="all",
        choices=SUPPORTED_PLATFORMS + ["all"],
        help="Target platform (default: all)"
    )

    args = parser.parse_args()
    text = args.text
    platform = args.platform

    print("Crosspost bot started")
    print(f"Post content: {text}")

    if platform == "all":
        targets = SUPPORTED_PLATFORMS
    else:
        targets = [platform]

    print(f"Platforms to post: {', '.join(targets)}")


if __name__ == "__main__":
    main()
