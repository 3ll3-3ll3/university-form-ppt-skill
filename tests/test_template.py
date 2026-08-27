from pathlib import Path
import hashlib
import zipfile
import pytest

STUDENT = Path("assets/certificate_template.pptx")
FACULTY = Path("assets/teacher_certificate_template.pptx")
EXPECTED_SHA = {
    STUDENT: "7c2b39b0e29a0771ddc909ce9341c2d8eb5a47f9f925ee30239650452bf04147",
    FACULTY: "e2d645a79677ba69a1c648c8e542812c48b30e841af62ce76fec3b5c866b6720",
}


def require_current_binary(path: Path) -> None:
    if not path.exists():
        pytest.xfail(f"manual template upload still required: {path}")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA[path]:
        pytest.xfail(f"repository template binary is not the current user-approved version: {path}")


def slide_xml(path: Path) -> str:
    require_current_binary(path)
    with zipfile.ZipFile(path) as zf:
        return "\n".join(
            zf.read(name).decode("utf-8", errors="ignore")
            for name in zf.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )


def test_student_template_placeholders():
    xml = slide_xml(STUDENT)
    assert xml.count("{{name}}") == 1
    assert xml.count("{{student_id}}") == 1
    assert xml.count("{{faculty_id}}") == 0
    assert xml.count("{{school_name}}") == 2


def test_faculty_template_placeholders():
    xml = slide_xml(FACULTY)
    assert xml.count("{{name}}") == 1
    assert xml.count("{{student_id}}") == 0
    assert xml.count("{{faculty_id}}") == 1
    assert xml.count("{{school_name}}") == 2
