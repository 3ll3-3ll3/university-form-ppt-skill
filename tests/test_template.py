from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from fill_certificate import EXPECTED, count_tokens  # noqa: E402
from random_identity import generate_identity  # noqa: E402


def test_template_placeholder_counts():
    template = ROOT / "assets" / "certificate_template.pptx"
    assert count_tokens(template) == EXPECTED


def test_default_identity_is_layout_friendly():
    identity = generate_identity(seed=1)
    assert len(identity["student_id"]) == 8
    assert identity["student_id"].isdigit()
    assert len(identity["name"]) <= 12


def test_nine_digit_identity_is_supported_for_render_checked_cases():
    identity = generate_identity(seed=1, student_id_length=9)
    assert len(identity["student_id"]) == 9
    assert identity["student_id"].isdigit()
