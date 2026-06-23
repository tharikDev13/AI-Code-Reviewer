def build_review_prompt(
    code: str,
    changed_files: list
) -> str:

    return f"""
Review this code as a senior Team Lead.

Report only issues that are directly supported by the code shown.

For each issue provide:

Issue:
Code:
Reason:
Suggestion:

Keep the reason and suggestion short and easy to understand.

Do not provide suggested fixes.
Do not provide final code.
Do not assume missing code.
Do not speculate.

Code:

{code}
"""