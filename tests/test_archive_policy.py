from datetime import datetime, timezone
from pathlib import Path

import pytest

from scripts.archive_record import choose_record_stem, minute_record_stem, require_real_drive_urls


def test_minute_record_stem_is_precise_to_one_minute():
    dt = datetime(2026, 8, 27, 9, 37, 59, tzinfo=timezone.utc)
    assert minute_record_stem(dt) == "2026-08-27_09-37"


def test_same_minute_collision_appends_student_id(tmp_path: Path):
    dt = datetime(2026, 8, 27, 9, 37, tzinfo=timezone.utc)
    (tmp_path / "2026-08-27_09-37.md").write_text("x", encoding="utf-8")
    assert choose_record_stem(tmp_path, "6483275", dt) == "2026-08-27_09-37_6483275"


def test_final_archive_requires_real_drive_urls():
    with pytest.raises(SystemExit):
        require_real_drive_urls("", "", prepare_only=False)


def test_real_drive_urls_are_accepted():
    require_real_drive_urls(
        "https://docs.google.com/presentation/d/example/edit",
        "https://drive.google.com/file/d/example/view",
        prepare_only=False,
    )


def test_prepare_only_is_not_final_completion():
    require_real_drive_urls("", "", prepare_only=True)
