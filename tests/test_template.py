from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from fill_certificate import EXPECTED, count_tokens  # noqa: E402


def test_template_placeholder_counts():
    template = ROOT / "assets" / "certificate_template.pptx"
    assert count_tokens(template) == EXPECTED
