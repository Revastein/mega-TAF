from typing import Iterable

import allure


def allure_description(
    test_case_title: str,
    steps: Iterable[dict[str, str | list[str] | None]],
    preconditions: Iterable[str] | None = None,
):
    """
    Generate default HTML report for a test case description

    :param test_case_title: Title
    :param steps: List of steps (dict), where each step has a required key "action"
       and an optional key "expected" (string or list of strings).
    :param preconditions: List of preconditions, if any
    """
    new_line = "<p></p>"
    html_parts = [f"{test_case_title}{new_line}"]

    if preconditions:
        preconditions_html = "<strong>Precondition:</strong><ol>"
        for condition in preconditions:
            preconditions_html += f"<li>{condition}</li>"
        preconditions_html += "</ol>"
        html_parts.append(preconditions_html)

    steps_html = "<strong>Scenario:</strong><ol>"
    for step_item in steps:
        action = step_item["action"]
        steps_html += f"<li>{action}"

        if expected := step_item.get("expected"):
            expected_results = (
                [expected] if isinstance(expected, str) else list(expected)
            )
            steps_html += f"{new_line}<em>Expected result:</em><blockquote><ul>"
            for exp in expected_results:
                steps_html += f"<li>{exp}</li>"
            steps_html += "</ul></blockquote>"

        steps_html += "</li>"
    steps_html += "</ol>"
    html_parts.append(steps_html)

    description = "".join(html_parts)
    allure.dynamic.description_html(description)
