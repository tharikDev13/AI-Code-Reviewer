from git import Repo


def get_diff(
    repo_path,
    target_branch,
    source_branch
):

    repo = Repo(repo_path)

    origin = repo.remotes.origin

    origin.fetch()

    try:

        diff_output = repo.git.diff(
            f"origin/{target_branch}",
            f"origin/{source_branch}"
        )

        return diff_output

    except Exception as e:

        print(
            f"Diff Extraction Error: {e}"
        )

        return ""


def get_incremental_diff(
    repo_path,
    before_sha,
    after_sha
):

    repo = Repo(repo_path)

    try:

        diff_output = repo.git.diff(
            before_sha,
            after_sha
        )

        return diff_output

    except Exception as e:

        print(
            f"Incremental Diff Error: {e}"
        )

        return ""


def extract_added_code(
    diff_text
):

    extracted_lines = []

    current_file = None

    for line in diff_text.splitlines():

        if line.startswith(
            "diff --git"
        ):

            try:

                current_file = (
                    line.split(
                        " b/"
                    )[1]
                )

                extracted_lines.append(
                    f"\nFILE: {current_file}\n"
                )

            except Exception:
                pass

            continue

        if (
            line.startswith("index ")
            or line.startswith("---")
            or line.startswith("+++")
            or line.startswith("@@")
        ):
            continue

        if line.startswith("+"):

            extracted_lines.append(
                line[1:]
            )
    return "\n".join(
        extracted_lines
    )