import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Cross-post the same content to multiple platforms"
    )
    parser.add_argument(
        "text",
        help="The text content to post"
    )

    args = parser.parse_args()
    text = args.text

    print("Crosspost bot started")
    print(f"Post content: {text}")


if __name__ == "__main__":
    main()

