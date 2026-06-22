def build_review_prompt(
    code: str,
    changed_files: list
) -> str:

    return f"""
Review this code as a senior Team Lead.

Review the code carefully and identify issues line by line.

For each issue found provide:

Issue:
Code:
Reason:

Keep the reason short and easy to understand.

Code:

{code}
"""