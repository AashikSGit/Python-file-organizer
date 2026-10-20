from pathlib import Path
import file_categories


def handle_duplicates(base_directory, file_name):

    new_path = base_directory / "Duplicate files"
    new_path.mkdir(exist_ok=True)

    replace = new_path / file_name

    return replace


def get_destination(base_directory, file_object, file_categories=file_categories.titles):

    file_ext = file_object.suffix.lower()
    file_category = file_categories.get(file_ext, "Other")

    new_category = base_directory / file_category
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


def arrange_files(user_files):

    for file in user_files:

        arranged_dir = Path("arranged")
        arranged_dir.mkdir(exist_ok=True)

        destination = get_destination(arranged_dir, file)

        if destination.exists():

            destination = handle_duplicates(arranged_dir, file.name)

        file.replace(destination)


def main():
    user_dir = input("Give us directory path (absolute path): ")
    user_directory = Path(user_dir)

    user_files = get_user_files(user_directory)

    arrange_files(user_files)


main()
