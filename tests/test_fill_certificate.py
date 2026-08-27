from pathlib import Path
import hashlib
import zipfile
import pytest

from scripts.fill_certificate import fill

STUDENT = Path("assets/certificate_template.pptx")
FACULTY = Path("assets/teacher_certificate_template.pptx")
EXPECTED_SHA = {
    STUDENT: "7c2b39b0e29a0771ddc909ce9341c2d8eb5a47f9f925ee30239650452bf04147",
    FACULTY: "e2d645a79677ba69a1c648c8e542812c48b30e841af62ce76fec3b5c866b6720",
}


def require_current_binary(path: Path) -> None:
    if not path.exists():
        pytest.xfail(f"manual template upload still required: {path}")
    if hashlib.sha256(path.read_bytes()).hexdigest() != EXPECTED_SHA[path]:
        pytest.xfail(f"repository template binary is not current: {path}")


def all_slide_xml(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        return "\n".join(
            zf.read(n).decode("utf-8", errors="ignore")
            for n in zf.namelist()
            if n.startswith("ppt/slides/slide") and n.endswith(".xml")
        )


def test_student_fill(tmp_path: Path):
    require_current_binary(STUDENT)
    out = tmp_path / "student.pptx"
    fill(STUDENT, out, "student", "Li An", "1234567", "Soochow University")
    xml = all_slide_xml(out)
    assert "{{student_id}}" not in xml
    assert "1234567" in xml


def test_faculty_fill(tmp_path: Path):
    require_current_binary(FACULTY)
    out = tmp_path / "faculty.pptx"
    fill(FACULTY, out, "faculty", "Li An", "1234567", "Soochow University")
    xml = all_slide_xml(out)
    assert "{{faculty_id}}" not in xml
    assert "1234567" in xml
