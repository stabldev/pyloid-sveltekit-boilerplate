from pyloid.builder import (build_from_spec, cleanup_before_build,
                            create_spec_from_json)


def main():
    spec_path = create_spec_from_json("build_config.json")
    cleanup_before_build("build_config.json")
    build_from_spec(spec_path)


if __name__ == "__main__":
    main()
