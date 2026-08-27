from pathlib import Path
import zipfile


TEMPLATE = Path("assets/certificate_template.pptx")


def test_template_exists():
    assert TEMPLATE.exists()


def test_template_contains_expected_placeholders():
    with zipfile.ZipFile(TEMPLATE) as zf:
        xml = "\n".join(
            zf.read(name).decode("utf-8", errors="ignore")
            for name in zf.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )
    assert xml.count("{{name}}") == 1
    assert xml.count("{{student_id}}") == 1
    assert xml.count("{{school_name}}") == 2


def test_template_preserves_demo_markings():
    with zipfile.ZipFile(TEMPLATE) as zf:
        text = "\n".join(
            zf.read(name).decode("utf-8", errors="ignore")
            for name in zf.namelist()
            if name.endswith(".xml")
        )
    assert "SAMPLE" in text or "NOT VALID" in text
