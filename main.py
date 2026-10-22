from pathlib import Path
import file_categories


def get_src_path():
    user_dir = input("Directory path: ").strip()
    user_directory = Path(user_dir).expanduser()

    if not user_directory.is_dir():
        print("Please provide a valid directory")
        return None

    return user_directory.resolve()


def unique_destination(destination: Path):

    candidate = destination
    counter = 1

    while candidate.exists():
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )

        counter += 1

    return candidate


def get_destination(destination_directory, file_object, file_categories=file_categories.titles):

    file_ext = file_object.suffix.lower()
    file_category = file_categories.get(file_ext, "Other")

    new_category = destination_directory / file_category
    new_category.mkdir(exist_ok=True)

    destination = new_category / file_object.name

    return destination


def get_user_files(user_directory):

    user_files = (
        path
        for path in user_directory.rglob("*")
        if path.is_file())

    has_files = any(user_files)

    if not has_files:
        print("It seems no files in the directory. Can you recheck?")

    else:
        return user_files


def arrange_files(user_files, source_dir: Path):

    # The output directory will be appeared in the same parent directory of source directory.
    parent = source_dir.parent
    arranged_dir = parent / "Organized_directory"
    arranged_dir.mkdir(exist_ok=True)

    for file in user_files:

        destination = get_destination(arranged_dir, file)

        # Manages duplicate files by defining an unique name
        processed = unique_destination(destination)

        file.replace(processed)


def main():
    user_directory = get_src_path()

    if user_directory:
        user_files = get_user_files(user_directory)

        if user_files:
            arrange_files(user_files, user_directory)


main()
