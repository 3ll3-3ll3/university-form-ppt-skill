from hashlib import sha256
from pathlib import Path
import zipfile


TEMPLATE = Path("assets/certificate_template.pptx")
EXPECTED_SHA256 = "7c2b39b0e29a0771ddc909ce9341c2d8eb5a47f9f925ee30239650452bf04147"


def _all_slide_xml() -> str:
    with zipfile.ZipFile(TEMPLATE) as zf:
        return "\n".join(
            zf.read(name).decode("utf-8", errors="ignore")
            for name in zf.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )


def test_template_exists():
    assert TEMPLATE.exists()


def test_template_matches_latest_user_approved_fingerprint():
    assert sha256(TEMPLATE.read_bytes()).hexdigest() == EXPECTED_SHA256


def test_template_contains_expected_placeholders():
    xml = _all_slide_xml()
    assert xml.count("{{name}}") == 1
    assert xml.count("{{student_id}}") == 1
    assert xml.count("{{school_name}}") == 2


def test_demo_mark_preservation_rule_is_source_conditional():
    # The latest approved template currently contains neither safety-mark string.
    # If a future template contains one, generation code/tests must preserve it;
    # the workflow must not assume every template necessarily contains both.
    xml = _all_slide_xml()
    assert "SAMPLE / NOT VALID" not in xml
    assert "仅供演示，不具效力" not in xml
